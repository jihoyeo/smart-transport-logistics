#!/usr/bin/env python3
"""
슬라이드 원고 문체 검사.

md2pptx의 reference/writing-guide.md §5·§6에 있는 규칙 중
기계로 잡을 수 있는 것만 검사한다. 빌더의 넘침 경고와는 별개다.

    python3 slides/tools/check_style.py slides/week01/ch01_why.md
    python3 slides/tools/check_style.py slides/*/*.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# 은유·비유 — 슬라이드에서도 노트에서도 쓰지 않는다
METAPHOR = [
    "서 있는 바닥", "바닥에 서", "지도입니다", "학기 전체의 지도", "갈고리", "거울",
    "조각", "척추", "다리를 놓", "묻어가", "폐쇄계", "본체", "죽어도", "못 박",
    "심장", "뼈대", "밑거름", "발판", "물꼬", "씨앗", "열쇠", "관문", "무기",
]
# 과장·선언
HYPE = ["핵심", "좌우된다", "좌우하는", "필수적", "혁신", "패러다임", "~의 시대", "획기적"]
# 상투어
CLICHE = ["에 대해 알아보", "중요한 점은", "다양한 측면에서", "효과적으로 활용",
          "종합하면 이러한", "말할 수 있습니다"]
# 홍보 말투·구어
PROMO = ["한눈에", "손쉽게", "빠르고 정확하게", "해 보세요", "지금 바로", "하면 끝",
         "~해요", "~죠", "딱 "]

# 물리 동작에 빗댄 동사 — 추상적 작업에는 사전적 의미의 동사를 쓴다
PHYSICAL = [
    r"돌린|돌리[며다는고]|돌려[ ]?(보|주|야|서)", r"짚(는|어|고|을|었)", r"붙이(기|는|고)|붙인다",
    r"묶(었|는|어|고)", r"걷어", r"얹(는|어|고)", r"넘기|넘긴다", r"잡는다|틀을 잡",
    r"(?:^|(?<=[\s(]))재는|잰다", r"뺀다|빼는", r"가른다", r"민다|밀면서", r"살린다",
    r"몰린다", r"닿는다", r"띄워|띄운", r"열어 (보|둔|두)", r"꺼내(는|어|고)",
    r"올린다(?! ?\.)", r"내린다",
]

GROUPS = [("은유", METAPHOR), ("과장", HYPE), ("상투어", CLICHE), ("홍보·구어", PROMO)]


def check(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    problems, in_code, in_comment = [], False, False

    for i, ln in enumerate(lines, 1):
        if ln.startswith("```"):
            in_code = not in_code
            continue
        if ln.startswith("<!--"):
            in_comment = True
        if in_comment:
            if "-->" in ln:
                in_comment = False
            continue
        if in_code:
            continue

        is_title = ln.startswith("# ") or ln.startswith("## ")
        is_bullet = bool(re.match(r"^\s*- ", ln))
        is_note = ln.startswith("> ")

        if is_bullet or is_title or is_note:
            for label, words in GROUPS:
                for w in words:
                    if w in ln:
                        problems.append(f"{path}:{i} [{label}] '{w}' — {ln.strip()[:60]}")
            for pat in PHYSICAL:
                m = re.search(pat, ln)
                if m:
                    problems.append(
                        f"{path}:{i} [물리 동작] '{m.group(0)}' — {ln.strip()[:60]}")

        if is_bullet and re.search(r"다\.$|입니다\.?$|합니다\.?$|한다\.$", ln.strip()):
            problems.append(f"{path}:{i} [서술형 종결] 개조식으로 — {ln.strip()[:60]}")

        if (is_title or is_bullet) and re.search(r"(는가|인가|한가|을까|나요)\s*\??$", ln.strip()):
            problems.append(f"{path}:{i} [의문형] 답을 명사구로 — {ln.strip()[:60]}")

        if not in_code and "`" in ln:
            problems.append(f"{path}:{i} [백틱] 빌더가 처리하지 않음 — {ln.strip()[:60]}")

    # 슬라이드별 1단계 불릿 개수
    slide, count, title_line = None, 0, 0
    for i, ln in enumerate(lines + ["## __END__"], 1):
        if ln.startswith("## "):
            if slide and count > 4:
                problems.append(f"{path}:{title_line} [불릿 과다] 1단계 {count}개 (한도 4) — {slide}")
            slide, count, title_line = ln[3:].strip(), 0, i
        elif slide and re.match(r"^- ", ln):
            count += 1
    return problems


def main() -> int:
    # 지적 문구에 —, · 같은 글자가 들어간다. 콘솔 기본 인코딩이 cp949면 출력에서 죽는다.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    paths = [Path(a) for a in sys.argv[1:]]
    if not paths:
        print(__doc__); return 2
    all_problems = [p for path in paths for p in check(path)]
    for p in all_problems:
        print(p)
    print(f"\n{len(paths)}개 파일, 지적 {len(all_problems)}건")
    return 1 if all_problems else 0


if __name__ == "__main__":
    sys.exit(main())
