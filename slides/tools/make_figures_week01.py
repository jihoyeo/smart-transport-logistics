#!/usr/bin/env python3
"""
Lecture figures for week 1 (교재 0장) — drawn from the textbook's recorded run.

Run with the textbook venv so `smartmob` and the fixtures resolve:
    cd ~/lecture/mobility-simulation-book && .venv/bin/python \
        <this repo>/slides/tools/make_figures_week01.py

Writes slides/week01/figures/ch00_record.png next to that week's deck.
색은 week02 그림과 같은 팔레트를 쓴다.
"""
from __future__ import annotations

import os
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

OUT = Path(__file__).resolve().parents[1] / "week01" / "figures"
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
    "lines.linewidth": 2, "legend.frameon": False,
})


def main() -> None:
    os.environ.setdefault("SMARTMOB_OFFLINE", "1")
    from smartmob import Dtumos

    sim = Dtumos().run_simulation(
        city="hanam", mode="taxi", fleet_size=80, num_passengers=1000,
        time_start=1080, time_end=1440, random_seed=42,
    )
    rec = sim.record
    minutes = rec["time"] if "time" in rec else range(len(rec))
    hours = [m / 60 for m in minutes]
    driving = rec["driving_vehicle_cnt"]
    empty = rec["empty_vehicle_cnt"]
    on_duty = driving + empty

    fig, ax = plt.subplots(figsize=(7.2, 4.8))           # 불릿 옆 자리 3:2
    ax.plot(hours, driving, color=NAVY, label="운행 중 차량")
    ax.plot(hours, empty, color=ORANGE, linestyle="--", label="대기 중 차량")
    ax.plot(hours, on_duty, color=GRAY, linestyle=":", label="근무 중 합계")
    ax.set_xlabel("시각"); ax.set_ylabel("차량 수")
    ax.set_xticks(range(18, 25))
    ax.set_xticklabels([f"{h % 24:02d}:00" for h in range(18, 25)])
    ax.legend(loc="lower left", ncol=1)
    fig.tight_layout(); fig.savefig(OUT / "ch00_record.png"); plt.close(fig)
    print("wrote", OUT / "ch00_record.png",
          f"on_duty max {on_duty.max()} min {on_duty.min()}")


if __name__ == "__main__":
    main()
