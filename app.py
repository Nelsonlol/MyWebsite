"""
作者:ge
日期:2021年12月07日0:24
"""
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
# app.config['SECRET_KEY'] = '1456719640@qq.com'


@app.route("/")
def root():
    """
    主页
    :return: Index.html
    """
    infos = []
    con = sqlite3.connect("xiaoliaoTable.db")
    cur = con.cursor()
    sql = "select * from xiaoliaoTable limit 0,12"
    data = cur.execute(sql)
    for item in data:
        infos.append(item)
    cur.close()
    con.close()
    return render_template('Index.html', infos=infos)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')
