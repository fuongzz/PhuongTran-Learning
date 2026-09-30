# AI Harness (Agent Harness)

- **Loại:** Kỹ thuật chuyên sâu
- **Ngày tạo:** 2026-09-30
- **Chủ đề:** ai-agent, llm-infrastructure

## Định nghĩa ngắn gọn

AI harness (hay agent harness) là lớp hạ tầng phần mềm bao quanh một LLM, biến nó từ "chỉ trả lời prompt" thành một **agent có thể hành động**: gọi tool, giữ trạng thái, tuân theo policy, và tự lặp lại các bước cho đến khi hoàn thành tác vụ. Công thức thường được dùng: **Agent = Model + Harness**.

## Giải thích chi tiết
- Bản thân LLM chỉ sinh ra văn bản/tool-call đề xuất — nó không tự thực thi hành động, không tự nhớ giữa các lượt gọi, không tự biết hành động nào được phép. Harness là phần giải quyết tất cả những việc đó.
- Vấn đề nó giải quyết: cùng một model có thể cho kết quả tốt hơn hoặc tệ hơn rất nhiều tùy vào harness được xây dựng ra sao — nên "harness engineering" dần trở thành một mảng kỹ thuật riêng, tách khỏi "prompt engineering".
- Đây chính là lớp mà các sản phẩm như Claude Code, Cursor, hay các agent framework (Microsoft Agent Framework, v.v.) triển khai xung quanh model nền.

## Cơ chế hoạt động
Harness vận hành quanh một **vòng lặp Reason → Act → Observe → Repeat** (ReAct loop):
1. **Reason** — model phân tích ngữ cảnh hiện có, quyết định hành động tiếp theo.
2. **Act** — harness thực thi hành động đó (gọi tool, chạy code, truy vấn dữ liệu...), *không phải model tự làm*.
3. **Observe** — kết quả hành động được đưa ngược lại làm ngữ cảnh mới.
4. **Repeat** — lặp lại đến khi tác vụ hoàn thành hoặc chạm giới hạn.

Các thành phần cốt lõi thường thấy trong một harness:
- **System prompt / instructions** — chỉ dẫn hành vi và giới hạn (guardrail) cho agent.
- **Tools & execution** — API, trình chạy code, database mà agent được phép gọi.
- **Sandbox** — môi trường cô lập để chạy code/tool an toàn.
- **Filesystem / storage** — lưu file, trạng thái xuyên suốt phiên làm việc.
- **Memory management** — theo dõi ngữ cảnh trong và giữa các phiên hội thoại (bao gồm cả nén/compaction khi ngữ cảnh quá dài).
- **Feedback loop** — tự kiểm tra, tự sửa lỗi.
- **Guardrail / approval** — kiểm soát quyền, yêu cầu người dùng duyệt hành động rủi ro (human-in-the-loop).
- **Observability** — ghi log, audit trail để theo dõi và debug.

Ví dụ cụ thể từ Microsoft Agent Framework: một `HarnessAgent` được lắp ráp từ nhiều khối — chat client (kết nối model) → chat pipeline (gọi hàm, nén lịch sử) → context providers (bộ nhớ, todo, chế độ hoạt động) → middleware (duyệt hành động, observability) → lớp UX ứng dụng (hiển thị tiến trình, xin phê duyệt).

## Ví dụ cụ thể

Tạo một agent có harness bằng Microsoft Agent Framework (Python):
```python
from agent_framework import create_harness_agent
from agent_framework.openai import OpenAIChatClient

agent = create_harness_agent(client=OpenAIChatClient(model="gpt-4o"))
session = agent.create_session()
response = await agent.run("Plan a weekend trip to Seattle.", session=session)
```
Ở đây, model (`gpt-4o`) chỉ lo phần suy luận/sinh nội dung; harness (`create_harness_agent`) lo phần quản lý session, tool-calling, todo tracking, tool approval, observability — tất cả đã bật sẵn theo mặc định.

## Ứng dụng thực tế
- **Coding agent** (Claude Code, Cursor,...): harness quản lý việc đọc/sửa file, chạy lệnh shell, xin phép trước hành động nguy hiểm.
- **Research/data agent**: harness quản lý truy vấn nhiều nguồn, tổng hợp, giữ trạng thái tiến trình dài hạn.
- **Enterprise agent có kiểm soát rủi ro**: harness là nơi đặt guardrail, ví dụ chặn tool call nguy hiểm trước khi thực thi (liên hệ tới khái niệm "gating tool calls" — xem thêm phần Jev AI bên dưới, dù nguồn về Jev AI chưa được xác minh).

## Thuật ngữ liên quan
- [Jev AI](jev-ai.md) — theo nguồn (⚠️ chưa xác minh độc lập), được quảng cáo là một mô hình quyết định nhanh có thể dùng làm guardrail/router *bên trong* một AI harness.

## Nguồn tham khảo
1. [What is an AI Agent Harness? — Databricks](https://www.databricks.com/blog/ai-harness)
2. [Agent Harness — Microsoft Learn (Agent Framework)](https://learn.microsoft.com/en-us/agent-framework/concepts/harness)
3. [What is an AI harness? — Parallel.ai](https://parallel.ai/articles/what-is-an-agent-harness) (tham khảo thêm, chưa fetch chi tiết)
4. [AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents — arXiv](https://arxiv.org/pdf/2605.13357) (paper, tham khảo thêm)
