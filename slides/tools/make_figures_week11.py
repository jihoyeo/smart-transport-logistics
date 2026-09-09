#!/usr/bin/env python3
"""
Lecture figures for week 11 (교재 11장) — drawn from the textbook's simulation loop.

Run with the textbook venv so `smartmob` resolves:
    cd ~/lecture/mobility-simulation-book && .venv/bin/python \
        <this repo>/slides/tools/make_figures_week11.py

Writes slides/week11/figures/ch11_fleet.png next to that week's deck.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

from smartmob.data import load_demand, load_vehicles
from smartmob.teaching.simloop import simulate

OUT = Path(__file__).resolve().parents[1] / "week11" / "figures"
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


def main() -> None:
    demand, vehicles = load_demand("hanam"), load_vehicles("hanam")
    fleets = (20, 30, 40, 50, 60, 70, 80)
    waits, rates = [], []
    for n in fleets:
        s = simulate(demand, vehicles.head(n), 1080, 1440).summary()
        waits.append(s["avg_waiting_time_min"])
        rates.append(s["service_rate"])

    fig, ax1 = plt.subplots(figsize=(7.2, 4.8))       # 불릿 옆 자리 3:2
    ax1.plot(fleets, waits, "o-", color=ORANGE, label="평균 대기")
    ax1.set_xlabel("차량 대수"); ax1.set_ylabel("평균 대기 (분)", color=ORANGE)
    ax1.tick_params(axis="y", labelcolor=ORANGE)

    ax2 = ax1.twinx()
    ax2.plot(fleets, rates, "s--", color=NAVY, label="서비스율")
    ax2.set_ylabel("서비스율", color=NAVY)
    ax2.tick_params(axis="y", labelcolor=NAVY)
    ax2.spines["top"].set_visible(False)

    ax1.grid(alpha=0.25, linewidth=0.6)
    fig.tight_layout(); fig.savefig(OUT / "ch11_fleet.png"); plt.close(fig)

    print("wrote", OUT / "ch11_fleet.png")
    for n, w, r in zip(fleets, waits, rates):
        print(f"  {n}대  평균대기 {w:.2f}분  서비스율 {r:.3f}")


if __name__ == "__main__":
    main()
