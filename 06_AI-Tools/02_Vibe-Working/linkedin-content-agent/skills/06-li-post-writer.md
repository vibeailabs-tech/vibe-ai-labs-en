# Li Post Writer — Viết LinkedIn Text Post

Viết một LinkedIn text post hoàn chỉnh, sẵn sàng đăng.

## Cách dùng
```
/li-post-writer [topic or brief]
/li-post-writer mode=iterate [topic — will write 3 variants]
/li-post-writer mode=thread [topic — will write 3-post thread]
```

## Trước khi Viết

Kiểm tra Brand Voice Context để lấy:
- Đại từ voice (tôi / chúng tôi)
- Quy tắc tone (từ 01-tone.md)
- Từ vựng bị cấm (từ 05-glossary.json)
- Bài viết này phục vụ pillar nào (từ 03-pillars.md)
- Credibility anchors (từ 06-authority.md)
- Insight từ memory (từ post-history.json) — những hook nào đã hiệu quả trước đây?

---

## MODE: fresh (mặc định)

Viết một bài hoàn chỉnh theo cấu trúc sau:

### Dòng 1-2: HOOK (quan trọng nhất)
Hook phải:
- Dừng scroll trong vòng dưới 3 giây
- Cụ thể — bao gồm con số, tên người, khung thời gian, hoặc tuyên bố táo bạo
- Dưới 150 ký tự (ưu tiên mobile)
- KHÔNG bắt đầu bằng "Tôi muốn chia sẻ", "Hôm nay", "I'm excited to"

Các pattern hook mạnh (chọn một dựa trên chủ đề):
- **Contrarian**: "[Common belief] là sai. Đây là lý do..."
- **Specific number**: "Sau [X] [units], đây là điều tôi học được..."
- **Personal story**: "[Specific moment]. Tôi đã [did X]. Kết quả:"
- **Surprising stat/fact**: "[Specific number]% [something counterintuitive]."
- **Bold prediction/claim**: "[Direct claim that experts will react to]."

### Dòng 3: SEE-MORE CLIFF
Dòng này cực kỳ quan trọng — LinkedIn cắt nội dung tại đây trước khi hiển thị "see more".
Dòng này phải:
- Chưa hoàn chỉnh theo cách khiến người đọc muốn biết thêm (đặt vấn đề mà chưa có đáp án)
- Hoặc đưa ra một tuyên bố bất ngờ đòi hỏi giải thích
- Hoặc nêu một vấn đề cụ thể mà người đọc đang gặp ngay lúc này

### Body (từ dòng 4 đến hết phần nội dung chính):
- Tối đa 2 dòng mỗi đoạn
- Dòng trống giữa mỗi đoạn (khoảng trắng = dễ đọc)
- Mỗi đoạn phải truyền đạt một luận điểm rõ ràng — không độn thêm
- Dùng cấu trúc câu ưu tiên của brand voice
- Dùng từ vựng được ưu tiên; tránh từ bị cấm trong glossary
- Nếu dùng danh sách: dùng ▸ hoặc — làm bullet (không dùng -)
- Đa dạng độ dài câu để duy trì nhịp đọc
- Bao gồm ít nhất 1 chi tiết cụ thể (con số, tên, ví dụ, ngày tháng)

### Bài học/Insight (phần áp chót):
- Phần "vậy thì sao" — người đọc nên rút ra điều gì?
- Phải là insight không hiển nhiên, không phải câu sáo rỗng
- Giữ ở 1-2 dòng

### CTA (dòng cuối cùng):
- Đúng một lời kêu gọi hành động
- KHÔNG chung chung: "thoughts?" hoặc "share bên dưới"
- Cụ thể và nhắm đúng đối tượng:
  - "Bạn đã từng gặp vấn đề này chưa? Cách bạn xử lý là gì?"
  - "Bạn đồng ý với point nào nhất? Điều gì khác với kinh nghiệm của bạn?"
  - "Tag một founder đang gặp vấn đề này."
  - "Save bài này — bạn sẽ cần nó khi [specific situation]."

### Hướng dẫn độ dài bài:
- Điểm ngọt: 150-300 từ
- Tối đa: 400 từ (vượt quá mức này, engagement thường giảm)
- Tối thiểu: 80 từ (quá ngắn = dwell time thấp)

---

## MODE: iterate (A/B variants)

Viết 3 biến thể của cùng một bài, mỗi biến thể thử nghiệm một hook khác:

**Variant A — Hook contrarian**:
Mở đầu bằng tuyên bố thách thức điều đa số người tin.
Body và bài học là cùng nội dung cốt lõi, điều chỉnh nhẹ.

**Variant B — Hook số cụ thể**:
Mở đầu bằng insight được định lượng hoặc khung thời gian.
Cùng nội dung cốt lõi, điểm vào khác.

**Variant C — Hook câu chuyện cá nhân**:
Mở đầu bằng một khoảnh khắc hoặc tình huống cụ thể.
Cùng nội dung cốt lõi, kể theo dạng narrative.

Xuất từng biến thể đầy đủ, gán nhãn rõ ràng:
```
━━ VARIANT A (Contrarian) ━━
[full post text]

━━ VARIANT B (Number) ━━
[full post text]

━━ VARIANT C (Story) ━━
[full post text]
```

Thêm ghi chú 1 dòng về điều mỗi biến thể đang kiểm tra.
Đề xuất biến thể nào nên đăng trước dựa trên lịch sử hiệu suất (nếu có).

---

## MODE: thread

Viết một thread 3 bài về cùng chủ đề.

Quy tắc cho thread:
- Bài 1: hook mạnh nhất + insight cấp cao nhất (có giá trị khi đứng độc lập)
- Bài 2: đào sâu hơn vào một khía cạnh cụ thể (tham chiếu Bài 1)
- Bài 3: ứng dụng thực tế / các bước tiếp theo / CTA

Mỗi bài phải hoàn chỉnh và có giá trị khi đứng riêng (không phải ai cũng đọc hết cả thread).

---

## Metadata Bài viết (xuất sau mỗi bài)

```
📊 POST METADATA
Format: text post
Hook type: [contrarian/number/story/etc]
Pillar: [pillar name]
Voice: [tôi/chúng tôi]
Word count: [N]
Est. dwell time: [X-Y seconds]
Banned words check: [clean / [word found]]
```

---

## Tự kiểm tra Chất lượng Trước khi Xuất

Trước khi xuất, kiểm tra:
- [ ] Hook cụ thể và dừng được scroll
- [ ] Không đoạn nào dài hơn 2 dòng
- [ ] Có dòng trống giữa các đoạn
- [ ] Không có từ bị cấm (kiểm tra với glossary)
- [ ] CTA cụ thể, không chung chung
- [ ] Voice khớp với loại authority đã chọn
- [ ] Ít nhất một chi tiết cụ thể trong bài
