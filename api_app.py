from flask import Flask, render_template, redirect, url_for, request
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="",
  database= "simple_crud"
)

app = Flask(__name__)

headings = ("Name", "Birthday", "Email")

mycursor = mydb.cursor()

try:
    mycursor.execute(
    '''
    CREATE TABLE users(
    `user_id` TINYINT(255) NOT NULL AUTO_INCREMENT,
    `name` CHAR(100) NOT NULL,
    `birthday` CHAR(100) NOT NULL,
    `email` CHAR(100) NOT NULL,
    PRIMARY KEY (`user_id`));
    '''
    )
except: pass

def update_table():
    mycursor.execute("SELECT * FROM users")

    data = []
    row_data = []

    for x in mycursor:
        row_data.append(x[0])
        row_data.append(x[1])
        row_data.append(x[2]) #.strftime("%d/%m/%Y")
        row_data.append(x[3])
        data.append(row_data)
        row_data = []
    return data

@app.route('/')
def table():
    data = update_table()
    return render_template("index.html", headings= headings, data = data)

@app.route("/edit/<user_id>")
def edit_index(user_id):
    mycursor.execute(f"SELECT * FROM users WHERE id_pessoa= '{user_id}'")
    user_data = mycursor.fetchone()
    return render_template("edit.html", user_id = user_id, user_data = user_data)

@app.route("/edit/<user_id>", methods=['GET', 'POST'])
def edit_user(user_id):
    if request.method == 'POST':
        if request.form.get("Edit") == "Edit":
            mycursor.execute(f"SELECT * FROM users WHERE user_id= '{user_id}'")
            user_data = mycursor.fetchone()
            return render_template("edit.html", user_id = user_id, user_data = user_data)
        if request.form.get("Confirm") == "Confirm":
            mycursor.execute(f"SELECT * FROM users WHERE user_id= '{user_id}'")
            user_data = mycursor.fetchone()

            name = user_data[1]
            birthday = user_data[2]
            email = user_data[3]

            if request.form.get("Name") != "":
                name = request.form.get("Name")

            if request.form.get("Birthday") != "":
                birthday = request.form.get("Birthday")

            if request.form.get("Email") != "":
                email = request.form.get("Email")
                

            data = update_table()
            mycursor.execute(f"""
            UPDATE users
            SET
            name = '{name}',
            birthday = '{birthday}',
            email = '{email}'
            WHERE user_id = '{user_id}';
            """)
            mydb.commit()
            return redirect("/")


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if  request.form.get("Delete") == "Delete":
            my_id = request.form.get("my_id","")
            mycursor.execute(f"DELETE FROM users WHERE user_id= '{my_id}'")
            mydb.commit()
        elif  request.form.get("Confirm") == "Confirm":
            name = request.form.get("Name")
            birthday = request.form.get("Birthday")
            email = request.form.get("Email")
            mycursor.execute(f"""
            INSERT INTO users(`name`,`birthday`,`email`) 
            VALUES ('{name}','{birthday}','{email}');
            """)
            mydb.commit()
        else:
            pass
        data = update_table()
        return render_template("index.html", headings= headings, data = data)
    elif request.method == 'GET':
        return render_template("index.html", headings= headings, data = data)
 
if __name__ == '__main__':
    app.run(debug=True)