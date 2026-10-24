# 01 · Logos

## Chọn file nào?

| Nhu cầu | File |
|---|---|
| Nền sáng, mặc định | `vibe-ai-labs_horizontal_color.svg` / `stacked_color.svg` |
| Nền tối, mặc định | `…_reversed.svg` |
| Nền màu / ảnh tối bão hòa | `…_white.svg` (một màu) |
| In một màu, dấu, khắc | `…_black.svg` (Midnight, một màu) |
| Có tagline | thêm hậu tố `_tagline` |
| Avatar, app icon, favicon | thư mục `App_Icons_Avatars/`, `Favicon/` |
| Chỉ biểu tượng ruy-băng | `vibe-ai-labs_icon_*.svg` |

Cấu trúc tên file: `vibe-ai-labs_[bố-cục]_[biến-thể][_tagline][_kích-thước].ext`
Bố cục: `horizontal` · `stacked` · `icon` — Biến thể: `color` · `reversed` · `white` · `black`.

## Thư mục

- `SVG/` — vector, nền trong suốt (ưu tiên cho web, in, thiết kế).
- `PNG/` — nền trong suốt; bản 2000/2400 px (lớn) và 800/1000 px (web).
- `App_Icons_Avatars/` — app icon (Midnight/Cloud/Blue), avatar tròn/vuông.
- `Favicon/` — favicon.ico, SVG, PNG 16–512, safari-pinned-tab, webmanifest, snippet `<head>`.
- `Official_Master/` — artwork gốc do chủ thương hiệu cung cấp (PNG 1254×1254).

## Quy tắc ngắn

Vùng an toàn = 1 × đường kính chấm tròn · Tối thiểu: ngang 140 px, dọc 96 px, icon 24 px · Không kéo giãn, đổi màu, thêm bóng, dựng lại wordmark. Xem *Brand Guidelines* (mục 07–12).

## Lưu ý quan trọng về nguồn vector

Các file SVG được **dựng lại (trace) từ master PNG chính thức** để dùng trên mọi nền và mọi kích thước. Hình dạng, tỉ lệ và gradient bám sát bản gốc; tuy nhiên đây chưa phải file vector gốc của nhà thiết kế. Trước khi in ấn quy mô lớn (bảng hiệu, in offset) nên xin bản AI/PDF vector gốc, rồi thay thế file trùng tên.
