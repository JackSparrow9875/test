from flask import Flask

__name__ = '__main__'

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hi</h1>'

#comment added
if __name__ == '__main__':
    app.run(debug=True)