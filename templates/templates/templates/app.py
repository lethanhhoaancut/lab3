# app.py

from flask import Flask, render_template

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Route cho trang chủ
@app.route('/')
def index():
    """Hàm xử lý cho trang chủ."""
    page_title = "Trang Chủ"
    return render_template('index.html', title=page_title)

# Route cho trang giới thiệu
@app.route('/about')
def about():
    """Hàm xử lý cho trang giới thiệu."""
    page_title = "Giới Thiệu"
    return render_template('about.html', title=page_title)

# Route động cho trang người dùng
# Ví dụ: /user/Khang
@app.route('/user/<string:name>')
def user(name):
    """Hàm xử lý cho trang người dùng với tên động."""
    page_title = f"Chào {name}"
    return render_template('user.html', title=page_title, user_name=name)

# Chạy ứng dụng khi file này được thực thi trực tiếp
if __name__ == '__main__':
    # Bật chế độ debug để tự động tải lại khi có thay đổi
    app.run(debug=True)
