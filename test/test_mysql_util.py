from unittest import TestCase
from util.mysql_util import MySQLUtil

class TestMySQLUtil(TestCase):
    def setUp(self) -> None:
        # setUp = __init__
        self.metadata_db = MySQLUtil()

    def test_query(self):
        self.metadata_db.query("CREATE DATABASE if not exists test CHARACTER SET utf8")
        self.metadata_db.select_db("test")
        self.metadata_db.check_table_exists_and_create(
            "test",
            "for_unit_test",
            "id int primary key, name varchar(255)"
        )
        self.metadata_db.execute("TRUNCATE for_unit_test")
        self.metadata_db.execute(
            "INSERT INTO for_unit_test VALUES(1, 'Lily'), (2, 'Lucy')"
        )
        result = self.metadata_db.query("SELECT * FROM for_unit_test ORDER BY id")
        expected = ((1, 'Lily'), (2, 'Lucy'))
        self.assertEqual(expected, result)
        # clean
        self.metadata_db.execute("DROP TABLE for_unit_test")
        self.metadata_db.execute("DROP DATABASE test")
        self.metadata_db.close_conn()

    def test_execute_without_autocommit(self):
        self.metadata_db.conn.autocommit(True)
        self.metadata_db.query("CREATE DATABASE if not exists test CHARACTER SET utf8")
        self.metadata_db.select_db("test")
        self.metadata_db.check_table_exists_and_create(
            "test",
            "for_unit_test",
            "id int primary key, name varchar(255)"
        )
        self.metadata_db.execute("TRUNCATE for_unit_test")
        self.metadata_db.execute_without_autocommit(
            "INSERT INTO for_unit_test VALUES(1, 'Lily')"
        )
        result = self.metadata_db.query("SELECT * FROM for_unit_test ORDER BY id")
        expected = ((1, 'Lily'), )
        self.assertEqual(expected, result)
        # clean
        self.metadata_db.close_conn()

        # set autocommit to False
        new_util = MySQLUtil()
        new_util.select_db("test")
        new_util.conn.autocommit(False)
        new_util.execute_without_autocommit(
            "INSERT INTO for_unit_test VALUES(2, 'Lucy')"
        )
        new_util.close_conn()

        new_util2 = MySQLUtil()
        new_util2.select_db("test")
        result = new_util2.query("SELECT * FROM for_unit_test ORDER BY id")
        expected = ((1, 'Lily'), )
        self.assertEqual(expected, result)

        # clean up
        new_util2.execute("DROP TABLE for_unit_test")
        new_util2.execute("DROP DATABASE test")
        new_util2.close_conn()