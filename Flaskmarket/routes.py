from Flaskmarket import app
from flask import render_template
from Flaskmarket.models import Items

@app.route('/market')
def market():
    item = Items.query.all()
    return render_template('market.html',items=item)

@app.route('/')
def home():
    return render_template('home.html')