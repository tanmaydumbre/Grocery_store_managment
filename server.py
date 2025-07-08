from flask import Flask,request, jsonify

app = Flask(__name__)

import product_dao
import orders_dao
import uom_dao
from sql_connection import get_connection
import json
connection = get_connection()

# Example route

@app.route('/getallproducts')
def hello():
    products = product_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/getUOM',methods=['GET'])
def get_unit():
    response=uom_dao.get_unit(())
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct',methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = product_dao.insert_product(connection,request_payload)
    response = jsonify({
        'product_id':product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder',methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = product_dao.insert_product(connection,request_payload)
    response = jsonify({
        'order_id':order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders',methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct',methods=['POST'])
def delete_product():
    return_id = product_dao.delete_product(connection,request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("starting python flask server")
    app.run(port=5000)


