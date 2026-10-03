# Jev AI

- **Loại:** Kỹ thuật chuyên sâu
- **Ngày tạo:** 2026-09-30
- **Cập nhật:** 2026-10-03 — xác minh lại nguồn; bổ sung nội dung video IBM Technology
- **Chủ đề:** ai-agent, model-routing, calibration, guardrails

> ✅ **Công ty và mô hình: đã xác minh là có thật.** Cảnh báo *"nhiều khả năng là nội dung hư cấu"* trong bản note ngày 30/09 là **quá nặng và đã được sửa**. Bằng chứng:
> - Thông cáo báo chí qua **Business Wire** (15/09/2026), được Morningstar và Yahoo Finance syndicate: TypeSafe AI ra khỏi stealth với **40 triệu USD seed do DCVC dẫn dắt**, valuation khoảng 200 triệu USD.
> - Có **profile trên PitchBook, Tracxn, stockanalysis.com** — các nền tảng dữ liệu tài chính chỉ lập hồ sơ cho công ty thật.
> - **Nhà sáng lập:** Diogo Almeida (cựu researcher OpenAI, có tên trong công trình RLHF/InstructGPT), cùng Erik Gafni và Sasha Sheng.
> - **Video giải thích của IBM Technology** (Martin Keen, 01/10/2026) — nguồn độc lập đầu tiên ngoài cụm blog. Đã xác nhận kênh qua ảnh chụp màn hình.
>
> ⚠️ **Vẫn còn ba thứ CHƯA được kiểm chứng độc lập:**
> 1. **Mọi con số hiệu năng** (200x nhanh hơn, 400x rẻ hơn, 70–500ms) đến từ chính công ty. Video IBM chỉ nói *"nhanh và rẻ hơn LLM cho loại câu hỏi này"*, **không** đưa con số nào. Chưa có benchmark của bên thứ ba.
> 2. **Kiến trúc mô hình**: chính video IBM nói *TypeSafe chưa công bố nhiều về kiến trúc của Jev*. Mọi mô tả bên trong đều là những gì công ty tự nói.
> 3. Tin *"đang đàm phán gọi hơn 1 tỷ USD ở valuation trên 10 tỷ"* chỉ thấy ở nguồn chất lượng thấp — **chưa đáng tin**.

## Định nghĩa ngắn gọn

Jev là mô hình đầu tiên trong dòng **"System One"** của công ty **TypeSafe AI** (ra mắt 15/09/2026). Nó **không sinh văn bản**: bạn gửi vào một *trạng thái* + các *câu hỏi có kiểu dữ liệu*, nó trả về **xác suất** cho từng câu trả lời — và các xác suất đó được huấn luyện để **khớp với tỷ lệ đúng thực tế** (calibrated). Một "lớp quyết định" để code dùng trực tiếp, thay vì phải parse text do LLM sinh ra.

## Giải thích chi tiết

### System 1 vs System 2
- Tên lấy từ sách *Thinking, Fast and Slow* của Daniel Kahneman. **System 1**: nhanh, tự động — "2 × 2 = ?" bạn biết ngay là 4. **System 2**: chậm, có chủ đích — "17 × 24 = ?" phải tính từng bước.
- Chatbot sinh câu trả lời từng token một. Reasoning model còn viết ra cả chain of thought — đó là thứ gần System 2 nhất mà AI có.
- Nhưng **rất nhiều quyết định trong phần mềm không cần System 2** — chúng chỉ là phán đoán nhanh. Jev được làm cho đúng loại việc đó.

### Ba cách huấn luyện bằng reinforcement learning
Hầu hết LLM qua hai giai đoạn: **pre-training** (đọc lượng text khổng lồ, học đoán token tiếp theo) → **post-training** (thường dùng reinforcement learning: model trả lời, *thứ gì đó* chấm điểm, model bị đẩy về phía câu trả lời điểm cao). Khác nhau ở chỗ *ai chấm*:

| Kỹ thuật | Ai chấm điểm | Hệ quả |
|---|---|---|
| **RLHF** — RL from Human Feedback | Người chấm chọn câu trả lời thích hơn → train reward model | Người thích câu nghe tự tin → model **học cách nghe chắc chắn kể cả khi sai** |
| **RLVR** — RL with Verifiable Rewards | Tự động: bài toán đúng không, code pass unit test không | Lý do reasoning model giỏi toán & code. Nhưng chỉ thưởng *đáp án đúng*, **không thưởng việc biết mình chắc đến đâu**; lại chậm và đắt vì chain of thought |
| **RLCD** — RL for Calibrated Decisions | Thưởng khi **xác suất model đưa ra khớp với thực tế** | Đây là cách Jev được train |

### Calibration nghĩa là gì
Vẽ biểu đồ: trục ngang là xác suất model đưa ra, trục dọc là tỷ lệ model thực sự đúng. Model calibrate tốt sẽ nằm trên **đường chéo**: khi nó nói 80%, nó đúng khoảng 80% số lần.

Đây là điểm mấu chốt so với LLM: bạn có thể *hỏi* LLM nó chắc bao nhiêu phần trăm, nhưng con số nó nói ra **không nhất thiết khớp** với xác suất thật mà nó dùng để ra câu trả lời.

## Cơ chế hoạt động

**Input gồm hai thứ, gửi trong một request duy nhất:**
- **State** — dữ liệu mà quyết định xoay quanh. Ví dụ: email hỗ trợ + lịch sử giao dịch gần đây của khách.
- **Các câu hỏi**, mỗi câu một kiểu:

| Kiểu | Hỏi gì | Output |
|---|---|---|
| **Choice** | Chọn 1 trong danh sách cho trước | Một xác suất cho **mỗi** lựa chọn. Chỉ có thể là các lựa chọn bạn đưa vào — không bịa thêm được |
| **Score** | Chấm trên thang có thứ tự (vd. low → critical) | Vị trí trên thang |
| **Bool** *(?)* | Đúng / sai | Một con số, vd. 0.9 = 90% là "đúng" |

> ⚠️ **Tên kiểu đúng/sai vẫn chưa chắc.** Bản note cũ ghi "Noul", transcript tự động của video IBM ghi "null". Cả hai rất có thể là lỗi nghe/chép của chữ **"bool"** khi đọc thành tiếng — nhưng đây là suy luận. Cần đối chiếu doc gốc của TypeSafe.

**Vì sao nhanh hơn:** LLM phải viết JSON ra từng token một. Jev không sinh text, nên **cả ba câu trả lời về cùng lúc**.

**Model vẫn có thể sai** — chọn nhầm hay chấm lệch. Nhưng xác suất cho bạn biết khả năng sai là bao nhiêu.

## Ví dụ cụ thể

Email: *"Tháng này tôi bị trừ tiền hai lần, sửa giúp tôi."* Phần mềm cần trả lời ba câu:

| Câu hỏi | Kiểu | Kết quả (minh họa trong video) |
|---|---|---|
| Đây có phải yêu cầu hoàn tiền? | Bool | 0.9 |
| Team nào xử lý? (billing / technical / sales) | Choice | billing: 0.85 |
| Mức độ khẩn cấp? | Score | khoảng high → critical |

### Dùng xác suất để viết code: thiết kế ngưỡng (threshold)

Đây là phần thực tế nhất của video:

```
xác suất ≥ 0.9         → tự động: đưa thẳng vào hàng đợi hoàn tiền
0.1 < xác suất < 0.9   → không chắc: chuyển cho người kiểm tra
xác suất ≤ 0.1         → không phải hoàn tiền, bỏ qua
```

Vì xác suất đã được calibrate, **ngưỡng cũng cho biết đại khái nhánh tự động sẽ sai bao nhiêu lần**. Quy tắc: **sai càng đắt, ngưỡng đặt càng cao.**

## Ứng dụng thực tế
- **Phân loại / định tuyến** — ví dụ email hỗ trợ ở trên; định tuyến yêu cầu sang model nhanh/rẻ hay model mạnh/đắt.
- **Guardrail** — đặt quanh chatbot để kiểm tra tin nhắn đi vào/đi ra, ví dụ phát hiện jailbreak; hoặc gate tool call của agent trước khi thực thi.
- **Workflow kết hợp với LLM**, đúng như mô hình Kahneman: `Jev phân loại email → LLM viết thư trả lời → Jev phân loại phản hồi của khách`. Phần lớn công việc chạy trên System 1 nhanh; LLM (System 2) chỉ vào cuộc khi cần suy nghĩ thật.
- **Những chỗ LLM hiện quá chậm/đắt để đặt vào** — chấm *từng dòng* database, *từng dòng* log file.

## Giới hạn (theo video IBM)
- **Chỉ nhận input là text** (tại thời điểm video).
- **Kém về toán và cả việc đếm** — để những việc đó cho công cụ khác.
- **Có thể bị lừa bởi chỉ dẫn giấu trong dữ liệu nó đọc** (prompt injection) — như mọi model AI khác. Đáng chú ý vì nó lại được quảng bá làm guardrail.
- **Không thay thế LLM.** Hai loại bổ trợ cho nhau.

## Chuyện cái tên
Jev đặt theo **William Stanley Jevons** — nhà kinh tế học năm 1865 chỉ ra rằng khi động cơ hơi nước hiệu quả hơn, nước Anh lại **dùng nhiều than hơn** (*nghịch lý Jevons*). Hàm ý: khi một phán đoán trở nên cực nhanh và cực rẻ, người ta sẽ đặt nó vào nhiều chỗ hơn chứ không phải ít đi.

## Thuật ngữ liên quan
- [AI Harness](ai-harness.md) — Jev là một thành phần có thể dùng bên trong một AI harness để gate/route quyết định.

## Vì sao thuật ngữ này đáng theo dõi (nhưng chưa đáng học sâu)

Jev ra mắt chưa đầy một tháng, chưa có benchmark độc lập, và đang ở diện waitlist. Với lộ trình trong [python-for-ai-engineer.md](../skills/python-for-ai-engineer.md), đây là thứ **ghi vào sổ để biết, không phải thứ build bây giờ**.

Nhưng khái niệm nền của nó thì đáng nắm ngay, vì nó độc lập với sản phẩm:
- **Typed / structured output** — ràng buộc model trả về đúng schema. Gặp lại ở M3–M5.
- **Calibration** — model có biết mức độ nó không biết hay không. Chính là câu hỏi đã đặt ở M5: *"retrieve 3 chunk đều không liên quan — hệ thống có biết là nó không biết không?"*
- **Thiết kế ngưỡng theo chi phí sai lầm** — áp dụng được cho *bất kỳ* bộ phân loại nào có điểm số, kể cả cosine similarity trong RAG của bạn.

## Nguồn tham khảo

### Nhóm A — Nguồn độc lập / xác lập sự thật (độ tin cậy khá)
1. [IBM Technology — What Is Jev? The AI Model That Doesn't Generate Text](https://www.youtube.com/watch?v=YGgNBcIgI4s) — Martin Keen, 01/10/2026. Video giải thích; không phải benchmark.
2. [TypeSafe AI Emerges From Stealth With $40M in Funding — Business Wire via Morningstar, 15/09/2026](https://www.morningstar.com/news/business-wire/20260915525333/typesafe-ai-emerges-from-stealth-with-40m-in-funding-with-new-model-for-composable-ai) — thông cáo của công ty
3. [Bản syndicate trên Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/typesafe-ai-emerges-stealth-40m-190000776.html)
4. [PitchBook — Typesafe AI company profile](https://pitchbook.com/profiles/company/658924-30)
5. [Tracxn — TypeSafe company profile](https://tracxn.com/d/companies/typesafe/__fPC7t2VtGOz6qF_aK5y6KzoPEZ3dCBjkFq6qQcw51_c)
6. [FinSMEs — TypeSafe AI Raises $40M in Seed Funding](https://www.finsmes.com/2026/09/typesafe-ai-raises-40m-in-seed-funding.html)
7. [stockanalysis.com — TypeSafe AI valuation & funding](https://stockanalysis.com/private/typesafe-ai/)

### Nhóm B — Cụm blog nội dung trùng khớp (dùng để hiểu khái niệm, KHÔNG dùng để xác minh)
8. [LangChain blog — Building a harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev)
9. [Zapier — What Is Jev? TypeSafe AI System One Model](https://zapier.com/blog/jev/)
10. [Firecrawl — Inside TypeSafe Decision-Only AI Model](https://www.firecrawl.dev/blog/what-is-jev)
11. [MindStudio — Inside the AI Classifier Model Developers Are Racing to Adopt](https://www.mindstudio.ai/blog/what-is-jev-classifier-model)
12. [Hugging Face blog — A Practical Guide to System One](https://huggingface.co/blog/sora-2/what-is-jev-ai-a-practical-guide-to-system-one-and)
13. [daily.dev — The AI Model That Does Not Generate Text](https://daily.dev/posts/what-is-jev-the-ai-model-that-doesn-t-generate-text-jpe5yhzlr) — tiêu đề trùng với video IBM, nhiều khả năng là bài tóm tắt/repost của video
14. [Appinventiv — Enterprise Use Cases, Limits, and Adoption](https://appinventiv.com/blog/jev-usecases-and-adoption/)
