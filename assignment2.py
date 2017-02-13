from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add/<int:x>/<int:y>')
def add(x, y):
    return str(x+y)

@app.route('/sub/<int:x>/<int:y>')
def sub(x,y):
    return str(x-y)

@app.route('/mul/<int:x>/<int:y>')
def mul(x,y):
    return str(x*y)

@app.route('/favoritefoods')
def mylist():
    mylist= ['curry', 'lentills', 'beans', 'veggies']
    return jsonify(mylist)
