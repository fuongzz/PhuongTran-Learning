# Python for AI Engineer — Giáo trình rút gọn

> Đây không phải khóa học Python. Đây là **tập con Python tối thiểu** để build được RAG và agent, thiết kế để đi từ `hello.py` đến một RAG chạy được trong thời gian ngắn nhất.
>
> Nguyên tắc: **mỗi module đều kết thúc bằng code chạy được của cùng một project.** Không học kiến thức rời.

- **Ngày lập:** 2026-09-23
- **Mục tiêu:** Đủ Python để build & thử nghiệm, không phải để thi
- **Nguồn nền:** CS50P (chỉ các tuần được chỉ định) + doc chính thức
- **Liên quan:** [ai-engineer-essential-skills.md](ai-engineer-essential-skills.md) — Tier 1

---

## Project xuyên suốt: `ask-my-docs`

Một CLI hỏi đáp trên tài liệu của chính bạn. Mỗi module thêm một lớp:

```
M1 → đọc được file, in ra màn hình
M2 → cắt thành chunk, đếm, lọc
M3 → gọi được API model, nhận câu trả lời
M4 → xử lý lỗi, retry, không crash giữa chừng
M5 → embed + search, trả lời có grounding   ← RAG hoàn chỉnh
M6 → đóng gói thành CLI người khác chạy được
```

Kết thúc M5 là bạn **đã có một RAG do chính mình viết** — không phải notebook điền chỗ trống.

---

## Module 1 — Đủ để đọc và chạy code

**Mục tiêu:** đọc hiểu bất kỳ đoạn Python nào gặp trong code AI mà không hoảng.

**Nguồn:** CS50P tuần 0–2 (Functions/Variables, Conditionals, Loops) — *xem nhanh, không làm hết problem set*

**Nội dung cần:**
- `list`, `dict`, `tuple`, `set` — phân biệt khi nào dùng cái nào
- `dict` là quan trọng nhất: mọi response API đều là dict
- f-string: `f"Trả lời: {answer}"` — prompt là string, bạn sẽ ghép string suốt ngày
- `for`, `if`, `while`, truy cập lồng nhau: `data["choices"][0]["message"]["content"]`
- `def`, tham số mặc định, `return`

**Đạt khi tự làm được (không nhìn mẫu):**
- [ ] Cho một dict JSON lồng 3 tầng, lấy ra đúng giá trị ở tầng trong cùng
- [ ] Giải thích được vì sao `list` không dùng làm key của `dict`
- [ ] Viết hàm nhận list string, trả về list đã lọc bỏ chuỗi rỗng

**Bài build:** đọc một file `.txt`, in ra số dòng và số từ.

**Câu hỏi mình sẽ hỏi bạn:**
> `data.get("key")` khác `data["key"]` chỗ nào, và vì sao code gọi API gần như luôn dùng cái đầu?

---

## Module 2 — Xử lý dữ liệu

**Mục tiêu:** biến tài liệu thô thành thứ nhét được vào model.

**Nguồn:** CS50P tuần 6 (File I/O) + tuần 9 phần comprehension / unpacking

**Nội dung cần:**
- `with open(...) as f:` — context manager, vì sao phải dùng `with`
- `pathlib.Path` thay cho ghép string đường dẫn (quan trọng trên Windows)
- List comprehension: `[c for c in chunks if len(c) > 50]`
- Dict comprehension
- `json.loads` / `json.dumps` — **dùng liên tục**, mọi API đều nói chuyện bằng JSON
- Slicing: `text[i:i+500]` — đây chính là chunking

**Đạt khi tự làm được:**
- [ ] Viết `chunk_text(text, size, overlap)` trả về list các đoạn có chồng lấn
- [ ] Giải thích vì sao chunk cần overlap
- [ ] Đọc 1 file JSON, sửa 1 field, ghi lại ra file mới
- [ ] Viết lại một vòng `for` thành comprehension và ngược lại

**Bài build:** `ask-my-docs` đọc cả thư mục `.txt`, cắt thành chunk, lưu ra `chunks.json`.

**Câu hỏi mình sẽ hỏi bạn:**
> Chunk 500 ký tự và chunk 500 token khác nhau thế nào? Cái nào là thứ model thật sự quan tâm?

---

## Module 3 — Gọi API

**Mục tiêu:** đây là kỹ năng trung tâm. Video nói *"every AI product is fundamentally well-structured API calls."*

**Nguồn:** **không phải CS50** — đọc doc chính thức của thư viện bạn dùng

**Nội dung cần:**
- `pip`, virtual environment, `requirements.txt` — bạn đã có `.venv`, cần hiểu nó là gì
- `import`, module, `from x import y`
- Biến môi trường + `.env` — **không bao giờ hardcode API key vào code**
- Gọi một model bằng SDK: gửi message, đọc response
- Đọc được doc: tham số nào bắt buộc, response có cấu trúc gì

**Đạt khi tự làm được:**
- [ ] Tạo venv mới, cài thư viện, xuất `requirements.txt`
- [ ] Gọi model từ script, in ra câu trả lời
- [ ] API key nằm trong `.env`, `.env` nằm trong `.gitignore`
- [ ] Chỉ ra được trong response object chỗ nào chứa text, chỗ nào chứa số token

**Bài build:** `ask-my-docs` nhận câu hỏi từ dòng lệnh, gửi cho model, in câu trả lời.

**Câu hỏi mình sẽ hỏi bạn:**
> Nếu bạn commit nhầm `.env` lên GitHub rồi xóa ở commit sau, key còn lộ không? Vì sao?

---

## Module 4 — Code không sập

**Mục tiêu:** phân biệt script chạy một lần và chương trình dùng được.

**Nguồn:** CS50P tuần 3 (Exceptions) + tuần 4 (Libraries)

**Nội dung cần:**
- `try / except / finally`, bắt đúng loại lỗi chứ không `except:` trống
- Lỗi thật khi gọi API: rate limit, timeout, mạng đứt, response sai format
- Retry với exponential backoff — tự viết tay trước, dùng thư viện sau
- `logging` thay cho `print`
- Type hints: `def search(q: str, k: int = 5) -> list[str]:` — code AI hiện đại đầy thứ này

**Đạt khi tự làm được:**
- [ ] Bắt riêng lỗi rate limit và lỗi mạng, xử lý khác nhau
- [ ] Viết retry 3 lần, mỗi lần chờ gấp đôi
- [ ] Giải thích vì sao `except Exception: pass` là thói quen nguy hiểm
- [ ] Thêm type hint cho toàn bộ hàm đã viết

**Bài build:** `ask-my-docs` gọi API 50 lần liên tiếp mà không chết giữa chừng.

**Câu hỏi mình sẽ hỏi bạn:**
> Retry mọi lỗi có phải ý hay không? Lỗi nào retry là vô nghĩa?

---

## Module 5 — RAG hoàn chỉnh ⭐

**Mục tiêu:** đích đến. Từ đây bạn có thứ để đưa người khác xem.

**Nguồn:** khóa RAG deeplearning.ai (mở lại **ở đây**, không phải trước đó)

**Nội dung cần:**
- Gọi embedding API, nhận về vector
- Cosine similarity — tự viết bằng numpy trước khi dùng thư viện
- Lưu vector: bắt đầu bằng list trong bộ nhớ, **chưa cần vector DB**
- Ghép prompt: context + câu hỏi → context window
- Generator / `yield` — để stream câu trả lời

**Đạt khi tự làm được:**
- [ ] Giải thích cosine similarity bằng lời, không dùng công thức
- [ ] Trả lời đúng một câu hỏi mà model không thể biết nếu không có tài liệu
- [ ] Chỉ ra chunk nào đã được retrieve cho mỗi câu trả lời
- [ ] Tìm được một câu hỏi mà RAG của bạn **trả lời sai**, và giải thích vì sao

**Bài build:** RAG chạy end-to-end trên tài liệu thật của bạn.

**Câu hỏi mình sẽ hỏi bạn:**
> Retrieve top-3 chunk nhưng cả 3 đều không liên quan — hệ thống của bạn làm gì? Nó có biết là nó không biết không?

---

## Module 6 — Đưa cho người khác chạy

**Mục tiêu:** ranh giới giữa "em có làm thử" và "đây, anh chạy đi".

**Nguồn:** CS50P tuần 8 (OOP — chỉ đủ để đọc) + tuần 9 (argparse)

**Nội dung cần:**
- `class` — đủ để **đọc**; mọi framework agent đều là class
- `__init__`, `self`, method — không cần kế thừa sâu
- Decorator — đủ để hiểu `@tool`, `@app.get` đang làm gì
- `argparse` hoặc `typer` — CLI có `--help`
- `README.md` với hướng dẫn cài đặt chạy được trên máy sạch

**Đạt khi tự làm được:**
- [ ] Gói toàn bộ thành `class DocSearcher` với method rõ ràng
- [ ] `python ask.py --help` in ra hướng dẫn tử tế
- [ ] Người khác clone repo, làm theo README, chạy được — **không nhắn hỏi bạn câu nào**

**Bài build:** push lên GitHub, nhờ một người thật chạy thử.

---

## Những thứ CS50P có mà bạn BỎ QUA được (bây giờ)

| Nội dung | Tuần | Vì sao bỏ |
|---|---|---|
| Regular expressions sâu | 7 | Biết `re.sub` cơ bản là đủ; hiếm là nút thắt trong RAG |
| Unit test chi tiết | 5 | Quan trọng, nhưng học khi đã có code đáng test |
| OOP kế thừa, `@classmethod`, dunder | 8 | Đọc hiểu là đủ; viết thì chưa cần |
| Problem set dạng đố vui | mọi tuần | Luyện tư duy thuật toán, không phải nút thắt của bạn |

**Không phải "không cần mãi mãi"** — là "chưa phải bây giờ". Quay lại sau M6.

---

## Điều kiện mình kèm theo

Bạn rút gọn Python để tiến nhanh tới build — hợp lý. Nhưng có một cái bẫy:

**Rút gọn kiến thức thì được. Rút gọn việc tự gõ code thì không.**

Nếu bạn đọc giáo trình này rồi bảo AI viết hộ từng module, bạn sẽ về đúng chỗ xuất phát: có code chạy được mà không có judgment. Mà judgment mới là thứ cả hai video bạn đã note đều nói là thứ duy nhất còn được trả tiền.

Quy ước: **mỗi ô `[ ]` ở trên phải do tay bạn gõ ra.** Mình ra đề, gợi ý, chỉ chỗ sai, hỏi vặn. Mình không viết hộ.

---

## Bài học rút ra cho mình
<!-- TỰ VIẾT -->


## Hành động
- [ ]
