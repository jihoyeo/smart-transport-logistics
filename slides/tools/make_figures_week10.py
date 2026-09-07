#!/usr/bin/env python3
"""
Lecture figures for week 10 (교재 9장) — drawn from the textbook's ETA dataset.

Run with the textbook venv so `smartmob`, scikit-learn and LightGBM resolve:
    cd ~/lecture/mobility-simulation-book && .venv/bin/python \
        <this repo>/slides/tools/make_figures_week10.py

Writes slides/week10/figures/ch09_*.png and ch10_*.png next to that week's decks.
"""
from __future__ import annotations

from pathlib import Path

import lightgbm as lgb
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

from smartmob.data import data_path
from smartmob.teaching.eta import FEATURES, TARGET
from smartmob.teaching.dispatch import nearest_neighbour, route_length_km, two_opt

OUT = Path(__file__).resolve().parents[1] / "week10" / "figures"
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


def eta_error() -> None:
    df = pd.read_parquet(data_path("hanam/eta_samples.parquet"))
    X_train, X_test, y_train, y_test = train_test_split(
        df[FEATURES], df[TARGET], test_size=0.2, random_state=42)

    model = lgb.LGBMRegressor(n_estimators=400, learning_rate=0.05,
                              num_leaves=31, random_state=42, verbose=-1)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    error = pred - y_test

    fig, axes = plt.subplots(1, 2, figsize=(11.8, 4.7))   # 전체 폭 자리 2.5:1
    axes[0].scatter(y_test, pred, s=3, alpha=0.2, color=NAVY)
    lim = [0, float(y_test.max())]
    axes[0].plot(lim, lim, color=ORANGE, linewidth=1.5, linestyle="--")
    axes[0].set_xlabel("실제 (분)"); axes[0].set_ylabel("예측 (분)")

    axes[1].scatter(X_test["straight_km"], error, s=3, alpha=0.2, color=NAVY)
    axes[1].axhline(0, color=ORANGE, linewidth=1.5, linestyle="--")
    axes[1].set_xlabel("직선거리 (km)"); axes[1].set_ylabel("오차 (분)")

    for ax in axes:
        ax.grid(alpha=0.25, linewidth=0.6)
    fig.tight_layout(); fig.savefig(OUT / "ch09_error.png"); plt.close(fig)

    print("wrote", OUT / "ch09_error.png",
          f"MAE {mean_absolute_error(y_test, pred):.2f}분  R² {r2_score(y_test, pred):.3f}")
    bins = pd.cut(X_test["straight_km"], [0, 2, 4, 6, 8, 20])
    print(abs(error).groupby(bins, observed=True).mean().round(2).to_string())


def tsp_two_opt() -> None:
    import random
    rng = random.Random(3)
    stops = [(37.50 + rng.random() * 0.10, 127.13 + rng.random() * 0.14)
             for _ in range(12)]
    nn = nearest_neighbour(stops)
    improved = two_opt(stops, nn)

    fig, axes = plt.subplots(1, 2, figsize=(11.8, 4.7))   # 전체 폭 자리 2.5:1
    for ax, (label, order) in zip(axes, [("최근접 이웃", nn), ("2-opt", improved)]):
        seq = order + [order[0]]
        ax.plot([stops[i][1] for i in seq], [stops[i][0] for i in seq],
                "-o", color=NAVY, markersize=6, linewidth=1.4)
        ax.scatter(stops[order[0]][1], stops[order[0]][0], s=110,
                   color=ORANGE, zorder=3)
        ax.set_title(f"{label}  {route_length_km(stops, order):.1f} km", fontsize=14)
        ax.set_xticks([]); ax.set_yticks([]); ax.set_aspect(1 / 0.79)
        for sp in ax.spines.values():
            sp.set_visible(False)
    fig.tight_layout(); fig.savefig(OUT / "ch10_tsp.png"); plt.close(fig)
    print("wrote", OUT / "ch10_tsp.png",
          f"최근접 {route_length_km(stops, nn):.2f} km → 2-opt {route_length_km(stops, improved):.2f} km")


if __name__ == "__main__":
    eta_error()
    tsp_two_opt()
