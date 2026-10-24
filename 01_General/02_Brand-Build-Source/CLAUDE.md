# Vibe AI Labs — ghi chú làm việc (CLAUDE.md)

> Lưu từ phiên làm việc 2026-10-16 để làm tiếp. Người dùng nói **tiếng Việt**, trả lời bằng tiếng Việt, ngắn gọn; không dùng popup hỏi (AskUserQuestion) — hỏi thẳng trong chat. Khi người dùng nói "ít chữ thôi" là yêu cầu thật: poster/văn bản phải rút gọn.

## 1. Dự án là gì

Xây dựng bộ nhận diện & tài liệu cho **Vibe AI Labs** — *AI-Powered Growth & Creative Agency* (VI: Agency tăng trưởng & sáng tạo ứng dụng AI), Marketing × AI × Creative, thị trường Việt Nam. Người phụ trách: **Henry Le** (Marketing Engineer · Founder). Brand line: **Ideas. Intelligence. Real Growth.**

## 2. Cấu trúc thư mục (`/Users/henryle/Desktop/VIBE AI LABS/01_General/02_Brand-Build-Source/`)

> Gốc dự án `VIBE AI LABS/` là git repo public `vibeailabs-tech/vibe-ai-labs` (xem `README.md` và `00_Folder-Map.png` ở gốc). Ngày 2026-10-24 đã sắp xếp lại thư mục và xoá bản trùng: **brandkit nguồn chuẩn giờ là `VIBE AI LABS/02_Brandkit/01_General-Brandkit/`**, Design Team Kit là `VIBE AI LABS/02_Brandkit/02_Designer-Kit/`. Các mục `brandkit/` và `Vibe_AI_Labs_Design_Team_Kit/` nhắc bên dưới chính là hai folder đó.

| Mục | Trạng thái |
|---|---|
| `Vibe AI Labs .docx` | Hồ sơ thương hiệu (34 mục, tiếng Việt). **Đã sửa một phần** — xem §4 |
| `Vibe AI Labs .docx.bak` | Bản gốc ban đầu (chưa sửa). Chưa xóa — hỏi người dùng |
| `02_Brandkit/01_General-Brandkit/` (trước là `brandkit/`) | **Brand Kit v2.0** hoàn chỉnh (430 file, ~82 MB). Nguồn chuẩn cho logo/màu/font/template |
| `02_Brandkit/02_Designer-Kit/` (trước là `Vibe_AI_Labs_Design_Team_Kit/`) | Kit riêng cho **team design làm poster**, dựa trên brandkit v2.0. Bản zip vẫn ở đây: `Vibe_AI_Labs_Design_Team_Kit.zip` |
| `posts/` | 2 poster Facebook 1080×1080 đã làm (xem §6) |
| `_tools/` | Script build (đã sao từ `/tmp` để không mất). Chạy `bash _tools/setup.sh` để khôi phục |
| `CLAUDE.md` | File này |

Bộ brandkit v1 cũ **đã xóa theo yêu cầu** (không còn bản sao).

## 3. Quyết định đã chốt (đừng đảo ngược khi chưa hỏi)

- **Thứ tự cố định**: Marketing → AI → Creative (Marketing × AI × Creative). Agency Introduction cũ viết "Marketing. Creative. AI." đã sửa.
- **Tên ba trụ**: *Marketing số* · *Trí tuệ nhân tạo (AI) & Tự động hóa* · *Thiết kế & Sáng tạo* (EN: Digital Marketing · AI & Automation · Design & Creative Studio). Màu trụ: Electric Blue `#2563FF` · Green `#16A34A` · Orange `#F97316`.
- **Phân cấp tagline**: Brand line "Ideas. Intelligence. Real Growth." (chính) · Descriptor "AI-Powered Growth & Creative Agency" · "Turn Brands into Growth" chỉ cho nội dung giáo dục/infographic. *(Tôi tự đề xuất — người dùng chưa xác nhận rõ.)*
- **Màu lõi**: Midnight `#0B1026`, Electric Blue `#2563FF`, Aqua `#14D8C4`, Violet Glow `#8B5CF6`, Cloud `#F8FAFC`; phụ: Ink `#111827`, Slate `#667085`, Line `#D9E2F2`. Aqua **không** làm chữ trên nền sáng.
- **Font**: Plus Jakarta Sans (tiêu đề) + Inter (thân/UI), file OFL đã kèm trong kit.
- **Logo chính thức** = ruy-băng gradient + chấm tròn + wordmark "Vibe **AI** Labs" (master PNG 1254×1254 nền tối: `brandkit/01_Logos/Official_Master/`). **Các SVG trong kit là bản dựng lại (trace) từ PNG**, mượt ở kích thước thường, hơi gợn khi phóng ≥ 4×, hai mũi nhọn hơi tròn. Cần xin file vector gốc của designer trước khi in lớn. Logo "sóng" cũ là legacy, đã bỏ.
- **Liên hệ chính thức**: email `vibeailabs@gmail.com` · website `https://vibe-ai-labs.vibeailabs.workers.dev` (tạm, chưa có tên miền) · WORC@Q2 Building, 21 Võ Trường Toản, An Khánh, TP.HCM · Facebook `facebook.com/vibe.ai.labs` · X `x.com/vibe_ai_labs`. **Hotline / Zalo / WhatsApp / LinkedIn / YouTube / TikTok / Threads: để trống** (người dùng bảo chừa) → không in lên template.
- **Poster**: một thông điệp, một CTA, headline ≤ 8 từ, tổng ≤ 30 từ (≤ 40 với danh sách), không emoji, logo trên-trái, gradient chỉ ở dòng tiêu đề cuối/ruy-băng/nền.
- Không dùng số liệu bịa trong nội dung đối ngoại: chỉ số liệu xác minh được (docx có câu này).

## 4. Tình trạng file docx

**Đã làm:** điền mọi ô `[Bổ sung]` (kèm dữ liệu **mẫu tự đặt**, xem dưới), thống nhất danh sách công nghệ (OpenAI, Claude, Gemini, Grok, DeepSeek, n8n, Hermes Agent, Make, Zapier, API), email mục 6 = "Email: vibeailabs@gmail.com", mục 18 → Heading 1, **xóa mục 35**, website + link dự án (`/du-an`) + đặt lịch (`/lien-he`) dùng địa chỉ workers.dev, "Thành viên cộng đồng: **100.000+**" (số thật do người dùng cung cấp).

**Còn trống (15 chỗ):** Hotline, Zalo, WhatsApp (mục 6, 33, 34, 15), LinkedIn công ty (mục 7, 33), YouTube, TikTok, Threads (mục 7), LinkedIn + WhatsApp nhà sáng lập (mục 15), "Email doanh nghiệp" (mục 34), **mục 14 "Bộ nhận diện thương hiệu"** (ghi chú giữ chỗ).

**Dữ liệu mẫu do tôi tự đặt trong docx — phải thay bằng thật trước khi dùng ngoài:** giờ làm việc (T2–T6 09:00–18:00), giá tối thiểu 10 triệu VNĐ, tạm ứng 50%/50%, báo giá hiệu lực 30 ngày, hỗ trợ sau bàn giao 30 ngày & phản hồi 24 giờ, giới thiệu Henry Le (mục 15), đội ngũ/cộng tác viên (mục 16), 1 case study mẫu ẩn tên (mục 24), 2 nhận xét khách hàng hư cấu (Nguyễn Thị Lan – Sắc Việt; Trần Quốc Bảo – Bếp Nhà Foods), số liệu mục 28 (35+ khách hàng, 60+ dự án = 28 Marketing + 14 AI + 18 Sáng tạo, 8 ngành, 4 nhóm cộng đồng), đối tác/khách hàng mô tả chung.

**Chưa đồng bộ với brandkit (việc cần làm):**
1. Điền **mục 14** từ brandkit (logo, màu, font, họa tiết, giọng điệu, quy tắc dùng).
2. Thêm vào docx: tagline "Ideas. Intelligence. Real Growth.", descriptor, lời hứa thương hiệu, phương pháp *Audit → Build → Automate → Grow*.
3. **3 infographic trong docx** (Marketing số / AI & Tự động hóa / Thiết kế & Sáng tạo) vẫn dùng logo cũ + tagline "Turn Brands into Growth" + màu pastel — cần làm lại bằng logo mới (sẽ khác phong cách 3D gốc, báo người dùng).

Cách sửa docx: giải nén (zip) → sửa `word/document.xml` bằng script Python (regex theo đoạn `<w:p>`), zip lại giữ nguyên các part; luôn kiểm tra bằng `python-docx`. Backup trước khi sửa.

## 5. Brandkit v2.0 — những gì có (`brandkit/`)

`00_README` (README, CHANGELOG, manifest) · `01_Logos` (SVG/PNG stacked·horizontal·icon × color·reversed·white·black ± tagline, App_Icons_Avatars, Favicon, Official_Master) · `02_Color` (palette, CSV/JSON/.ase/.gpl, contrast-matrix, gradients.css) · `03_Typography` (fonts OFL, type-scale, specimen, fonts.css) · `04_Graphic_Elements` (nền ruy-băng/sóng dark+light × 3 tỉ lệ, orb, dot-grid) · `05_Icons` (26 icon + Pillar_Tiles + sheet) · `06_Templates` (Social 11 định dạng × dark/light + 4 mẫu nội dung; Presentation PPTX 9 layout; Stationery: danh thiếp bleed 3mm, letterhead, proposal, chữ ký email; Documents DOCX; Digital: virtual background) · `07_Messaging` (5 file md) · `08_PDF` (Brand Guidelines 34 trang VN, Quick Reference, Logo Usage Sheet, Agency Introduction 9 trang, Business Card/Letterhead/Proposal Cover) · `09_Brand_Tokens` (JSON, CSS, Tailwind, W3C).

**Còn thiếu / hạn chế đã báo người dùng:** logo vector là trace; chưa Pantone/EPS/PDF-vector logo; chưa mở thử PPTX/DOCX trong Office hay SVG trong Figma/Illustrator; chưa có ảnh mockup thật, ảnh chụp, file animation, thư viện Figma; tiếng Việt do tôi viết chưa có người bản ngữ rà; số điện thoại/Zalo/LinkedIn chưa in; ô số liệu trong template là placeholder (+00%).

## 6. Design Team Kit & poster đã làm

`Vibe_AI_Labs_Design_Team_Kit/`: `00_START_HERE` (README, **Poster_Playbook.pdf** 16 trang, **Poster_Cheat_Sheet.pdf**, manifest) · `01_Logos` · `02_Color_Fonts` · `03_Poster_Templates` (**6 layout R1–R6** Announcement/Insight list/Pillars/Stat/Quote/Event × 4 tỉ lệ 1x1·4x5·9x16·16x9 × dark/light = 48 SVG+PNG; `Print_A3` R1/R3/R6 PDF (chưa bleed); `Guides` lớp vùng an toàn) · `04_Components` · `05_Backgrounds` · `06_Icons` · `07_Copy_Library` · `08_Export_Handoff` (export-specs, qa-checklist, brief) · `09_Reference`.

`posts/` (Facebook 1080×1080, mỗi bản có `_dark` + `_light`, PNG + SVG):
- `facebook-poster_marketing-ai-creative_…` — "Ba năng lực. Một hệ thống." + 3 thẻ Marketing/AI/Creative + CTA "Nhắn tin cho chúng tôi". Người dùng đã duyệt bản **ít chữ**.
- `facebook-poster_rui-ro-khi-dung-ai_…` — "4 rủi ro khi dùng AI thiếu kiểm soát." (Thông tin sai · Lộ dữ liệu · Nội dung na ná · Mất kiểm soát) + "AI hỗ trợ. Con người quyết định." — yêu cầu gốc là "tác hại của AI"; tôi đổi góc sang "rủi ro khi thiếu kiểm soát" cho khớp thương hiệu. **Chưa nhận phản hồi của người dùng.**

## 7. Công cụ & lưu ý kỹ thuật (đã trả giá bằng thời gian)

- Máy **không có** pdftoppm / ImageMagick / node / inkscape. Có **Google Chrome** (headless để render SVG→PNG, HTML→PDF), **Swift/PDFKit** (xem PDF thành ảnh: `swift _tools/pdf_to_png.swift file.pdf outdir`), `python3 -m venv` + pip hoạt động.
- Script build đặt ở `/tmp/brandbuild` & `/tmp/dk` (hardcode `/tmp/...`); `/tmp` có thể mất → **chạy `bash _tools/setup.sh` trước**. Thư mục output tạm: `/tmp/kit_out` (brandkit), `/tmp/design_out` (design kit). `render.py` render PNG bằng Chrome.
- **BUG đã sửa**: Chrome headless cắt đáy ảnh khi cửa sổ nhỏ (`--window-size` bị trừ ~87px chrome UI, nhất là chiều rộng < ~500px). `render.py` hiện render cửa sổ lớn hơn rồi **crop** về đúng kích thước. Đã render lại 118 PNG nhỏ trong brandkit. Nếu viết hàm render mới → dùng `render.svg_to_png`, đừng gọi Chrome trực tiếp.
- **Lệch giữa `/tmp/kit_out` và `brandkit/` (live)**: live đã được vá thêm (a) thêm `width`/`height` cho 100 SVG (danh thiếp/thư tính theo mm), (b) render lại PNG nhỏ. **Live là nguồn chuẩn** — sửa trực tiếp trong `brandkit/`; nếu build lại từ script thì phải áp lại các vá này (hoặc rsync có chọn lọc).
- Logo vector sinh từ `_tools/brandbuild/logo_paths.json` (kết quả trace: 4 vùng ruy-băng với gradient tuyến tính tách theo mặt + chấm tròn + chữ). `logo.py` dựng các biến thể; `trace_logo.py` + `smoothpath.py` + `trace_data/*.npy` để trace lại nếu cần. Wordmark "AI": đa giác sạch (không phải curve trace).
- Template poster: `_tools/dk/recipes.py` (engine layout R1–R6), `build_templates.py`, `build_components.py`, `build_playbook.py`, `build_cheat.py`, `poster_risk.py`. Poster lẻ: viết script ngắn dùng `recipes` helper (`scaffold`, `gradient`, `pill`, `card`).
- Lỗi hay gặp khi viết HTML bằng f-string/`%`: ký tự `%` trần trong chuỗi dùng toán tử `%` → phải viết `%%`.
- Các PDF guidelines dùng `zoom` CSS trên `.pad`; trang dài tràn footer → giảm cỡ ảnh/bảng.
- Thông tin trong template luôn lấy từ `cfg.py` (WEBSITE, EMAIL, FOUNDER…) — đổi một chỗ khi có tên miền/hotline.

## 8. Việc làm tiếp (gợi ý theo ưu tiên)

1. **Đồng bộ docx** (mục 14 + tagline/descriptor/promise/phương pháp) — xin xác nhận phân cấp tagline trước.
2. Làm lại **3 infographic** trong docx bằng logo mới (cần chốt phong cách).
3. Xin người dùng: file vector logo gốc (AI/SVG/PDF); hotline, Zalo, LinkedIn…; tên miền; số liệu/khách hàng/nhận xét thật; xác nhận giới thiệu Henry Le; có xóa `.docx.bak` không.
4. Mở thử PPTX/DOCX/SVG trong Office/Figma/Illustrator, báo lỗi → sửa.
5. Lấy phản hồi poster "rủi ro khi dùng AI"; làm thêm poster khác từ `recipes.py` (bài viết 3 câu hỏi bắt đầu AI; Story 9:16; A3).
6. (Tùy chọn) Bleed 3 mm cho `Print_A3`; Pantone; mockup thực tế; bản tiếng Anh của Brand Guidelines.
