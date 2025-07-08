from sql_connection import get_connection


def get_unit(connecion):
    cursor=connecion.cursor()
    cursor.execute('SELECT * FROM unit')
    response=[]
    for (uom_id,uom_name) in cursor:
        response.append({
            'uom_id':uom_id,
            'uom_name':uom_name
        })
    return response


if __name__ == '__main__':

    connection = get_connection()
    print(get_unit(connection))