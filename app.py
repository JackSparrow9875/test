from flask import Flask, render_template, redirect
import sqlite3

__name__ = '__main__'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)