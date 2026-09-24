# Notes

Ghi chú tổng hợp từ video, blog, podcast, sách, short course — những nguồn **không phải khóa học có code** (→ `deeplearning-ai/`, `python-fundamentals/`) và **không phải paper** (→ `research/`).

## Cấu trúc

| Thư mục / file | Nội dung |
|---|---|
| `learning-methods/` | Cách học, tự học, năng suất |
| `career/` | Nghề developer, thị trường, AI & việc làm |
| `skills/` | Bộ kỹ năng cụ thể cần học cho một vai trò / lĩnh vực |
| `templates/` | Form mẫu cho từng loại nguồn: `video.md`, `article.md`, `book.md`, `short-course.md` |
| `reading_list.md` | Nhật ký mọi nguồn đã xem / đọc, mới nhất ở trên |

Thêm thư mục mới khi có ≥ 2 note cùng chủ đề chưa có chỗ.

## Quy ước

- Mỗi nguồn một file `.md`, tên kebab-case theo tiêu đề gốc: `how-to-become-dangerously-self-educated.md`
- Dùng template trong `templates/` (hoặc gọi `/note` để AI điền giúp)
- Hai mục **Bài học rút ra cho mình** và **Hành động** luôn tự viết — không để AI điền
- Mỗi note mới → thêm 1 dòng vào `reading_list.md`
- Skill `/note` nằm ở `.claude/skills/note/SKILL.md`

## Cách dùng skill `/note`

```
/note <link hoặc tiêu đề>
<dán summary / timestamps / transcript>
```

AI chọn template, điền form, tổng hợp key insights, cập nhật `reading_list.md`. Bạn đọc lại, viết 2 mục cá nhân, rồi tự commit.

AI không xem được video từ link — luôn dán kèm summary/timestamps, có transcript càng tốt.

## Quyền của AI trong thư mục này

AI được **tự tạo và sửa file trong `notes/`** (note mới, reading list, thư mục chủ đề mới) mà không cần hỏi, trừ hai mục cá nhân ở trên. Các thư mục khác trong repo vẫn theo quy tắc "chỉ hướng dẫn" trong `CLAUDE.md` gốc.
