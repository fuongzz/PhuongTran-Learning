# Essential Skills for Becoming an AI Engineer: RAG, AI Agents, & More

- **Loại:** Video
- **Nguồn:** Kênh YouTube không được nêu tên trong transcript, chỉ nói "our channel" *(suy luận: IBM Technology)*
- **Link:** https://www.youtube.com/watch?v=XN3xNJvWXsc
- **Ngày xem:** 2026-09-22
- **Chủ đề:** ai-engineering, skills, rag, agents, career
- **Đánh giá:** ⭐⭐⭐⭐☆
- **Đáng xem lại:** Có

## Tóm tắt 1 dòng

AI Engineer không train model mà lắp model có sẵn thành hệ thống chạy được, và bộ kỹ năng để làm việc đó xếp thành 3 tier: nền tảng kỹ thuật → kỹ năng AI (embeddings/RAG/agents) → deploy & vận hành.

## Nội dung chính

### Bối cảnh: vì sao con đường vào nghề đã đổi (00:01)
- Trước đây: bằng CS → internship → cày coding challenge → chờ callback.
- AI coding tools làm việc *viết code* không còn là phần khó nữa.
- Phần khó bây giờ là **judgment**: cấu trúc ứng dụng thế nào, xây cái gì, và **vì sao chọn cách này thay vì cách kia** — thứ lớp học khó dạy, phải học qua việc build.

### AI Engineer khác ML Researcher ở chỗ nào (01:19)
- **ML Researcher**: train foundation model từ đầu, publish paper về kiến trúc mới, cần toán sâu + bằng cấp cao.
- **AI Engineer**: build *với* model đã có sẵn (frontier hoặc open source), nối nó vào hệ thống làm việc có ích.
- Cụ thể là: nối model với data, cấp tools và thông tin bên ngoài, thêm memory, loop, guardrails.
- Ẩn dụ của video: researcher làm **động cơ**, AI engineer làm **chiếc xe**.

### Tier 1 — Foundations (03:05)
- Không phải kỹ năng AI, nhưng thiếu nó thì không build được gì. Thứ tự các tier quan trọng: nhiều người nhảy thẳng lên agent rồi phải quay lại học lại cơ bản.
- **Python**: không cần thành wizard, nhưng phải đủ đọc hiểu code — kể cả code do AI agent viết ra. Các lib ML/AI (PyTorch, TensorFlow) đều chạy trên Python.
- **Git + CLI + Linux**: để chia sẻ project và để làm việc trên đúng OS nơi agent sẽ được deploy.
- **API**: cách nối hai phần mềm với nhau — gọi model bằng code, xử lý response, xử lý rate limit. Mọi sản phẩm AI về bản chất là một chuỗi API call có cấu trúc tốt.

### Tier 2 — Kỹ năng AI engineering (04:30)
- **Embeddings & vector search**: chuyển text (PDF, các format khác) thành vector số, tìm theo **độ tương đồng ngữ nghĩa** chứ không phải khớp keyword — ví dụ "Kubernetes" gần với "containers", "orchestration".
- **RAG (Retrieval Augmented Generation)**: đưa thông tin có thật vào context window để model trả lời đúng thay vì bịa. Pipeline: document → chunk theo kích thước cố định → embed thành vector → lưu vào vector DB. Khi có câu hỏi: lấy đoạn liên quan từ DB + câu hỏi → nhét cả hai vào context window → model trả lời, có grounding.
- Gần như mọi công ty thử nghiệm AI đều muốn một phiên bản RAG nào đó, kể cả khi không dùng embeddings mà dùng dạng storage khác.
- **Agents & tool use**: kỹ năng applied AI được săn đón nhất hiện tại, vì agent chuyển từ *trả lời câu hỏi* sang *làm việc*.
- Phân biệt: **workflow** đi theo đường định sẵn A → B → C; **agent** tự quyết bước tiếp theo, gọi tool, quan sát kết quả, rồi lặp lại. Làm được loop này **đáng tin cậy và ở quy mô lớn** chính là định nghĩa của một AI engineer giỏi.

### Tier 3 — Ship & deploy (07:43)
- Giá trị thật chỉ xuất hiện khi thứ mình làm rời khỏi laptop và đến tay người dùng.
- **Containerization + Kubernetes**: đóng gói agent (đôi khi cả model) để deploy trên nhiều môi trường hybrid cloud.
- **Observability**: khi agent gọi model, gọi DB qua lại nhiều lượt, phải hiểu được *vì sao* nó ra quyết định cuối cùng — nền tảng của minh bạch và tin cậy.
- **Monitoring**: kiểm soát chi phí token và bảo mật.
- Deploy có thể trên bare metal (tách biệt hoàn toàn) hoặc cloud hosted service.

### Ba use case phổ biến nhất trong production (09:23)
- **RAG / knowledge systems**: HR service, bệnh viện, chatbot — cho người dùng hỏi và nhận lại dữ liệu có grounding.
- **Agents & tools**: agent query database, visualize data, làm những việc trước đây chỉ subject matter expert làm được.
- **Deployed applications**: dùng AI tool giúp engineer ship code trong vài giờ thay vì vài tuần.
- Lời khuyên: chọn build trong 3 mảng này, kết hợp với lĩnh vực mình quan tâm.

## Key insights
1. **Thứ tự học quan trọng hơn danh sách học.** Video nói thẳng: người ta hay nhảy thẳng vào agent trước khi biết xử lý data và hạ tầng, rồi mất thời gian học lại cơ bản. Tier 1 nhàm chán (Git, CLI, API) nhưng nó là điều kiện để hai tier trên không sụp.
2. **Ranh giới giữa workflow và agent là ranh giới của độ khó.** Viết một chuỗi bước cố định thì ai cũng làm được; làm một vòng lặp *tự quyết định* mà vẫn chạy ổn định ở quy mô lớn mới là phần khó — và đó chính là thứ nhà tuyển dụng trả tiền.
3. **RAG không phải là "kỹ thuật hay", nó là nhu cầu mặc định của doanh nghiệp.** Model không được train trên dữ liệu nội bộ của công ty, nên bất kỳ tổ chức nào muốn dùng AI trên dữ liệu của mình đều phải đi qua bài toán retrieval — dù có dùng vector DB hay không.
4. **Code không còn là lợi thế cạnh tranh, judgment thì có.** Khi AI viết được code, thứ phân biệt người giỏi là biết *chọn* kiến trúc nào, *vì sao*, và đọc hiểu được code AI sinh ra để bắt lỗi. Điều này kéo Python từ "biết viết" xuống "biết đọc" nhưng kéo tư duy hệ thống lên.
5. **Tier 3 là chỗ phần lớn người tự học bỏ quên.** Container, observability, monitoring chi phí token — demo trên laptop không cần, nhưng đó chính là phần khiến một project trở thành bằng chứng năng lực thay vì một notebook.

## Câu hỏi mở / điểm chưa đồng ý
- Video khẳng định "agent là kỹ năng applied AI được săn đón nhất hiện tại" nhưng không đưa bất kỳ số liệu tuyển dụng nào. Cần tự kiểm chứng bằng job posting thực tế.
- Tiêu đề hứa "three projects that'll help demonstrate your skills to potential employers" nhưng phần cuối chỉ liệt kê **3 use case** chung chung (RAG / agents / deployment), không phải 3 project cụ thể có scope rõ ràng. Phần thực hành bị bỏ ngỏ.
- Video gợi ý "không cần bằng CS" nhưng đồng thời yêu cầu Linux, Kubernetes, observability, API design — đây gần như là toàn bộ skillset của một backend/DevOps engineer. Câu hỏi thật là: người không nền tảng mất bao lâu để đi hết Tier 1? Video không trả lời.
- Chunking được nói qua một câu ("chunked in fixed sizes") — thực tế chunking strategy là một trong những chỗ quyết định chất lượng RAG nhiều nhất. *(suy luận, không có trong video)*

## Liên hệ với note khác
- [how-to-become-dangerously-self-educated.md](../learning-methods/how-to-become-dangerously-self-educated.md) — cùng luận điểm "code đã rẻ, thứ được trả tiền là hiểu bản chất và judgment". Note kia trả lời *vì sao* phải học như vậy; note này trả lời *học cái gì cụ thể* nếu chọn hướng AI engineering.

## Bài học rút ra cho mình
<!-- TỰ VIẾT: nó thay đổi gì trong cách mình học / làm? -->


## Hành động
- [ ]
