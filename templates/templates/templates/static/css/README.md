# Dự án Web Flask Đơn Giản

Đây là một dự án web đơn giản được xây dựng bằng **Python** và framework **Flask**. Mục đích của dự án là minh họa cách cấu trúc một ứng dụng Flask cơ bản, sẵn sàng để phát triển thêm hoặc đưa lên host.

## Tính năng

- Trang chủ
- Trang giới thiệu
- Trang chào mừng người dùng động (ví dụ: `/user/An`)
- Sử dụng template kế thừa (base template)
- Tích hợp file CSS tĩnh

## Hướng dẫn cài đặt và chạy

1.  **Clone repository về máy:**
    ```bash
    git clone https://github.com/ten-cua-ban/ten-repository.git
    cd ten-repository
    ```

2.  **Tạo và kích hoạt môi trường ảo (khuyến khích):**
    ```bash
    # Trên a'Mac/Linux
    python3 -m venv venv
    source venv/bin/activate

    # Trên Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Cài đặt các thư viện cần thiết:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Chạy ứng dụng:**
    ```bash
    python app.py
    ```

5.  **Mở trình duyệt và truy cập:**
    - `http://127.0.0.1:5000/` để vào trang chủ.
    - `http://127.0.0.1:5000/about` để vào trang giới thiệu.
