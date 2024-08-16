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
    return render_template('details.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)