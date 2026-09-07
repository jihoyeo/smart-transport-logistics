#!/usr/bin/env python3
"""
Lecture figures for week 4 (교재 4장) — drawn from the textbook's Hanam data.

Run with the textbook venv so `smartmob` and the parquet data resolve:
    cd ~/lecture/mobility-simulation-book && .venv/bin/python \
        <this repo>/slides/tools/make_figures_week04.py

Writes slides/week04/figures/ch04_*.png and ch05_*.png next to that week's decks.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

from smartmob.data import load_gtfs, load_road_graph
from smartmob.teaching.dijkstra import dijkstra

OUT = Path(__file__).resolve().parents[1] / "week04" / "figures"
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

HALL, MISA = (37.5393, 127.2148), (37.5606, 127.1930)
SLOTS = [
    ("새벽 6시", "weekday_offpeak_p50"),
    ("오전 8시", "weekday_am_peak_p50"),
    ("낮 11시", "weekday_midday_p50"),
    ("오후 6시", "weekday_pm_peak_p50"),
    ("심야 23시", "weekday_night_p50"),
]


def travel_time_by_slot() -> None:
    base = load_road_graph("hanam", modes=("drive",))
    start, goal = base.nearest_node(*HALL), base.nearest_node(*MISA)
    free = dijkstra(base, start, goal).duration_s / 60

    labels, minutes = [], []
    for label, col in SLOTS:
        g = load_road_graph("hanam", modes=("drive",), speed_column=col)
        minutes.append(dijkstra(g, start, goal).duration_s / 60)
        labels.append(label)

    fig, ax = plt.subplots(figsize=(7.2, 4.8))     # 불릿 옆 자리 3:2
    ax.bar(labels, minutes, color=NAVY, width=0.55)
    ax.axhline(free, color=ORANGE, linestyle="--", linewidth=1.5)
    ax.text(len(labels) - 0.4, free + 0.12, f"자유류 {free:.1f}분",
            color=ORANGE, ha="right", fontsize=12)
    ax.set_ylabel("소요시간 (분)")
    ax.grid(axis="y", alpha=0.25, linewidth=0.6)
    fig.tight_layout(); fig.savefig(OUT / "ch04_time_of_day.png"); plt.close(fig)
    print("wrote", OUT / "ch04_time_of_day.png",
          " ".join(f"{l} {m:.2f}분" for l, m in zip(labels, minutes)),
          f"| 자유류 {free:.2f}분")


def gtfs_stops() -> None:
    stops = load_gtfs("hanam")["stops"]
    fig, ax = plt.subplots(figsize=(7.2, 4.8))     # 불릿 옆 자리 3:2
    ax.scatter(stops["stop_lon"], stops["stop_lat"], s=3, alpha=0.5, color=NAVY)
    ax.set_xlabel("경도"); ax.set_ylabel("위도")
    ax.set_aspect(1 / 0.79)      # 위도 37도에서 경도 1도가 더 짧다
    fig.tight_layout(); fig.savefig(OUT / "ch05_stops.png"); plt.close(fig)
    print("wrote", OUT / "ch05_stops.png", f"정류장 {len(stops):,}개")


if __name__ == "__main__":
    travel_time_by_slot()
    gtfs_stops()
