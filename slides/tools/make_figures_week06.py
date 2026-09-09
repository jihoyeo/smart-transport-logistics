#!/usr/bin/env python3
"""
Lecture figures for week 6 (교재 7장) — drawn from the textbook's Hanam GTFS.

Run with the textbook venv so `smartmob` and the GTFS data resolve:
    cd ~/lecture/mobility-simulation-book && .venv/bin/python \
        <this repo>/slides/tools/make_figures_week06.py

Writes slides/week06/figures/ch07_components.png next to that week's deck.
"""
from __future__ import annotations

import random
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

from smartmob.data import load_gtfs
from smartmob.teaching.raptor import INF, TransitData, journey, raptor, summarize

OUT = Path(__file__).resolve().parents[1] / "week06" / "figures"
OUT.mkdir(parents=True, exist_ok=True)
NAVY, ORANGE, GRAY = "#1F3A5F", "#C2410C", "#9CA3AF"
HALL = (37.5393, 127.2148)

for cand in ("Pretendard", "AppleGothic", "Malgun Gothic"):
    if any(f.name == cand for f in font_manager.fontManager.ttflist):
        plt.rcParams["font.family"] = cand
        break
plt.rcParams.update({
    "axes.unicode_minus": False, "figure.dpi": 200,
    "font.size": 14, "axes.labelsize": 14, "legend.fontsize": 13,
    "axes.spines.top": False, "axes.spines.right": False,
})


def main() -> None:
    data = TransitData.from_gtfs(load_gtfs("hanam"))
    origins = data.access_stops(*HALL)
    result = raptor(data, origins, 8 * 3600)

    reachable = [i for i, t in enumerate(result.best) if t < INF]
    rng = random.Random(7)
    rows = []
    for stop in rng.sample(reachable, 300):
        s = summarize(data, journey(data, result, stop), 8 * 3600)
        if s.get("reachable") and s["total_min"] <= 180:   # 극단값 제외
            rows.append(s)

    parts = ["in_vehicle_min", "walk_min", "wait_min"]
    labels = ["차내", "도보", "대기"]
    series = [[r[c] for r in rows] for c in parts]

    fig, ax = plt.subplots(figsize=(7.2, 4.8))       # 불릿 옆 자리 3:2
    bp = ax.boxplot(series, tick_labels=labels, patch_artist=True, widths=0.5,
                    medianprops=dict(color=ORANGE, linewidth=2),
                    flierprops=dict(marker="o", markersize=3, markerfacecolor=GRAY,
                                    markeredgecolor=GRAY, alpha=0.5))
    for patch in bp["boxes"]:
        patch.set_facecolor(NAVY); patch.set_alpha(0.35); patch.set_edgecolor(NAVY)
    ax.set_ylabel("시간 (분)")
    ax.grid(axis="y", alpha=0.25, linewidth=0.6)
    fig.tight_layout(); fig.savefig(OUT / "ch07_components.png"); plt.close(fig)

    total = sum(sum(s) for s in series)
    shares = " ".join(f"{l} {sum(s) / total:.1%}" for l, s in zip(labels, series))
    print("wrote", OUT / "ch07_components.png", f"표본 {len(rows)}건 | {shares}")


if __name__ == "__main__":
    main()
