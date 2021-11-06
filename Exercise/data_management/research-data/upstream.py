from connect import mysql_connect, mysql_connect_db

def init_database(databasename='fx'):
    # create database if not exists
    conn = mysql_connect()
    cur = conn.cursor()
    try:
        cur.execute(f"CREATE DATABASE {databasename}")
        print(cur.fetchall())
    except Exception as e:
        print(e)
    conn.close()

def init_tables():
    conn = mysql_connect_db(db="fx")
    cur = conn.cursor()
    # create table if not exists
    try:
        cur.execute('''CREATE TABLE fx.currency (
                        id INT,
                        name VARCHAR(255),
                        iso_3 VARCHAR(255)
                    )''')
    except Exception as e:
        print(e)

    try:
        cur.execute('''CREATE TABLE fx.data_type (
                        id INT,
                        description VARCHAR(255)
                    )''')
    except Exception as e:
        print(e)

    try:
        cur.execute('''CREATE TABLE fx.timeseries_data (
                        id INT,
                        base_id INT,
                        counter_id INT,
                        data_type_id INT,
                        date VARCHAR(255),
                        value NUMERIC(10,5)
                    )''')
    except Exception as e:
        print(e)
    conn.close()

if __name__ == "__main__":
    init_database()
    init_tables()
    # downstream
    conn = mysql_connect()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO fx.currency
            (id, name, iso_3)
        VALUES
            (1,	'australian dollar', 'aud'),
            (2,	'swiss franc',       'chf'),
            (3,	'us dollar',    	 'usd')
    """)
    cur.execute("""
        INSERT INTO fx.data_type
            (id, description)
        VALUES
            (1, 'spot price'),
            (2, 'foward price, 1m')
        """)
    cur.execute(
        """
        INSERT INTO fx.timeseries_data
            (id, base_id, counter_id, data_type_id, date, value)
        VALUES
            (1,	1,	3,	1,	'2021-01-05',	0.1361),
            (2,	1,	3,	1,	'2021-01-06',	0.4488),
            (3,	3,	2,	2,	'2021-01-05',	0.6185)
        """)
    conn.commit()
    conn.close()