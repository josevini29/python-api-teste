import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return '{"status":"ok","message":"hello word!","by":"José Vinicius","email":"josevini29@hotmail.com"}', 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)