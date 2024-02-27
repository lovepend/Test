import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_table():
    # SQLite 데이터베이스 연결
    conn = sqlite3.connect('Id.db')  # 실제 데이터베이스 파일명으로 변경
    cursor = conn.cursor()

    # 테이블에서 데이터 가져오기
    cursor.execute("SELECT id, name, sid, spw FROM users")
    data = cursor.fetchall()

    # HTML 템플릿에 데이터 전달
    return render_template('test.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)