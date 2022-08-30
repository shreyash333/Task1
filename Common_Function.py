import DB


def delete_Data(table_id, table_attri, table_name):
    try:
        DB.mainDB_Cursor.execute('DELETE FROM %s WHERE %s=%d' %
                                 (table_name, table_attri, table_id))
        DB.mysqldb.commit()
        print('Record deteted successfully...')
    except:
        print("Failed to delete record...")
    DB.mysqldb.close()
    return True


def view_Data(table_id, table_attri, table_name):
    try:
        DB.mainDB_Cursor.execute('SELECT * from %s WHERE %s=%d' %
                                 (table_name, table_attri, table_id))
        result = DB.mainDB_Cursor.fetchall()
    except:
        print('Error:Unable to fetch data.')
    DB.mysqldb.close()
    return list(result)


def view__All_Data(table_name):
    try:
        DB.mainDB_Cursor.execute('SELECT * from %s' % (table_name))
        result = DB.mainDB_Cursor.fetchall()
    except:
        print('Error:Unable to fetch data.')
    DB.mysqldb.close()
    return list(result)
