#!/usr/bin/env python3
"""
Figure for the shared dev-environment deck (slides/common/dev_env.md).

Draws the tool landscape: editors and terminal agents both act on one project
folder, and an orchestrator runs several agents on separate worktrees.

Run with any python that has matplotlib:
    python slides/tools/make_figures_common.py

Writes slides/common/figures/tools_landscape.png.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).resolve().parents[1] / "common" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

for cand in ("Pretendard", "AppleGothic", "Malgun Gothic"):
    if any(f.name == cand for f in font_manager.fontManager.ttflist):
        plt.rcParams["font.family"] = cand
        break
plt.rcParams.update({"font.size": 13, "axes.unicode_minus": False})

DARK, MID, LIGHT = "0.15", "0.45", "0.75"


def box(ax, x, y, w, h, title, sub, edge=DARK, style="round,pad=0.02", dashed=False):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle=style, linewidth=1.6, edgecolor=edge,
        facecolor="white", linestyle="--" if dashed else "-", zorder=3,
    ))
    ax.text(x + w / 2, y + h * 0.62, title, ha="center", va="center",
            fontsize=14, fontweight="bold", color=DARK, zorder=4)
    ax.text(x + w / 2, y + h * 0.26, sub, ha="center", va="center",
            fontsize=12, color=MID, zorder=4)


def arrow(ax, p, q, style="-|>"):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=14,
                                 linewidth=1.4, color=MID, zorder=2))


fig, ax = plt.subplots(figsize=(11.8, 4.7))   # 전체 폭 자리 2.5:1
ax.set_xlim(0, 11.8)
ax.set_ylim(0, 4.7)
ax.axis("off")

box(ax, 0.2, 2.75, 3.1, 1.3, "편집기", "VS Code · Antigravity")
box(ax, 0.2, 0.65, 3.1, 1.3, "터미널 에이전트", "Claude Code · Codex")
box(ax, 4.4, 1.7, 2.7, 1.4, "프로젝트 폴더", "코드 · 데이터 · 결과")

arrow(ax, (3.3, 3.4), (4.4, 2.75))
arrow(ax, (3.3, 1.3), (4.4, 2.05))

box(ax, 8.0, 0.45, 3.5, 3.8, "", "", edge=LIGHT, dashed=True)
ax.text(9.75, 3.95, "Orca — 병렬 실행", ha="center", va="center",
        fontsize=13, color=MID)
for i, y in enumerate((2.60, 1.60, 0.60)):
    box(ax, 8.35, y, 2.8, 0.80, f"에이전트 {i + 1}", f"worktree {i + 1}", edge=MID)
arrow(ax, (7.1, 2.4), (8.0, 2.4))

ax.text(5.75, 1.35, "같은 폴더를 사람과 에이전트가 함께 고친다",
        ha="center", va="center", fontsize=12, color=MID)

fig.tight_layout()
fig.savefig(OUT / "tools_landscape.png", dpi=200)
plt.close(fig)
print(OUT / "tools_landscape.png")
