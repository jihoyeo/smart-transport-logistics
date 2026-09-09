#!/usr/bin/env python3
"""
Lecture figures for week 7 (교재 8장) — drawn from the textbook's Hanam data.

Run with the textbook venv so `smartmob` and the parquet data resolve:
    cd ~/lecture/mobility-simulation-book && .venv/bin/python \
        <this repo>/slides/tools/make_figures_week07.py

Writes slides/week07/figures/ch08_*.png and ch12_*.png next to that week's decks.
"""
from __future__ import annotations

from pathlib import Path

import geopandas as gpd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager

from smartmob.data import data_path, load_demand, load_road_graph, load_vehicles
from smartmob.teaching.demand_gen import generate_demand
from smartmob.teaching.metrics import kpi_table
from smartmob.teaching.simloop import simulate

OUT = Path(__file__).resolve().parents[1] / "week07" / "figures"
OUT.mkdir(parents=True, exist_ok=True)
NAVY, ORANGE, GRAY = "#1F3A5F", "#C2410C", "#9CA3AF"

for cand in ("Pretendard", "AppleGothic", "Malgun Gothic"):
    if any(f.name == cand for f in font_manager.fontManager.ttflist):
        plt.rcParams["font.family"] = cand
        break
plt.rcParams.update({
    "axes.unicode_minus": False, "figure.dpi": 200,
    "font.size": 14, "axes.labelsize": 14, "legend.fontsize": 13,
    "axes.spines.top": False, "axes.spines.right": False,
})


def hourly() -> None:
    od = pd.read_parquet(data_path("hanam/od_2024.parquet"))
    by_hour = od.groupby("ST_TIME_CD")["CNT"].sum()
    fig, ax = plt.subplots(figsize=(11.8, 4.7))       # 전체 폭 자리 2.5:1
    ax.bar(by_hour.index, by_hour.values, color=NAVY, width=0.7)
    ax.set_xlabel("출발 시각 (시)"); ax.set_ylabel("통행량 (명)")
    ax.set_xticks(range(0, 24, 2))
    ax.grid(axis="y", alpha=0.25, linewidth=0.6)
    fig.tight_layout(); fig.savefig(OUT / "ch08_hourly.png"); plt.close(fig)
    top = by_hour.sort_values(ascending=False).head(3)
    print("wrote", OUT / "ch08_hourly.png",
          " ".join(f"{h}시 {c:,.0f}명" for h, c in top.items()))


def sampling() -> None:
    boundary = gpd.read_file(data_path("hanam/boundary.geojson")).geometry.iloc[0]
    graph = load_road_graph("hanam", modes=("drive",))
    uniform = generate_demand(boundary=boundary, n=800, seed=1, hourly=None)
    on_road = generate_demand(graph=graph, n=800, seed=1, hourly=None)

    fig, axes = plt.subplots(1, 2, figsize=(11.8, 4.7))   # 전체 폭 자리 2.5:1
    for ax, df, color, title in [
        (axes[0], uniform, ORANGE, "경계 안 균등 샘플링"),
        (axes[1], on_road, NAVY, "도로 위 샘플링"),
    ]:
        gpd.GeoSeries([boundary]).plot(ax=ax, facecolor="none",
                                       edgecolor=GRAY, linewidth=0.8)
        ax.scatter(df["origin_lon"], df["origin_lat"], s=6, alpha=0.5, color=color)
        ax.set_title(title, fontsize=14)
        ax.set_xticks([]); ax.set_yticks([]); ax.set_aspect(1 / 0.79)
        for sp in ax.spines.values():
            sp.set_visible(False)
    fig.tight_layout(); fig.savefig(OUT / "ch08_sampling.png"); plt.close(fig)
    print("wrote", OUT / "ch08_sampling.png", f"각 {len(uniform)}건")


def wait_hist_and_pareto() -> None:
    demand, vehicles = load_demand("hanam"), load_vehicles("hanam")
    fleets = (20, 30, 40, 50, 60, 70, 80)
    runs = {n: simulate(demand, vehicles.head(n), 1080, 1440) for n in fleets}

    fig, ax = plt.subplots(figsize=(7.2, 4.8))         # 불릿 옆 자리 3:2
    for n, color in ((20, ORANGE), (80, NAVY)):
        waits = [r.wait_min for r in runs[n].requests if r.pickup_time is not None]
        ax.hist(waits, bins=30, alpha=0.6, color=color,
                label=f"{n}대 (배차 {len(waits)}명)")
    ax.set_xlabel("대기시간 (분)"); ax.set_ylabel("승객 수")
    ax.legend(); ax.grid(alpha=0.25, linewidth=0.6)
    fig.tight_layout(); fig.savefig(OUT / "ch12_wait_hist.png"); plt.close(fig)

    xs, ys = [], []
    for n in fleets:
        k = kpi_table(runs[n])
        xs.append(k["service_rate"]); ys.append(k["utilization"])

    fig, ax = plt.subplots(figsize=(7.2, 4.8))         # 불릿 옆 자리 3:2
    ax.plot(xs, ys, "-o", color=NAVY)
    for x, y, n in zip(xs, ys, fleets):
        ax.annotate(f"{n}대", (x, y), textcoords="offset points",
                    xytext=(8, 5), fontsize=12)
    ax.set_xlabel("서비스율"); ax.set_ylabel("차량 가동률")
    ax.grid(alpha=0.25, linewidth=0.6)
    fig.tight_layout(); fig.savefig(OUT / "ch12_pareto.png"); plt.close(fig)

    print("wrote", OUT / "ch12_wait_hist.png", "및 ch12_pareto.png")
    for n, x, y in zip(fleets, xs, ys):
        print(f"  {n}대  서비스율 {x:.3f}  가동률 {y:.3f}")


if __name__ == "__main__":
    hourly()
    sampling()
    wait_hist_and_pareto()
