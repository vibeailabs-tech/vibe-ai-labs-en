# Contrast matrix (WCAG 2.1)

Tỷ lệ tương phản giữa màu chữ (hàng) và màu nền (cột). **AA text ≥ 4.5**, **AA large text / UI ≥ 3.0**. ✅ = đạt AA, 🔸 = chỉ dùng cho chữ lớn (≥ 24 px hoặc ≥ 19 px đậm) / thành phần UI, ❌ = không dùng làm chữ.

| Text \ Background | White | Cloud | Midnight | Electric Blue |
|---|---|---|---|---|
| Midnight | ✅ 18.81 | ✅ 17.98 | — | 🔸 3.86 |
| Ink | ✅ 17.74 | ✅ 16.96 | ❌ 1.06 | 🔸 3.64 |
| Slate | ✅ 4.97 | ✅ 4.75 | 🔸 3.78 | ❌ 1.02 |
| Electric Blue | ✅ 4.88 | ✅ 4.66 | 🔸 3.86 | — |
| Aqua | ❌ 1.80 | ❌ 1.72 | ✅ 10.44 | ❌ 2.70 |
| Violet Glow | 🔸 4.23 | 🔸 4.05 | 🔸 4.44 | ❌ 1.15 |
| White | — | ❌ 1.05 | ✅ 18.81 | ✅ 4.88 |
| Cloud | ❌ 1.05 | — | ✅ 17.98 | ✅ 4.66 |

## Quy tắc rút ra

- **Aqua #14D8C4 không dùng làm chữ trên nền sáng** (1.8:1). Aqua chỉ dùng làm màu nền/nhấn, hoặc làm chữ trên Midnight (≈ 10.4:1).
- **Electric Blue #2563FF** đạt AA cho chữ thường trên White/Cloud (≈ 4.9:1). Trên Midnight chỉ đạt cho chữ lớn / UI.
- **Violet Glow #8B5CF6** chỉ dùng cho chữ lớn hoặc tag; không dùng cho đoạn văn.
- Nút CTA: nền Electric Blue + chữ White (≈ 4.9:1) ✅.
- Chữ thân bài: Ink hoặc Midnight trên nền White/Cloud; White trên nền Midnight.
- Gradient chỉ dùng cho tiêu đề lớn, ruy-băng, nền và chuyển động; không đặt đoạn văn trực tiếp lên vùng gradient sáng.
