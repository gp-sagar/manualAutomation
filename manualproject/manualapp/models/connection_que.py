from django.db import MySQLdb

db_username = 'root',
db_password = 'root',
# db_HOST = '127.0.0.1',
database_inst_name =  '3306',
    
    
def get_db_connection():
    try:
        db_bill = MySQLdb.connect(
            database_inst_name,
            db_username, db_password)
        # db_bill = MySQLdb.connect("localhost", "root", "root")
        cursor = db_bill.cursor(MySQLdb.cursors.DictCursor)
        return cursor, db_bill
    except (MySQLdb, Exception) as e:
        traceback.print_exc()


class DB:
    conn = None

    def connect(self):
        self.conn = MySQLdb.connect(
            database_inst_name,
            db_username, db_password, "db_wal")

    def query(self, sql):
        try:
            cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(sql)
        except (AttributeError, MySQLdb.OperationalError):
            self.connect()
            cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(sql)
        return cursor