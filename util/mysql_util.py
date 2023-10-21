"""
MySQL utility class
The provided functionalities include:
- Creating a MySQL connection
- Closing the connection
- Executing SQL queries and returning query results
- Creating tables
- Checking if a table exists
"""
# We need to maintain the connection (MySQL connection).
# The class has a member variable, which is the connection.
# As long as the object of the class is not destroyed, this connection can be used continuously after a successful connection.
# If you don't use a class and write it in a method, the connection object is disposable.
import pymysql
from config import project_config as conf
from util.logging_util import init_logger

logger = init_logger()

class MySQLUtil:
    def __init__(self):
        self.conn = pymysql.Connection(
            host=conf.metadata_host,
            user=conf.metadata_user,
            password=conf.metadata_password,
            port=conf.metadata_port,
            charset=conf.mysql_charset,
            autocommit=False  # When you execute SQL, need to call the .commit() method for it to take effect.
        )
        logger.info(f"Processing {conf.metadata_host}:{conf.metadata_port} database connection...")

    def close_conn(self):
        if self.conn:
            self.conn.close()

    def query(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        logger.info(f"The SQL query has been executed, and there is {len(result)} results")

        return result
