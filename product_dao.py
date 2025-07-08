from sql_connection import get_connection

def get_all_products(connection):

    cursor = connection.cursor()
    query = ("SELECT product_id,name,products.uom_id,price_per_unit, unit.uom_name FROM products inner join unit on unit.uom_id=products.uom_id")
    cursor.execute(query)
    response=[]
    for (product_id,name,uom_id,price_per_unit,uom_name) in cursor:
        response.append({
            'product_id':product_id,
            'name':name,
            'uom_id':uom_id,
            'price_per_unit':price_per_unit,
            'unit name':uom_name
        })
    return response

def insert_product(connection,product):
    cursor=connection.cursor()

    cursor.execute('INSERT INTO products (name, uom_id, price_per_unit) VALUES (%s,%s,%s)',
                   (product['product_name'],product['uom_id'],product['price_per_unit'])
                   )
    connection.commit()
    return product

def delete_product(connection,product_id):
    cursor=connection.cursor()
    cursor.execute('DELETE from products where product_id='+ str(product_id))
    connection.commit()
    return product_id

if __name__ == '__main__':
    connection = get_connection()
    print(get_all_products(connection))
    # print(insert_product(connection,{
    #     'product_name':'chips',
    #     'uom_id':'1',
    #     'price_per_unit':'10'
    # }))
    # print(delete_product(connection,20))