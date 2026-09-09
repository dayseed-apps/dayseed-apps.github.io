# 또또 landing

## Direction
Product-led Decide/Learn surface matching the approved MartLog composition.
Keep the existing 또또 landing's pink identity; do not recolor the real app screenshot.
One question-led hero, actual product image, two install links, then a short usage flow.
No feature-card grid, invented metrics, testimonials, scripts, or tracking changes.

## Visual system
- Page #ffffff; product stage #fff2f6; secondary surface #fffafb.
- Ink #27232a; muted #6f6873; accent #a62c53; border #eee0e6.
- Existing brand pink #ff6f91 is decorative; darker accent used for readable text.
- Korean-first Apple SD Gothic Neo / Malgun Gothic typography, no external font fetches.
- Desktop 1080px content width; split hero; mobile single column.
- 56/44/36px hero heading; 18/16px intro; 44px minimum link targets.
- Same spacing, focus, download controls and static CSS posture as MartLog.

## Content and asset provenance
- Question: 마지막 수유, 몇 시였지? (Marketing/runs/2026-W39/scenario.md).
- Existing 또또 landing supports recording, invited-family sharing, growth and vaccinations.
- Image: Flutter/ReleaseClones/ddoddo-1.0.3/tools/screenshots/ko/_raw/01_home.png.
- This is the actual app screenshot harness, not a reconstructed interface.
- main_screenshot.dart explicitly seeds sample baby 서윤 and enables isDemoMode.
- Resize and WebP encode only; no UI, names, times or records repainted.
- Visible caption states 실제 앱 화면 · 샘플 데이터; UI may differ by version.
- Retain existing medical-information disclaimer and all four support/policy routes.
- Store URLs preserved exactly. No claims about feeding intervals or medical outcomes.

## Delivery scope
Only ddoddo/index.html, this document, assets/record-timeline.webp and its regression test.
Separate worktree based on latest fetched main; local preview only pending approval.
