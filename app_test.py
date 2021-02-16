from flask import Flask, render_template, request
import mysql.connector as ms

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/insert',methods=['POST'])
def sf():
    if request.method=='POST':

        city=request.form['user']

        connection = ms.connect(host="localhost", user="root", passwd="Duoschat@123", database="world")
        db_cursor = connection.cursor()
        sql = "INSERT INTO test(number) values ("+str(city)+")"
        db_cursor.execute(sql)
        connection.commit()

        select_sql="select id from test where number="+city
        db_cursor.execute(select_sql)
        val=db_cursor.fetchone()         #---select query
        return str(val)

    """
    connection=ms.connect(host="localhost",user="root",passwd="Duoschat@123",database="world")
    db_cursor=connection.cursor()
    sql = "select Code from country where Name='Aruba'"
    db_cursor.execute(sql)
    a=db_cursor.fetchall()
    for x in a:
        ab=x
    return ab"""


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)
