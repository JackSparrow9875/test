from flask import Flask, render_template, redirect, flash, request
import sqlite3
from datetime import datetime


app = Flask(__name__)


def get_db_cursor():
    conn = sqlite3.connect('Library')
    return conn


#------------------APP INTERFACE--------------------------
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/userlist')
def userlist():
    conn = get_db_cursor()
    c = conn.cursor()
    c.execute('''SELECT * FROM Users''')
    users = c.fetchall()
    return render_template('userlist.html', users=users)



#--------------------USER--------------------------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    name = None
    email = None
    password1 = None
    password2 = None
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        try:
            if password1 == password2:
                password = password1
                conn = get_db_cursor()
                c = conn.cursor()
                c.execute('''
                          INSERT INTO Users (Name, Email, Password)
                          VALUES (?,?,?)''', (name, email, password))
                conn.commit()
                conn.close()
            else:
                flash('Passwords donot match, please try again...')
                return render_template('signup')
        except Exception as e:
            flash(f'An error occured: {str(e)}')
            return render_template('signup.html')
    return render_template('signup.html')



#----------------------ERROR PAGES--------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



if __name__ == '__main__':
    app.run(debug=True)