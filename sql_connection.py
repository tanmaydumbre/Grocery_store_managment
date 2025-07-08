import MySQLdb


__cnx = None

def get_connection():
    global __cnx
    if __cnx is None:
        __cnx = MySQLdb.connect(
            user='root',
            password='tanmay@14',
            host='127.0.0.1',
            db='grocery_store'
        )

    return __cnx

cnx = get_connection()
cursor = cnx.cursor()