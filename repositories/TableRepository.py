import sqlite3
from models.Table import Table, TableType


class TableRepository:
    dbFile = 'tabledb.db'
    tableName = 'tables_position'

    @staticmethod
    def find_by_id(id):
        result = None

        with TableRepository.__create_connection() as conn:
            cursor = conn.cursor()
            sql = "SELECT id, pos_x, pos_y, rotation, type " \
                  "FROM " + TableRepository.tableName + " " + \
                  "WHERE id = " + str(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            result = Table(row[0], row[1], row[2], row[3], TableType(int(row[4])))
            cursor.close()

        return result

    @staticmethod
    def find_all():
        result = []

        with TableRepository.__create_connection() as conn:
            cursor = conn.cursor()
            sql = "SELECT id, pos_x, pos_y, rotation, type " \
                  "FROM " + TableRepository.tableName

            cursor.execute(sql)
            rows = cursor.fetchall()
            result = list(map(lambda r: Table(int(r[0]), r[1], r[2], r[3], TableType(r[4])), rows))
            cursor.close()

        return result

    @staticmethod
    def update(table):
        with TableRepository.__create_connection() as conn:
            cursor = conn.cursor()
            sql = "UPDATE " + TableRepository.tableName + " " \
                  "SET pos_x = " + str(table.getX()) + ", " + \
                  "pos_y = " + str(table.getY()) + ", " + \
                  "rotation = " + str(table.getRotation()) + ", " + \
                  "type = " + str(table.getType().value) + " " \
                  "WHERE id = " + str(table.getId())
            cursor.execute(sql)
            conn.commit()
            cursor.close()

    @staticmethod
    def create(x, y, rotation, type):
        id = None
        with TableRepository.__create_connection() as conn:
            cursor = conn.cursor()
            sql = "INSERT INTO " + TableRepository.tableName + " " \
                  "VALUES (NULL," + str(x) + "," + str(y) + "," + str(rotation) + \
                        "," + str(type.value) + ")"
            cursor.execute(sql)
            conn.commit()
            id = cursor.lastrowid
            cursor.close()
        return Table(id, x, y, rotation, type)

    @staticmethod
    def deleteById(id):
        if not isinstance(id, int):
            raise Exception('deleteById: id should be int!')

        with TableRepository.__create_connection() as conn:
            cursor = conn.cursor()
            sql = "DELETE FROM " + TableRepository.tableName + " " \
                "WHERE id = " + str(id)
            cursor.execute(sql)
            conn.commit()
            cursor.close()

    @staticmethod
    def __create_connection():
        conn = None
        try:
            conn = sqlite3.connect(TableRepository.dbFile)
        except sqlite3.Error as e:
            print(e)

        return conn
