# Li Visual Brief — Định hướng hình ảnh cho Designer hoặc AI Tool

Tạo visual brief chi tiết cho hình ảnh, bìa PDF hoặc thumbnail đi kèm bài đăng. Hình ảnh mạnh giúp tăng click-through và dừng scroll trước khi người đọc kịp đọc dòng chữ đầu tiên.

## Khi nào cần tạo Visual Brief

- Bài đăng ảnh đơn → luôn luôn (ảnh là thứ người đọc nhìn thấy đầu tiên)
- Carousel PDF → thiết kế slide bìa + style guide tổng thể
- Article → thumbnail
- Newsletter → ảnh header (không bắt buộc nhưng tăng tính chuyên nghiệp)
- Bài text → không bắt buộc; bài chỉ text vẫn có thể hiệu quả mà không cần ảnh

---

## LinkedIn Image Specs

| Use case | Ratio | Dimensions |
|----------|-------|-----------|
| Single image post (vuông) | 1:1 | 1080 × 1080 px |
| Single image post (ngang) | 1.91:1 | 1200 × 628 px |
| Single image post (dọc) | 4:5 | 1080 × 1350 px |
| Carousel PDF slides | 1:1 hoặc 4:5 | 1080×1080 hoặc 1080×1350 |
| Article thumbnail | 1.91:1 | 1200 × 628 px |

Khuyến nghị cho bài feed: **4:5 portrait (1080×1350)** — chiếm nhiều diện tích nhất trên feed mobile, dừng scroll hiệu quả nhất.

---

## Các thành phần của Brief

### 1. Format & Dimensions
Ghi rõ use case và kích thước cụ thể.

### 2. Visual Concept
Mô tả hình ảnh cần thể hiện — đủ cụ thể để designer hoặc AI image tool có thể thực thi.

- XẤU: "Hình ảnh chuyên nghiệp về năng suất làm việc"
- TỐT: "Ảnh đôi: bên trái là bảng trắng lộn xộn đầy sticky note; bên phải là cùng bảng đó chỉ còn 3 mục gọn gàng. Ẩn dụ cho việc ưu tiên hóa."

Với bìa carousel: mô tả metaphor hình ảnh hoặc hướng thiết kế đồ họa cho headline.

### 3. Text Overlay
Những chữ nào (nếu có) sẽ xuất hiện trên ảnh?
- Headline (chính xác từng chữ)
- Subtext hoặc byline
- Tên thương hiệu / handle

Ghi rõ: thứ bậc kích thước chữ (headline lớn / subtext vừa / attribution nhỏ)

### 4. Color Direction
Nếu brand colors đã được định nghĩa trong brand voice files, dùng luôn.
Nếu chưa, gợi ý theo chủ đề và cảm xúc:
- Tin tưởng/chuyên môn: xanh đậm, navy, charcoal
- Năng lượng/hành động: cam, tông ấm
- Sạch/tối giản: nền trắng, một màu accent duy nhất
- Cao cấp: nền tối, chữ vàng hoặc trắng

### 5. Typography Style
- Bold geometric sans-serif (hiện đại, startup)
- Clean humanist sans-serif (gần gũi, chuyên nghiệp)
- Editorial serif (uy quyền, thought leadership)
- Mixed (headline serif + body sans-serif)

### 6. Mood & Style
Chọn một phong cách chính:
- **Minimal text on solid color** — tương phản cao, dễ làm, phù hợp hầu hết bài đăng
- **Photography + text overlay** — cần ảnh đẹp; tốt cho bài kể chuyện
- **Data visualization** — biểu đồ, đồ thị; tốt cho bài dữ liệu
- **Illustration / iconography** — tốt cho bài framework hoặc quy trình
- **Typographic poster** — câu quote hoặc hook trở thành toàn bộ hình ảnh

### 7. Những gì cần tránh
Các cliché hình ảnh phổ biến của chủ đề này khiến ảnh trông generic:
- (Liệt kê 2-3 trope hình ảnh cụ thể cần tránh cho loại nội dung này)

---

## AI Image Tool Prompt (Bonus)

Nếu người dùng muốn dùng Midjourney, DALL-E hoặc tương tự:
Tạo phiên bản prompt từ brief, định dạng phù hợp cho AI image generation.

---

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎨 VISUAL BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Use case: [single image / carousel cover / article thumbnail]
Dimensions: [W × H px] | Ratio: [ratio]

VISUAL CONCEPT:
[2-4 câu mô tả chính xác những gì cần thể hiện]

TEXT OVERLAY:
  Headline: "[exact text]"
  Subtext: "[nếu có]"
  Attribution: "[tên/handle — nhỏ, góc dưới]"

COLORS:
  Background: [màu / hex]
  Primary text: [màu / hex]
  Accent: [màu / hex]

TYPOGRAPHY: [mô tả style]

MOOD: [lựa chọn style + mô tả 2 chữ]

AVOID: [2-3 visual cliché cần bỏ qua]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 AI IMAGE PROMPT (Midjourney / DALL-E):
"[AI-ready image generation prompt]"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
