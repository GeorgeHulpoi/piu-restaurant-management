import sqlite3
from models.Table import Table

class TableRepository:
    dbFile = '../tabledb.db'
    tableName = 'tables_position'

    @staticmethod
    def find_by_id(id):
        result = None

        with TableRepository.__create_connection() as conn:
            with conn.cursor() as cursor:
                sql = "SELECT table_id, pos_x, pos_y, rotation FROM " + TableRepository.tableName + " where table_id = " \
                             + str(id)
                cursor.execute(sql)
                row = cursor.fetchone()
                result = Table(row[0], row[1], row[2], row[3])

        return result

    @staticmethod
    def find_all():
        result = []

        with TableRepository.__create_connection() as conn:
            with conn.cursor() as cursor:
                sql = "SELECT table_id, pos_x, pos_y, rotation FROM " + TableRepository.tableName + " where table_id = " \
                      + str(id)
                cursor.execute(sql)
                rows = cursor.fetchall()
                result = list(map(lambda r: Table(r[0], r[1], r[2], r[3]), rows))

        return result

    @staticmethod
    def update(table):
        with TableRepository.__create_connection() as conn:
            with conn.cursor() as cursor:
                sql = "UPDATE " + TableRepository.tableName + " " + "" \
                      "SET pos_x = " + str(table.getX()) + ", " + \
                      "pos_y = " + str(table.getY()) + ", " + \
                      "rotation = " + str(table.getRotation()) + " " + \
                      "WHERE table_id = " + str(table.getId())
                cursor.execute(sql)
                conn.commit()

    @staticmethod
    def __create_connection():
        conn = None
        try:
            conn = sqlite3.connect(TableRepository.dbFile)
        except sqlite3.Error as e:
            print(e)

        return conn
