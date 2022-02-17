from datetime import datetime
import sqlite3
from flask import Flask, g, render_template, flash, request, redirect
import sqlite3
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.config.from_object(__name__)

load_dotenv()
SECRETKEY = os.environ.get("SECRETKEY")
DATABASE = os.environ.get("DATABASE")

def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_any_request():
    g.db = connect_db()

@app.teardown_request
def req_end(exc):
    g.db.close()

@app.route("/")
def show_msg():
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    cur = g.db.execute(sql)
    msg = [{'title':title, 'text': text} for title, text in cur.fetchall()]
    return render_template('showmsg.html', msg=msg)

@app.route("/insert", methods=['POST'])
def insert():
    sql = "INSERT INTO entradas(titulo, texto) VALUES (?, ?);"
    title = request.form['title']
    text = request.form['text']
    #date = datetime(now)
    g.db.execute(sql, [title, text])
    g.db.commit()
    g.db.close()
    return redirect("/")

# if __name__ == "__main__":
# 	app.run()