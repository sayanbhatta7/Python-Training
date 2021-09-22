from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1> Hello world </h1>'

#dynamic route
@app.route('/user/<name>')
def user(name):
    return '<h1> hello %s!</h1>' %name

#headers
@app.route("/headers")
def headers():
    user_a= request.headers.get('User-Agent')
    return '<p> your browser is %s</p>' %user_a

if __name__=='__main__':
    app.run(debug=True)