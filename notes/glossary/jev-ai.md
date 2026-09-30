# Jev AI

- **Loại:** Kỹ thuật chuyên sâu — **⚠️ CHƯA XÁC MINH ĐỘC LẬP**
- **Ngày tạo:** 2026-09-30
- **Chủ đề:** ai-agent, model-routing

> ⚠️ **Cảnh báo độ tin cậy:** Các nguồn tìm được đều xuất hiện đồng loạt trong một khoảng thời gian ngắn (huggingface blog, langchain blog, vercel, mindstudio, medium, substack, một trang "Wikipedia"), mô tả rất trơn tru và khớp nhau bất thường về một công ty/mô hình rất mới ("TypeSafe AI", ra mắt 15/9/2026). Khi kiểm tra chéo, chính nội dung "Wikipedia" tự nhận xét ngày phát hành tương lai "gợi ý đây là tài liệu hư cấu" (fictional documentation). Chưa tìm được nguồn độc lập, đáng tin cậy bên ngoài cụm này (Forbes/TechCrunch chỉ được *nhắc tên*, chưa xác minh bài gốc). **Nhiều khả năng đây là nội dung hư cấu/marketing/thử nghiệm, không phải một sản phẩm AI đã xác lập.** Đọc phần dưới như mô tả *theo nguồn tự nhận*, không phải sự thật đã kiểm chứng.

## Định nghĩa ngắn gọn

Theo các nguồn (chưa kiểm chứng): Jev là một mô hình AI độc quyền của công ty "TypeSafe AI", không sinh văn bản tự nhiên như LLM mà trả về giá trị có kiểu dữ liệu (typed values) kèm xác suất/độ tin cậy — được mô tả như một "lớp quyết định" (decision layer) tốc độ cao cho phân loại, định tuyến, chấm điểm trong ứng dụng.

## Giải thích chi tiết
- Được định vị (theo marketing) là "System One model" — đối lập với LLM "System Two" tốn kém, chậm — nhằm giải quyết vấn đề chi phí/độ trễ khi dùng LLM đầy đủ cho các quyết định đơn giản, lặp lại.
- Công ty tự nhận huấn luyện bằng "Reinforcement Learning for Calibrated Decisions (RLCD)" trên dữ liệu tổng hợp, tối ưu xác suất theo kết quả thực tế thay vì theo sở thích người đánh giá.
- Các chỉ số hiệu năng (200x nhanh hơn, 400x rẻ hơn) do chính đội ngũ công ty tạo ra và công bố — không có bên thứ ba kiểm chứng.

## Cơ chế hoạt động
- Input: một khối **trạng thái** (state — chuỗi, JSON, hoặc mảng văn bản) + một hoặc nhiều **câu hỏi có kiểu** (typed questions).
- Mô hình đánh giá tất cả câu hỏi trên cùng trạng thái trong **một lượt xử lý song song** (single parallel pass), 70–500ms.
- Ba loại câu hỏi (primitives):
  - **Choice**: chọn 1 trong các lựa chọn định sẵn, kèm xác suất từng lựa chọn.
  - **Score**: chấm điểm theo thang đo có thứ tự.
  - **Noul**: câu hỏi đúng/sai, trả về xác suất.
- Vì output luôn theo schema định trước, nguồn tự nhận điều này giúp giảm lỗi định dạng/"hallucination" so với LLM sinh text tự do.

## Ví dụ cụ thể

Theo nguồn: phân loại một ticket hỗ trợ có khẩn cấp không.
```json
{
  "state": "Tôi đã cố kết nối Stripe 3 ngày mà không được...",
  "questions": {
    "is_urgent": "Tin nhắn này có truyền đạt tính khẩn cấp không?"
  }
}
```
Kết quả trả về: xác suất khẩn cấp ~99.9%.

## Ứng dụng thực tế
- **Model routing**: dùng Jev để đánh giá độ phức tạp của yêu cầu, từ đó định tuyến sang mô hình nhanh/rẻ hay mô hình mạnh/đắt.
- **Guardrail trong AI agent**: kiểm tra một hành động/tool call có rủi ro trước khi cho thực thi ("gating tool calls").
- Cả hai use case đều nằm trong phạm vi khái niệm **AI harness** — lớp điều phối bao quanh model chính để kiểm soát hành vi agent.

## Thuật ngữ liên quan
- [AI Harness](ai-harness.md) — Jev (theo nguồn) là một thành phần có thể dùng bên trong một AI harness để gate/route quyết định.

## Nguồn tham khảo
1. [What Is Jev AI? A Practical Guide (Hugging Face blog)](https://huggingface.co/blog/sora-2/what-is-jev-ai-a-practical-guide-to-system-one-and) — ⚠️ chưa xác minh
2. [Jev (AI model) — "Wikipedia"](https://en.wikipedia.org/wiki/Jev_(AI_model)) — ⚠️ tự nhận xét ngày phát hành tương lai gợi ý nội dung hư cấu
3. [What Is Jev? A Guide to TypeSafe AI's System One Model (LangChain blog)](https://www.langchain.com/blog/building-a-harness-with-jev) — ⚠️ chưa xác minh
4. [What is Jev, TypeSafe AI's System One model? (Vercel)](https://vercel.com/i/what-is-jev) — chưa đọc chi tiết, liệt kê để tham khảo thêm
