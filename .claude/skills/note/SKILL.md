---
name: note
description: Tạo note tổng hợp từ video / bài viết / sách / short course theo template trong notes/templates, tổng hợp key insights, cập nhật notes/reading_list.md. Dùng khi user gõ /note hoặc nói "ghi chú lại video/bài này", "tạo note cho...".
---

# Skill: /note

Biến nguồn thông tin (video, blog, sách, short course) thành một file note có cấu trúc trong `notes/`.

**Input từ user:** link hoặc tiêu đề + tóm tắt / timestamps / transcript dán kèm.
**Output:** một file `.md` trong `notes/<chủ-đề>/` + một dòng mới trong `notes/reading_list.md`.

## Các bước

### 1. Phân loại nguồn → chọn template

| Nguồn | Template |
|---|---|
| YouTube, podcast, talk | `notes/templates/video.md` |
| Blog, bài viết, newsletter | `notes/templates/article.md` |
| Sách (theo chương) | `notes/templates/book.md` |
| Short course, workshop, bài giảng lẻ không có code | `notes/templates/short-course.md` |

Đọc template tương ứng. Nếu file template rỗng, dùng **cấu trúc dự phòng** ở cuối skill này và nhắc user điền template.

### 2. Chọn thư mục chủ đề

- Đọc `notes/README.md` để biết các thư mục hiện có (ví dụ `learning-methods/`, `career/`).
- Một note có thể thuộc nhiều tag, nhưng chỉ nằm ở **một** thư mục — chọn chủ đề chính.
- Không khớp thư mục nào → đề xuất tên mới (kebab-case) và **hỏi user** trước khi tạo.

### 3. Đặt tên file

kebab-case từ tiêu đề gốc, tiếng Anh, không dấu, bỏ từ thừa (a, the, complete, ...).
Ví dụ: *How to Become Dangerously Self Educated (Complete Plan for A Developer)* → `how-to-become-dangerously-self-educated.md`.

Nếu file đã tồn tại → hỏi user muốn ghi đè hay bổ sung.

### 4. Điền template

- **Metadata**: điền đủ. Ngày xem = hôm nay nếu user không nói. Đánh giá sao để trống nếu user chưa cho.
- **Tóm tắt 1 dòng**: một câu, nói được luận điểm trung tâm.
- **Nội dung chính**: bám theo timestamps / chương / heading user cung cấp. Mỗi mục 2–4 gạch đầu dòng. Viết tiếng Việt, giữ nguyên thuật ngữ tiếng Anh.
- **Key insights**: 3–5 ý, diễn đạt lại bằng lời khác, **không chép lại** summary gốc. Ưu tiên ý có thể áp dụng được.
- **Câu hỏi mở / điểm chưa đồng ý**: ít nhất 1 — chỗ tác giả khẳng định mà không có bằng chứng, hoặc điểm mâu thuẫn với note khác.
- **Liên hệ với note khác**: grep trong `notes/` theo tag/chủ đề; nếu có note liên quan, ghi đường dẫn tương đối và 1 câu vì sao liên quan. Không có thì ghi "Chưa có".
- **Bài học rút ra cho mình** và **Hành động**: **ĐỂ TRỐNG**, giữ nguyên comment hướng dẫn trong template. Đây là phần user tự viết.

### 5. Cập nhật `notes/reading_list.md`

Thêm một dòng vào bảng, **dòng mới nhất ở trên cùng**. Nếu file chưa có bảng, tạo header:

```markdown
| Ngày | Tiêu đề | Loại | Nguồn | Chủ đề | Note |
|---|---|---|---|---|---|
```

Cột `Note` là link tương đối tới file vừa tạo, ví dụ `[notes](learning-methods/how-to-become-dangerously-self-educated.md)`.

### 6. Báo cáo

Trả lời ngắn: đường dẫn file đã tạo, thư mục đã chọn và vì sao, 3 key insights. Nhắc user viết 2 mục cá nhân rồi tự commit.

## Giới hạn

- **Không xem được video / không fetch được trang** nếu chỉ có link. Khi user chỉ đưa link → yêu cầu dán summary, timestamps hoặc transcript. Không bịa nội dung.
- Chỉ dùng thông tin user cung cấp. Ý nào là suy luận của AI (không có trong input) thì đánh dấu *(suy luận)*.
- Chỉ tạo/sửa file trong `notes/`. Không đụng README gốc, không commit, không push.
- Nếu note cần thư mục mới → hỏi trước, không tự tạo.

## Cấu trúc dự phòng (khi template rỗng)

```markdown
# <Tiêu đề>

- **Loại:** Video | Article | Book | Short course
- **Nguồn:** <kênh / tác giả>
- **Link:** <url>
- **Ngày xem:** YYYY-MM-DD
- **Chủ đề:** <tag1>, <tag2>
- **Đánh giá:** ⭐⭐⭐☆☆
- **Đáng xem lại:** Có / Không

## Tóm tắt 1 dòng

## Nội dung chính
### <Mục 1> (mm:ss hoặc Chương 1)
-

## Key insights
1.

## Câu hỏi mở / điểm chưa đồng ý
-

## Liên hệ với note khác
- Chưa có

## Bài học rút ra cho mình
<!-- TỰ VIẾT: nó thay đổi gì trong cách mình học / làm? -->

## Hành động
- [ ]
```
