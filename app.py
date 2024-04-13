from flask import Flask, render_template, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

#------------------APP INTERFACE--------------------------
@app.route('/')
def index():
    return render_template('home.html')


#--------------------USER--------------------------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    name = None
    email = None
    password = None

    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)