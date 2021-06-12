from logging import debug
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import string, random

app = Flask(__name__)

db= SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

class Url_Model(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    long = db.Column(db.String())
    short = db.Column(db.String(3))

    def __init__(self, short, long ):
        self.short = short
        self.long = long
@app.route('/short')
def shortern_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=3 )
        rand_letters = "".join(rand_letters)
        short_url = Url_Model.query.filter_by(short= rand_letters).first()
        if not short_url:
            return rand_letters

@app.route('/', methods= ['POST', 'GET'])
def home():
    if request.method =='POST':
        url_recieved = request.form['nm'] 
        url_avaliable = Url_Model.query.filter_by(long=url_recieved).first()
        if url_avaliable:
            return redirect(url_for('display_short_url', url= url_avaliable.short))
        else:
            #creating new url if short url not found
            short_url = shortern_url()
            new_url= Url_Model(url_recieved,short_url)
            db.session.add(new_url)
            db.session.commit()
            return short_url
    else:
        return render_template('home.html')
@app.route('/copy')
def copy_page():

    return('copy your URL')

if __name__ =='__main__' :
    app.run(debug = True)