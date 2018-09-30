import os
import psycopg2
import json
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    cur = con.cursor()
    sql = 'SELECT * FROM PYTHON_APP_TESTE.USERS'
    cur.execute(sql) 

    resultset = cur.fetchall()  

    users = []
    for rec in resultset:
        user = {"id_user": rec[0], "ds_user": rec[1], "ds_email": rec[2]}
        users.append(user)
  
    return json.dumps(users), 200

if __name__ == "__main__":

    SIS_APP_PROD = None

    try:
        SIS_APP_PROD = os.environ['SIS_APP_PROD']     
    except:
        print('Não foi possivel encontrar variavel que define ambiente de produção ou desenvolvimento.')
        exit()

    try:
        if (SIS_APP_PROD == '1'): #Produção
            DATABASE_URL = os.environ['DATABASE_URL'] 
            conn = psycopg2.connect(DATABASE_URL, sslmode='require')
            print('\033[33m AMBIENTE PRODUCAO \033[m')
        elif (SIS_APP_PROD == '0'): #Desenvolvimento
            con = psycopg2.connect(host='localhost', database='app_python', user='postgres', password='root')
            print('\033[32m AMBIENTE DESENVOLVIMENTO \033[m')
        else:
            print('Variavel que define ambiente com valor inválido:', SIS_APP_PROD)
            exit()  
 
    except:
        print('Erro ao conectar-se ao banco de dados PostgreSQL.')
        exit()

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


  