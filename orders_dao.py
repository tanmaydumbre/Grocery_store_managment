from sql_connection import get_connection
from datetime import datetime

# insert orders
def insert_order(connection, order):
    cursor = connection.cursor()

    query = ("INSERT INTO orders"
                   " (customer_name, total, datetime)"
                   " VALUES (%s, %s, %s)")

    values = (order['customer_name'], order['grand_total'], datetime.now())

    cursor.execute(query, values)
    connection.commit()  # Commit the transaction

    order_id = cursor.lastrowid
    return order_id

# insert order_details
def insert_order_details(connection, order_details):
    cursor = connection.cursor()

    query = ("INSERT INTO order_details"
                           " (order_id, product_id, quantity, total)"
                           " VALUES (%s, %s, %s, %s)")

    values = (order_details['order_id'],
                          order_details['product_id'],
                          order_details['quantity'],
                          order_details['total'])

    cursor.execute(query, values)
    connection.commit()

def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM orders")
    cursor.execute(query)

    response = []
    for (order_id,customer_name,total,datetime) in cursor:
        response.append({
            'order_id':order_id,
            'customer_name':customer_name,
            'total':total,
            'datetime':datetime
        })
    return response



if __name__ == '__main__':
    connection = get_connection()
    print(get_all_orders(connection))
