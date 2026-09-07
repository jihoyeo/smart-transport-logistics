#!/usr/bin/env python3
"""공용 덱을 AI 모빌리티 저장소로 복사한다.

    python slides/tools/sync_common.py            # 다른 파일을 복사한다
    python slides/tools/sync_common.py --check    # 복사하지 않고 다른 파일만 알려 준다

원본은 이 저장소의 slides/common 이고, 사본은 AI 모빌리티 저장소의 같은 경로다.
대상 경로는 기본값이 ../ai-mobility 이고 AI_MOBILITY 환경변수로 바꿀 수 있다.

원고를 고쳤으면 pptx 를 먼저 다시 만들고 이 스크립트를 돌린다. 두 저장소의
파일이 한 글자도 다르지 않게 두는 것이 목적이다.
"""
from __future__ import annotations

import filecmp
import os
import shutil
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "common"
DEFAULT_DST = Path(__file__).resolve().parents[3] / "ai-mobility"


def files() -> list[Path]:
    return sorted(p for p in SRC.rglob("*") if p.is_file() and p.suffix != ".json")


def main(argv: list[str]) -> int:
    check_only = "--check" in argv
    dst_root = Path(os.environ.get("AI_MOBILITY", DEFAULT_DST))
    dst_common = dst_root / "slides" / "common"
    if not dst_root.exists():
        print(f"대상 저장소가 없습니다: {dst_root}")
        return 2

    differing: list[str] = []
    for src in files():
        rel = src.relative_to(SRC)
        dst = dst_common / rel
        same = dst.exists() and filecmp.cmp(src, dst, shallow=False)
        if same:
            continue
        differing.append(str(rel))
        if not check_only:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    if not differing:
        print(f"{len(files())}개 파일, 두 저장소가 같습니다")
        return 0

    verb = "다릅니다" if check_only else "복사했습니다"
    print(f"{len(differing)}개 파일 {verb}")
    for name in differing:
        print(f"  - {name}")
    return 1 if check_only else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
