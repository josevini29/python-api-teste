from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return str({"status": "ok", "message":"hello word", "by":"José Vinicius"}), 200

app.run()