from logging import debug
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/copy')
def copy_page():

    return('copy your URL')

if __name__ =='__main__' :
    app.run(debug = True)