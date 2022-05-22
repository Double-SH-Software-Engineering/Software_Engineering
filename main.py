from flask import Flask, render_template
from datetime import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root',password='!9535010a',host='localhost')
cursor = cnx.cursor()
cursor.execute("USE market")

def product_detail(product_id):
    product = []
    query = "select * from product where product_id=" + str(product_id) 
    cursor.execute(query)
    for c in cursor:
        product = c
    return product
        

app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/product/before/<int:id>')
def product_login(id):
    product = product_detail(id)
    return render_template('Product_login.html',result=product)

@app.route('/product/after/<int:id>')
def product(id):
    product = product_detail(id)
    return render_template('Product.html',result=product)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)



