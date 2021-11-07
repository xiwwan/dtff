import pymysql

def mysql_connect_db(host='localhost', user='root', password='', db='College'):
    # To connect MySQL database
    conn = pymysql.connect(
        host = host,
        user = user,
        password = password,
        db = db
    )
    print(conn)
    return  conn

def mysql_connect(host='localhost', user='root', password=''):
    # To connect MySQL database
    conn = pymysql.connect(
        host = host,
        user = user,
        password = password
    )
    print(conn)
    return  conn

# Driver Code
if __name__ == "__main__":
    conn = mysql_connect()
    # To close the connection
    conn.close()