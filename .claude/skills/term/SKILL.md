---
name: term
description: Tra cứu một thuật ngữ (đặc biệt thuật ngữ AI/kỹ thuật) từ các nguồn uy tín trên web, tổng hợp thành note giải nghĩa chi tiết trong notes/glossary/. Dùng khi user gõ /term <thuật ngữ> hoặc nói "giải thích X là gì", "thuật ngữ X".
---

# Skill: /term

Biến một thuật ngữ thành note giải nghĩa có cấu trúc, dựa trên nghiên cứu từ nguồn uy tín trên web.

**Input từ user:** tên thuật ngữ (tiếng Anh hoặc Việt), ví dụ `/term AI harness`.
**Output:** một file `.md` trong `notes/glossary/` + một dòng mới trong `notes/glossary/README.md`.

## Các bước

### 1. Nghiên cứu

- `WebSearch` thuật ngữ. Ưu tiên nguồn uy tín: docs chính thức (Anthropic, OpenAI, Google, framework gốc...), paper/arxiv, blog kỹ thuật lớn (có tác giả/tổ chức rõ ràng). Tránh nguồn SEO, không rõ tác giả, hoặc chỉ diễn giải lại nguồn khác.
- Nếu thuật ngữ mơ hồ hoặc có nhiều nghĩa khác nhau (ví dụ tên riêng sản phẩm chưa rõ ràng, hoặc không tìm thấy nguồn đáng tin cậy nào) → nói rõ với user thay vì đoán, hỏi lại để làm rõ ngữ cảnh (ví dụ: lĩnh vực nào, liên quan sản phẩm/công ty nào).
- Lấy ít nhất 2 nguồn để đối chiếu trước khi kết luận. `WebFetch` các nguồn đã chọn để đọc chi tiết, không chỉ dựa vào snippet tìm kiếm.

### 2. Phân loại

- **Khái niệm phổ thông** (ví dụ: overfitting, API key): giải thích gọn, không cần mục "Cơ chế hoạt động" sâu.
- **Thuật ngữ kỹ thuật / chuyên ngành** (ví dụ: AI harness, agent loop, RAG, MCP): luôn viết đầy đủ toàn bộ mục trong template, đặc biệt "Cơ chế hoạt động" — giải thích nó vận hành như thế nào bên trong, không chỉ định nghĩa hời hợt.

### 3. Đặt tên file

kebab-case từ thuật ngữ gốc, tiếng Anh nếu thuật ngữ là tiếng Anh: `ai-harness.md`, `agent-loop.md`.

Nếu file đã tồn tại → hỏi user muốn ghi đè hay cập nhật bổ sung.

### 4. Điền template

Dùng cấu trúc ở cuối skill này.

- **Định nghĩa ngắn gọn**: 1-2 câu, đủ để hiểu ngay.
- **Giải thích chi tiết**: bối cảnh ra đời, vấn đề nó giải quyết.
- **Cơ chế hoạt động**: chỉ bỏ trống nếu là khái niệm phổ thông không có "cơ chế" để nói. Với thuật ngữ kỹ thuật, đây là mục quan trọng nhất — mô tả luồng xử lý / kiến trúc / các thành phần bên trong.
- **Ví dụ cụ thể**: ít nhất 1 ví dụ thực tế, không chung chung.
- **Ứng dụng thực tế**: thuật ngữ này dùng ở đâu, cho việc gì.
- **Thuật ngữ liên quan**: grep trong `notes/glossary/` xem có thuật ngữ nào liên quan, link tới đó. Không có thì ghi "Chưa có".
- **Nguồn tham khảo**: liệt kê link các nguồn đã dùng.

Không bịa thông tin — nếu một nguồn không đủ rõ về một mục nào đó, ghi rõ là chưa chắc chắn thay vì đoán.

### 5. Cập nhật `notes/glossary/README.md`

Thêm một dòng vào bảng, dòng mới nhất ở trên cùng. Nếu file chưa có, tạo mới với header:

```markdown
# Glossary

Tổng hợp thuật ngữ đã tra cứu qua skill `/term`.

| Ngày | Thuật ngữ | Loại | Note |
|---|---|---|---|
```

Cột `Note` là link tương đối, ví dụ `[note](ai-harness.md)`.

### 6. Báo cáo

Trả lời ngắn: đường dẫn file đã tạo, định nghĩa 1 câu, và nguồn chính đã dùng.

## Giới hạn

- Chỉ tạo/sửa file trong `notes/glossary/`. Không đụng phần khác của repo, không commit, không push.
- Không bịa nội dung khi không tìm được nguồn đáng tin cậy — báo lại cho user.
- Nếu thuật ngữ trùng tên với sản phẩm/công ty ít thông tin công khai, nói rõ mức độ chắc chắn thấp thay vì suy diễn.

## Cấu trúc template

```markdown
# <Thuật ngữ>

- **Loại:** Khái niệm chung / Kỹ thuật chuyên sâu
- **Ngày tạo:** YYYY-MM-DD
- **Chủ đề:** <tag1>, <tag2>

## Định nghĩa ngắn gọn

## Giải thích chi tiết
-

## Cơ chế hoạt động
-

## Ví dụ cụ thể
-

## Ứng dụng thực tế
-

## Thuật ngữ liên quan
- Chưa có

## Nguồn tham khảo
1.
```
