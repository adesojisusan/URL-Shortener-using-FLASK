from logging import debug
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


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
@app.route()
def shortern_url():
    return "abcd"


@app.route('/', methods= ['POST', 'GET'])
def home():
    if request.method =='POST':
        url_recieved = request.form['nm']
        
        url_avaliable = Url_Model.query.fliter_by(long=url_recieved).first()
        if url_avaliable:
            return redirect(url_for('display_short_url', url= url_avaliable.short))
        return url_recieved
    else:
        return render_template('home.html')
@app.route('/copy')
def copy_page():

    return('copy your URL')

if __name__ =='__main__' :
    app.run(debug = True)