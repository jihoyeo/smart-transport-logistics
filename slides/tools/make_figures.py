#!/usr/bin/env python3
"""
Lecture figures for week 2 (교재 2장) — drawn from the textbook's Hanam data.

Run with the textbook venv so `smartmob` and the parquet data resolve:
    cd ~/lecture/mobility-simulation-book && .venv/bin/python \
        ~/lecture/smart-transport-logistics/slides/tools/make_figures.py

Writes slides/week02/figures/ch02_*.png next to that week's deck.
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.collections import LineCollection
import pandas as pd
from scipy.spatial import cKDTree

from smartmob.data import data_path
from smartmob.teaching.graph import haversine_km

OUT = Path(__file__).resolve().parents[1] / "week02" / "figures"
OUT.mkdir(parents=True, exist_ok=True)
NAVY, ORANGE, GRAY = "#1F3A5F", "#C2410C", "#9CA3AF"

for cand in ("Pretendard", "AppleGothic", "Malgun Gothic"):
    if any(f.name == cand for f in font_manager.fontManager.ttflist):
        plt.rcParams["font.family"] = cand
        break
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.dpi"] = 150

DRIVE = {
    "motorway", "motorway_link", "trunk", "trunk_link",
    "primary", "primary_link", "secondary", "secondary_link",
    "tertiary", "tertiary_link",
    "residential", "living_street", "unclassified", "service", "road",
}


def parse_edge_id(edge_id: str) -> tuple[str, str]:
    _, source_osm, target_osm = edge_id.rsplit("_", 2)
    return f"n{source_osm}", f"n{target_osm}"


def segments(edges: pd.DataFrame, coord: dict) -> list:
    segs = []
    for edge_id in edges["edge_id"]:
        u, v = parse_edge_id(edge_id)
        if u in coord and v in coord:
            (ulat, ulon), (vlat, vlon) = coord[u], coord[v]
            segs.append([(ulon, ulat), (vlon, vlat)])
    return segs


def draw_network(ax, segs, color, lw, title):
    ax.add_collection(LineCollection(segs, colors=color, linewidths=lw))
    ax.autoscale()
    ax.set_aspect(1 / 0.79)          # ~cos(37.5°): keep Hanam's shape
    ax.set_title(title, fontsize=13)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)


def main() -> None:
    nodes = pd.read_parquet(data_path("hanam/road_graph_nodes.parquet"))
    edges = pd.read_parquet(data_path("hanam/road_graph_edges.parquet"))
    coord = {r.node_id: (r.lat, r.lon) for r in nodes.itertuples(index=False)}
    drive = edges[edges["highway"].isin(DRIVE)]
    all_segs, drive_segs = segments(edges, coord), segments(drive, coord)
    print(f"edges {len(edges):,} / drive {len(drive):,}; "
          f"km {edges['length'].sum()/1000:,.0f} -> {drive['length'].sum()/1000:,.0f}")

    # 1. drive network alone
    fig, ax = plt.subplots(figsize=(11, 6.5))
    draw_network(ax, drive_segs, NAVY, 0.35, "")
    fig.tight_layout(); fig.savefig(OUT / "ch02_network_drive.png"); plt.close(fig)

    # 2. highway counts (top 10)
    counts = edges["highway"].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(11, 5))
    colors = [ORANGE if h in ("footway", "cycleway", "path", "steps", "pedestrian") else NAVY
              for h in counts.index]
    ax.barh(counts.index[::-1], counts.values[::-1], color=colors[::-1])
    for y, v in enumerate(counts.values[::-1]):
        ax.text(v + 300, y, f"{v:,}", va="center", fontsize=11)
    ax.set_xlabel("엣지 수"); ax.set_xlim(0, counts.max() * 1.15)
    ax.text(0.98, 0.05, "주황: 보행·자전거 전용", transform=ax.transAxes, ha="right",
            color=ORANGE, fontsize=11)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.tight_layout(); fig.savefig(OUT / "ch02_highway_counts.png"); plt.close(fig)

    # 3. before / after
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    draw_network(axes[0], all_segs, GRAY, 0.3,
                 f"전체 엣지 {len(edges):,}개 · {edges['length'].sum()/1000:,.0f} km")
    draw_network(axes[1], drive_segs, NAVY, 0.35,
                 f"자동차 엣지 {len(drive):,}개 · {drive['length'].sum()/1000:,.0f} km")
    fig.tight_layout(); fig.savefig(OUT / "ch02_network_before_after.png"); plt.close(fig)

    # 4. snapping around city hall
    hall = (37.5393, 127.2148)
    drive_nodes = sorted({n for e in drive["edge_id"] for n in parse_edge_id(e) if n in coord})
    tree = cKDTree([coord[n] for n in drive_nodes])
    _, idx = tree.query(hall)
    near = drive_nodes[idx]
    nlat, nlon = coord[near]
    dist_m = haversine_km(*hall, nlat, nlon) * 1000
    fig, ax = plt.subplots(figsize=(8, 6.5))
    r = 0.006
    local = [s for s in drive_segs if abs(s[0][1] - hall[0]) < r and abs(s[0][0] - hall[1]) < r * 1.3]
    ax.add_collection(LineCollection(local, colors=GRAY, linewidths=1.2))
    pts = [(coord[n][1], coord[n][0]) for n in drive_nodes
           if abs(coord[n][0] - hall[0]) < r and abs(coord[n][1] - hall[1]) < r * 1.3]
    ax.scatter([p[0] for p in pts], [p[1] for p in pts], s=14, color=NAVY, zorder=3, label="도로망 노드")
    ax.scatter([hall[1]], [hall[0]], s=140, marker="*", color=ORANGE, zorder=5, label="하남시청 좌표")
    ax.scatter([nlon], [nlat], s=90, facecolors="none", edgecolors=ORANGE, linewidths=2, zorder=5,
               label=f"가장 가까운 노드 {near} ({dist_m:.0f} m)")
    ax.plot([hall[1], nlon], [hall[0], nlat], color=ORANGE, linewidth=1.5, zorder=4)
    ax.set_xlim(hall[1] - r * 1.3, hall[1] + r * 1.3); ax.set_ylim(hall[0] - r, hall[0] + r)
    ax.set_aspect(1 / 0.79); ax.set_xticks([]); ax.set_yticks([])
    ax.legend(loc="lower right", fontsize=10, frameon=True)
    for s in ax.spines.values():
        s.set_visible(False)
    fig.tight_layout(); fig.savefig(OUT / "ch02_snap.png"); plt.close(fig)
    print("wrote", sorted(p.name for p in OUT.glob("ch02_*.png")), f"snap {near} {dist_m:.0f} m")


if __name__ == "__main__":
    main()
