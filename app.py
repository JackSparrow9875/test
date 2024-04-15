from flask import Flask, render_template, redirect, flash, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'Library'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)


#----------------------TABLES-----------------------------
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=True)
    email = db.Column(db.String(128), unique=True, nullable=True)
    password = db.Column(db.String(128), nullable=True)


#------------------APP INTERFACE--------------------------
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/userlist')
def userlist():
    users = Users.query.all()
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
                new_user = Users(Name=name, Email=email, password=password)
                db.session.add(new_user)
                db.session.commit()
                flash('User added successfully')
            else:
                flash('Passwords donot match, please try again...')
                return render_template('signup.html')
        except Exception as e:
            flash(f'An error occured: {str(e)}')
            return render_template('signup.html')
    return render_template('signup.html')


@app.route('/userlogin', methods=['POST', 'GET'])
def login():
    email = None
    password = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            conn = get_db_cursor()
            c = conn.cursor()
            c.execute('''SELECT * FROM Users WHERE Email = ?''', (email,))
            user = c.fetchone()
            if user is None:
                flash('No user is found...')
            elif user[3] != password:
                flash('Incorrect password, please try again...')
            else:
                flash('Login successfull!')
                return render_template('user_dashboard.html', user=user)
        except Exception as e:
            flash(f'An error occured: {str(e)}')
            return redirect(url_for("index"))
    return render_template('userlogin.html')


@app.route('/user/delete/<int:id>')
def deleteuser(id):
    conn = get_db_cursor()
    c = conn.cursor()
    try:
        c.execute('''DELETE FROM Users WHERE ID = ?''', (id,))
        conn.commit()
        flash('User has been deleted successfully. We are sad to see you leave')
        return redirect(url_for('login'))
    except Exception as e:
        flash(f'An error has occured: {str(e)}')
        return redirect(url_for("userlist"))
    finally:
        conn.close()


#----------------------ERROR PAGES--------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



if __name__ == '__main__':
    app.run(debug=True)