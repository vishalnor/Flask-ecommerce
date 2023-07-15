import os
from flask import Flask,render_template
# from models import Item

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password123@localhost/marketdb'


@app.route('/market')
def market():
    item = [
        {"id":1, "name":"vita marie", "barcode":10202020, "price":500},
        {"id":1, "name":"Born borm", "barcode":10202020, "price":500},
        {"id":1, "name":"Oreo", "barcode":10202020, "price":500}
    ]
    # db = SQLAlchemy(app)
    # db.create_all(item)
    return render_template('market.html',items=item)

@app.route('/')
def home():
    return render_template('home.html')
# nor
# bhavin
# vishal
# db.create_all()
if __name__ =='__main__':
    app.run(debug=True)