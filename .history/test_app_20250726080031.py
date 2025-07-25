from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def dns_test():
    hostname = 'oauth2.googleapis.com'
    try:
        ip = socket.gethostbyname(hostname)
        return f"SUCCESS: '{hostname}' resolved to {ip}"
    except Exception as e:
        # 오류를 HTML로 보기 좋게 표시
        return f"<h1>FAIL</h1><p>Could not resolve '{hostname}'</p><p>Error: {e}</p>", 500

if __name__ == '__main__':
    # Railway의 PORT 변수를 사용
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port)