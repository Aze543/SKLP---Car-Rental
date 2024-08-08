from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = "jwqdhgdigdqhg43%^dshighdjgdjghijh12345@$4dqjh$*90h"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rent')
def car_list():
    return render_template('list.html')

@app.route('/car-details')
def car_details():
    return '<h1>Refridgator</h1><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJSudXYuY7T-mmea-LeuKBBxDiihBaNcmbug&s" alt="..." />'


if __name__ == "__main__":
    app.run(debug=True)