import os
from flask import Flask
import psycopg2

app = Flask(__name__)


DATABASE_URL = os.environ['DATABASE_URL']
#print('Erro ao tentar encontrar variavel de ambiente do banco de dados.')
print('DATABASE_URL: ' + DATABASE_URL)

@app.route("/")
def hello():
    return '{"status":"ok","message":"hello word!","by":"José Vinicius","email":"josevini29@hotmail.com","Country":"Brazil"}', 200

if __name__ == "__main__":

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


  