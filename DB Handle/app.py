import sqlite3


class TableModel:
    def __init__(self, table_id, x, y, rotation):
        self.table_id = table_id
        self.x = x
        self.y = y
        self.rotation = rotation


def insert_table(x, y, rotation):
    sql_connection = sqlite3.connect('tabledb.db')
    cursor = sql_connection.cursor()
    db_table_name = "tables_position"
    sql_insert_query = "INSERT INTO " + db_table_name + " (pos_x, pos_y, rotation) VALUES (" + \
        str(x) + ", " + str(y) + ", " + str(rotation) + ")"
    cursor.execute(sql_insert_query)
    sql_connection.commit()
    cursor.close()
    if sql_connection:
        sql_connection.close()


def update_table(id, x, y, rotation):
    sql_connection = sqlite3.connect('tabledb.db')
    cursor = sql_connection.cursor()
    db_table_name = "tables_position"
    sql_update_query = "UPDATE " + db_table_name + " set pos_x = " + str(x) + \
        ", pos_y = " + str(y) + ", rotation = " + str(rotation) + " where table_id = " + str(id)
    cursor.execute(sql_update_query)
    sql_connection.commit()
    cursor.close()
    if sql_connection:
        sql_connection.close()


def delete_table(id):
    sql_connection = sqlite3.connect('tabledb.db')
    cursor = sql_connection.cursor()
    db_table_name = "tables_position"
    sql_delete_query = "DELETE from " + db_table_name + " where table_id = " + str(id)
    cursor.execute(sql_delete_query)
    sql_connection.commit()
    cursor.close()
    if sql_connection:
        sql_connection.close()


def find_one(id):
    sql_connection = sqlite3.connect('tabledb.db')
    cursor = sql_connection.cursor()
    db_table_name = "tables_position"
    sql_find_one_query = "SELECT table_id, pos_x, pos_y, rotation FROM " + db_table_name + " where table_id = " \
        + str(id)
    cursor.execute(sql_find_one_query)
    find_table = cursor.fetchall()
    for row in find_table:
        table = TableModel(row[0], row[1], row[2], row[3])
    cursor.close()
    if sql_connection:
        sql_connection.close()
    return table


def find_all():
    table_list = []
    sql_connection = sqlite3.connect('tabledb.db')
    cursor = sql_connection.cursor()
    db_table_name = "tables_position"
    sql_find_all_query = "SELECT * FROM " + db_table_name
    cursor.execute(sql_find_all_query)
    find_table = cursor.fetchall()
    for row in find_table:
        table = TableModel(row[0], row[1], row[2], row[3])
        table_list.append(table)
    cursor.close()
    if sql_connection:
        sql_connection.close()
    return table_list

