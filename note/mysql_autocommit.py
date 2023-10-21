import pymysql
conn = pymysql.Connection(
    host="localhost",
    user="root",
    password="Shanjun@007",
    port=3306,
    charset="utf8",
    autocommit=True
)
conn.select_db("etl_python")
cursor = conn.cursor()
cursor.execute("INSERT INTO etl_demo(id, name, dage_id) VALUES(1, 'Ammander', 18)")