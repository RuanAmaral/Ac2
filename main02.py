from flask import Flask, render_template, request
import os
#import mysql.connector
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'     
app.config['MYSQL_DATABASE_PASSWORD'] = 'ruan123' 
app.config['MYSQL_DATABASE_DB'] = 'testes' 
app.config['MYSQL_DATABASE_HOST'] = 'db' 
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('login02.html')

@app.route("/gravar", methods=['post', 'get'])
def gravar_dados():
    nome = request.form["nome"]
    preco = request.form["preco"]
    categoria = request.form["categoria"]
    if nome and preco and categoria:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("insert into tb_login (nome, preco, categoria) VALUES(%s,%s,%s)", (nome, preco, categoria))
        conn.commit()
    return render_template("login02.html")

@app.route("/listar", methods=['post', 'get'])
def listar():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("select nome, preco, categoria from tb_login")
    data = cursor.fetchall()
    conn.commit()
    return render_template("dados02.html", titulo="Dados", datas=data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5005))
    app.run(host='0.0.0.0', port=port)
