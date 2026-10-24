# Quy cách xuất file & bàn giao

## Kích thước & định dạng

| Kênh | Kích thước thiết kế | Xuất | Ghi chú |
|---|---|---|---|
| Facebook post vuông | 1080 × 1080 | PNG, **2160 × 2160** (2×) | Tỉ lệ 1:1 an toàn nhất |
| Facebook / Instagram dọc | 1080 × 1350 | PNG 2160 × 2700 | 4:5 chiếm nhiều chỗ nhất trên feed |
| Story / Reels / TikTok | 1080 × 1920 | PNG/JPG 1080 × 1920 | Chừa 250 px trên, 340 px dưới |
| Ngang 16:9 (X, YouTube thumbnail, bìa link) | 1280 × 720 (hoặc 1600 × 900) | PNG/JPG | Chữ lớn hơn 10% so với bản vuông |
| LinkedIn post | 1200 × 1200 | PNG 2400 × 2400 | |
| Poster in A3 | 297 × 420 mm | **PDF** (+ bleed 3 mm) | Font nhúng/outline; CMYK theo nhà in |
| Poster in A2/A1 | tỉ lệ 1 : 1,414 | PDF vector | Dùng file SVG/PDF, không phóng PNG |

## Thiết lập chung

- **Hệ màu:** sRGB (digital). In: nhận profile từ nhà in; không tự chuyển CMYK khi chưa proof.
- **Định dạng:** PNG cho poster có chữ/đồ họa phẳng; JPG chất lượng 88–92 khi poster có ảnh chụp; không dùng JPG cho chữ nhỏ trên nền gradient (dễ vỡ).
- **Dung lượng:** ≤ 5 MB mỗi ảnh để tránh bị nén mạnh; nếu lớn hơn → giảm xuống 1,5× hoặc xuất JPG 90.
- **Font:** Plus Jakarta Sans + Inter (có trong `02_Color_Fonts/fonts`). Không thay font. SVG mở mà font lạ = chưa cài font.
- **Logo:** dùng file trong `01_Logos`, không vẽ lại.
- **Tên file:** `vibe-ai-labs_[kênh]_[chủ-đề]_[tỉ-lệ]_[tone]_v[số].png` — ví dụ `vibe-ai-labs_facebook_ba-nang-luc_1x1_dark_v01.png`.

## Bàn giao

1. File xuất (PNG/JPG/PDF) + file nguồn (SVG hoặc file Figma/AI/PSD).
2. Một ảnh xem trước nhỏ (≤ 1 MB) để duyệt nhanh.
3. Caption đề xuất (nếu poster đi kèm bài đăng) — chữ dài để ở caption, không đưa lên poster.
4. Ghi chú nguồn: ảnh stock/AI (tên công cụ, ngày), font, số liệu (nguồn + kỳ đo).

## Thư mục lưu trữ gợi ý

```
Posters/
  2026-10/
    ba-nang-luc/
      source/   (SVG / Figma / AI)
      export/   (PNG, JPG)
      preview.jpg
      caption.md
```
