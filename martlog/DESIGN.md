# MartLog landing — local refinement

## 1. Atmosphere & Identity
Clear, approachable, useful. Primary direction: minimalist product-led, Decide/Learn surface for Korean Instagram visitors deciding whether to install. User selected retaining the purple brand, real app UI, stronger copy and install buttons. Scope is MartLog landing only, not a shared site redesign. Signature is the actual receipt-derived item history screen, not invented chart art. Existing feature claims only; no savings, review or user-count claims.

## 2. Color
Page #FFFFFF; product stage #F5F2FC; supporting surface #FAF9FC; ink #242032; muted #645F72; brand #7869E6 (from existing app-icon direction); accessible accent #5846B3; border #E5E0EE. Mostly white, one lavender stage, purple reserved for emphasis. Text contrast AA. No gradients or blur.

## 3. Typography
'Apple SD Gothic Neo', 'Malgun Gothic', -apple-system, BlinkMacSystemFont, sans-serif. Korean-native, zero font network dependency. Display 56px desktop / 36px mobile, line-height 1.22, weight 750. Section 32/28px, step 20px; body 18/16px, captions 14px floor. Korean keep-all + overflow-wrap for long strings. No justified or truncated copy.

## 4. Spacing & Layout
4px unit; 8/12/16/20/24/32/40/48/64/80 scale. Container 1080px, desktop gutters 40px, mobile 20px. Hero desktop text/screenshot columns; mobile copy + store buttons first then actual UI. Product screenshot displayed at legible width, bounded full width with intrinsic dimensions. Usage explanation is a vertical sequence, not equal feature cards. Native document scroll; no nested scroll. Breakpoints 960/600px. Check 1440, 768, 375 and 320px. Legal/support links consolidated in footer.

## 5. Components
Brand link (icon + wordmark), text navigation, existing two store-button links with exactly App Store / Google Play labels, actual product figure and caption, ordered usage steps, legal footer. Link states: default/hover underline or surface change, active visual feedback, visible 3px focus outline. Minimum 44px targets. No disabled/loading/empty/error UI: static document with native links, no forms, no client API or hidden content. Image fallback is descriptive alt text. No additional tracking script: public main has none, original uncommitted attribution work remains untouched; retain data-store hooks for later integration.

## 6. Motion & Interaction
No autoplay, no carousel, no animation, no sticky overlay. Simple color feedback only. Reduced motion does not change functionality. Downloads are always standard anchors, available without JS. In-page usage and download links use native anchors.

## 7. Depth & Surface
One lavender product stage and subtle screenshot shadow. Flat typography-led supporting section. No decorative icons, floating stats, invented phone widgets or background blobs.

## 8. Accessibility, Performance & Evidence
One h1, semantic main/nav/footer, skip link, meaningful image alt, visible sample-data caption. Decorative store SVGs hidden from accessibility tree. No CJK body under 14px. Keyboard and 200% zoom/reflow checks required.
Budget before edit: cold anonymous local /martlog/, mobile viewport 375x812, Chromium desktop emulating mobile dimensions with Fast 4G (1.6Mbps down/750Kbps up, 150ms RTT) and 4x CPU slowdown: LCP <2.5s and CLS <0.1 as lab diagnostic only. Capture baseline before modification under same profile. Added image should be WebP with fixed dimensions, no third-party runtime/font resources. No field p75 or real-user speed claims.

Evidence retained transiently outside repo/Operations. Final screenshots after final code at 1440/768/375. Tests must preserve store destinations, legal routes, visible sample disclosure, JS-free links and local asset availability. No push, PR, merge or deployment authorized in this pass.

## Asset provenance
`assets/item-history.webp` is a resized/re-encoded real sample-data UI from Marketing/runs/2026-W35/martlog-comic-01/assets/martlog-item-sample-ui.png; that package's qa.md traces it to MartLog `_raw/04_item.png`. No personal receipts or customer data.
