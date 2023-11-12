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
    def __init__(self,
                 host=conf.metadata_host,
                 user=conf.metadata_user,
                 password=conf.metadata_password,
                 port=conf.metadata_port,
                 charset=conf.mysql_charset,
                 autocommit=False):  # When you execute SQL, need to call the .commit() method for it to take effect.
        self.conn = pymysql.Connection(
            host=host,
            user=user,
            password=password,
            port=port,
            charset=charset,
            autocommit=autocommit
        )
        logger.info(f"Processing {host}:{port} database connection...")

    def close_conn(self):
        if self.conn:
            self.conn.close()

    def query(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        logger.info(f"The SQL query has been executed, and there is {len(result)} results.")

        return result

    def select_db(self, db):
        self.conn.select_db(db)

    def execute(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)

        logger.debug(f"execute with sql: {sql}")

        if not self.conn.get_autocommit():
            self.conn.commit()

    def execute_without_autocommit(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        logger.debug(f"execute with sql: {sql}")

    def check_table_exists(self, db_name, table_name):
        self.conn.select_db(db_name)
        result = self.query("SHOW TABLES")
        return (table_name,) in result

    def check_table_exists_and_create(self, db_name, table_name, create_clos):
        if not self.check_table_exists(db_name, table_name):
            create_sql = f"CREATE TABLE {table_name}({create_clos})"
            self.conn.select_db(db_name)
            self.execute(create_sql)

            logger.info(f"Create table: {table_name} to DB: {db_name}. SQL: {create_sql}.")
        else:
            logger.info(f"Table {table_name} exist in DB: {db_name}, skip create table.")


def get_processed_files(metadata_db,
                        db_name = conf.metadata_db_name,
                        table_name = conf.metadata_file_monitor_table_name,
                        create_cols = conf.metadata_file_monitor_table_create_cols):

    metadata_db.select_db(db_name)
    metadata_db.check_table_exists_and_create(
        db_name,
        table_name,
        create_cols
    )

    result = metadata_db.query(f"SELECT file_name FROM {table_name}")

    processed_files = []
    for r in result:
        processed_files.append(r[0])
    return processed_files
