import sqlite3
from flask import Flask, g
import sqlite3

DATABASE = 'blog.db'
SECRETKEY = 'y@vasurA'


app = Flask(__name__)
app.config.from_object(__name__)

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
    msg = []
    return str(msg)

# if __name__ == "__main__":
# 	app.run()