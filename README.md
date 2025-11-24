# Báo Cáo Dự Án AI Agent (6 Node)

## 1. Giới Thiệu Project
Dự án này là một hệ thống Chatbot thông minh được xây dựng dựa trên thư viện **LangGraph**. Hệ thống có khả năng phân loại ý định của người dùng từ tin nhắn đầu vào và tự động định tuyến (route) đến các chuyên gia (agent) phù hợp để xử lý.

Mục tiêu của dự án là cung cấp các câu trả lời chuyên sâu và chính xác hơn bằng cách sử dụng các agent chuyên biệt thay vì một mô hình chung chung.

## 2. Cấu Trúc Project
Cấu trúc thư mục chính của dự án:

```
.
├── main.py                 # File chạy chính của chương trình (Entry point)
├── pyproject.toml          # Quản lý dependencies và cấu hình project
├── src/                    # Source code chính
│   ├── graph/              # Định nghĩa đồ thị (Graph) và trạng thái (State)
│   │   ├── state.py        # Xây dựng StateGraph, định nghĩa các node và edge
│   │   └── schema.py       # Định nghĩa cấu trúc dữ liệu (State, MessageClassifier)
│   ├── nodes/              # Chứa logic xử lý của các node
│   │   ├── classify_message.py # Node phân loại tin nhắn
│   │   ├── router.py           # Node điều hướng
│   │   ├── football_expert.py  # Agent chuyên gia bóng đá
│   │   ├── therapist_agent.py  # Agent chuyên gia tâm lý
│   │   ├── logical_agent.py    # Agent tư duy logic/kỹ thuật
│   │   └── default_agent.py    # Agent xử lý hội thoại chung
│   └── models/             # Cấu hình Model (LLM)
```

## 3. Các Node Chức Năng
Hệ thống bao gồm các node chính sau:

1.  **Classifier (`classify_message`)**:
    *   Sử dụng LLM để phân tích tin nhắn người dùng.
    *   Phân loại tin nhắn vào một trong 4 nhóm: `emotional` (cảm xúc), `logical` (logic/kỹ thuật), `football` (bóng đá), hoặc `general` (chung).

2.  **Router (`router`)**:
    *   Nhận kết quả từ Classifier.
    *   Quyết định node tiếp theo sẽ được kích hoạt dựa trên loại tin nhắn.

3.  **Các Agent Chuyên Biệt**:
    *   **Therapist Agent**: Xử lý các vấn đề về cảm xúc, tâm lý.
    *   **Football Expert**: Trả lời các câu hỏi về bóng đá, tỉ số, cầu thủ.
    *   **Logical Agent**: Giải quyết các câu hỏi về sự kiện, kỹ thuật, phân tích logic.
    *   **General Agent**: Xử lý các câu chào hỏi xã giao hoặc các câu hỏi không rõ ràng.

## 4. Luồng Xử Lý (Workflow)
Luồng đi của một tin nhắn như sau:

1.  **Input**: Người dùng nhập tin nhắn từ `main.py`.
2.  **Start**: Tin nhắn được đưa vào Graph.
3.  **Classify**: Node `classifier` phân tích tin nhắn và gán nhãn (label).
4.  **Route**: Node `router` kiểm tra nhãn và chuyển hướng:
    *   Nếu là `emotional` -> Chuyển đến **Therapist**.
    *   Nếu là `football` -> Chuyển đến **Football Expert**.
    *   Nếu là `logical` -> Chuyển đến **Logical Agent**.
    *   Khác -> Chuyển đến **General Agent**.
5.  **Process**: Agent được chọn sẽ sinh ra câu trả lời.
6.  **End**: Kết thúc quy trình và trả về câu trả lời cho người dùng.

## 5. Cách Chạy Project

### Yêu cầu
*   Python >= 3.12
*   API Key của Google Gemini (hoặc model tương đương được cấu hình trong `src/models`).

### Cài đặt
1.  Clone repository về máy.
2.  Cài đặt các thư viện cần thiết:
    ```bash
    pip install -r requirements.txt
    # Hoặc nếu dùng uv/poetry thì cài theo pyproject.toml
    pip install langgraph langchain-google-genai python-dotenv ipykernel
    ```
3.  Tạo file `.env` và cấu hình API Key (nếu cần):
    ```
    GOOGLE_API_KEY=your_api_key_here
    ```

### Chạy chương trình
Mở terminal tại thư mục gốc của dự án và chạy lệnh:

```bash
python main.py
```

Nhập tin nhắn và nhấn Enter để trò chuyện với bot. Gõ `exit` để thoát.
