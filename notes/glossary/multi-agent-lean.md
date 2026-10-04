# Multi-agent architecture kiểu Lean

## Câu hỏi

Mô hình multi-agent kiểu “lean”: một việc – một agent làm; chỉ gọi thêm agent khi task khó hoặc có rủi ro. Các vai trò gồm Root/Orchestrator, Explorer, Worker, Researcher và Reviewer. Câu hỏi đặt ra là cách hiểu chi tiết mô hình này và tích hợp để dùng cho mọi project.

## Tổng quan

Đây là một dạng **hierarchical multi-agent system**. Một agent điều phối trung tâm phân rã công việc, giao cho các agent chuyên môn, sau đó kiểm tra và tích hợp kết quả.

```text
                         Root / Orchestrator
                                  |
              +-------------------+-------------------+
              |                   |                   |
           Explorer            Worker              Researcher
           Soi code          Viết code             Tra cứu
                                  |
                              Reviewer
```

## Vai trò

### Root / Orchestrator

Root không nên làm tất cả. Nó chịu trách nhiệm:

1. Hiểu yêu cầu.
2. Chia nhỏ công việc.
3. Giao nhiệm vụ.
4. Theo dõi trạng thái.
5. Hợp nhất kết quả.
6. Chạy kiểm tra cuối cùng.
7. Quyết định có cần Reviewer hay không.

### Explorer

Explorer chỉ đọc và điều tra: tìm file, tìm hàm hoặc class, vẽ flow, xác định test và phát hiện rủi ro. Explorer không sửa code.

Output nên có cấu trúc:

```json
{
  "relevant_files": ["src/auth/login.ts"],
  "entry_points": ["loginUser()"],
  "current_flow": ["LoginForm -> loginUser -> SessionService"],
  "risks": ["Session cookie được tạo ở SessionService"]
}
```

### Researcher

Researcher đọc tài liệu API, kiểm tra phiên bản, so sánh pattern và đưa ra khuyến nghị. Nó không sửa repository.

### Worker

Worker là agent chịu trách nhiệm triển khai một thay đổi cụ thể và viết test. Worker phải được cấp mục tiêu, phạm vi file, context cần thiết và tiêu chí hoàn thành. Worker không tự ý mở rộng phạm vi hoặc refactor ngoài yêu cầu.

### Reviewer

Reviewer nên được gọi khi code quan trọng, thay đổi lớn, test fail, có migration database, authentication, payment, permissions hoặc rủi ro bảo mật. Reviewer nên read-only ở lượt đầu và trả về các finding có mức độ nghiêm trọng cùng khuyến nghị sửa.

## Khi nào chạy song song?

Có thể chạy song song các task chỉ đọc, độc lập và không sửa cùng file. Ví dụ Explorer kiểm tra codebase trong khi Researcher đọc tài liệu OAuth.

Các task ghi file hoặc có dependency nên chạy tuần tự. Quy tắc an toàn là: **có thể song song ở tầng đọc và phân tích; nên tuần tự ở tầng ghi và tích hợp**.

## Task contract

Mỗi task nên có owner duy nhất, scope rõ ràng, dependency, acceptance criteria và output schema.

```json
{
  "task_id": "implement-login",
  "goal": "Thêm đăng nhập Google",
  "scope": {
    "allowed_files": ["src/auth/**", "tests/auth/**"],
    "forbidden_actions": ["Không sửa database schema"]
  },
  "acceptance_criteria": [
    "Đăng nhập thành công",
    "Login thất bại trả lỗi phù hợp",
    "Có test cho success và failure"
  ],
  "expected_output": ["changed_files", "test_results", "remaining_risks"]
}
```

## Kiến trúc tích hợp tổng quát

```text
User Request
    -> Task Classifier
    -> Orchestrator
       -> Explorer / Researcher / Worker
    -> Integration
       -> Format / Type check / Test / Diff review
    -> Reviewer nếu cần
```

Các thành phần quan trọng:

- **Agent registry**: khai báo quyền, công cụ và khả năng của từng agent.
- **Tool policy**: không cấp toàn bộ công cụ cho mọi agent.
- **Shared task store**: lưu task, dependency, kết quả, trạng thái test và retry.
- **Workspace isolation**: Worker song song nên có worktree hoặc workspace riêng.
- **Verification pipeline**: format, type check, unit test, integration test và review diff.

## Phân loại task

```text
Task nhỏ:        Root -> Worker -> Test
Task vừa:        Root -> Explorer -> Worker -> Test
Task cần tài liệu: Root -> Researcher -> Worker -> Test
Task rủi ro cao: Root -> Explorer + Researcher -> Worker -> Reviewer
```

Nên dùng progressive escalation: bắt đầu với số agent tối thiểu, chỉ tăng lực lượng khi có bằng chứng như thiếu context, test fail, xung đột file, vượt phạm vi hoặc rủi ro bảo mật.

## Retry và escalation

Mỗi task nên có giới hạn retry, thường là một hoặc hai lần. Nếu vẫn fail thì gọi Reviewer hoặc quay lại Root để điều chỉnh thiết kế. Không để agent lặp vô hạn.

Luồng an toàn:

```text
Worker -> Verification
       -> Pass: hoàn tất
       -> Fail: Worker sửa một lần
       -> Fail tiếp: Reviewer
```

## Các lỗi thường gặp

- Gọi quá nhiều agent cho task nhỏ.
- Hai Worker cùng sửa một file.
- Root vừa điều phối vừa code quá nhiều.
- Output tự do, không có schema.
- Tin vào câu “đã chạy test” mà không kiểm tra kết quả thực tế.
- Reviewer tự ý sửa code và biến thành Worker thứ hai.
- Nhiều Worker dùng chung một workspace.

## Công thức thực tế

1. Root xác định mục tiêu.
2. Root chia task theo đầu ra, không chỉ theo chức danh.
3. Mỗi task có một owner duy nhất.
4. Task độc lập thì chạy song song.
5. Task có dependency thì chạy tuần tự.
6. Worker chỉ sửa trong phạm vi được cấp.
7. Mọi thay đổi đều phải được verify.
8. Chỉ gọi Reviewer khi có rủi ro hoặc bằng chứng lỗi.
9. Mỗi agent trả về output có cấu trúc.
10. Root là nơi duy nhất quyết định hoàn tất.

Điểm cốt lõi không phải có bao nhiêu agent, mà là phân quyền rõ, phạm vi rõ, output rõ, workspace an toàn và tiêu chí hoàn thành rõ.
