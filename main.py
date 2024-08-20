from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from functions import dynamic_date

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = "jwqdhgdigdqhg43%^dshighdjgdjghijh12345@$4dqjh$*90h"


@app.route('/')
def home():
    year = dynamic_date()
    return render_template('index.html', year=year)

@app.route('/rent')
def car_list():
    year = dynamic_date()
    return render_template('list.html', year=year)

@app.route('/car-details')
def car_details():
    return render_template('details.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)