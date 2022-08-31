from cmath import log
from copy import error
from traceback import print_tb
import DB_Service
import file_log


def delete_Data(table_id, table_attri, table_name):
    try:
        DB_Service.mainDB_Cursor.execute('DELETE FROM %s WHERE %s=%d' %
                                         (table_name, table_attri, table_id))
        DB_Service.mysqldb.commit()
        print('Record deteted successfully...')
        log_message = ("Data Deleted from %s table where ID=%d " %
                       (table_name, table_id))
        file_log.logInfo("Common_Services.py", "delete_Data", log_message)
    except (DB_Service.mysqldb.Error, DB_Service.mysqldb.Warning, TypeError, ValueError) as e:
        DB_Service.mysqldb.rollback()
        print("Failed to delete record...")
        log_message = ("Failed to delete data from %s table where ID=%d " %
                       (table_name, table_id))
        file_log.logError("Common_Services.py", "delete_Data", log_message, e)
    DB_Service.mysqldb.close()
    return True


def view_Data(table_id, table_attri, table_name):
    try:
        DB_Service.mainDB_Cursor.execute('SELECT * from %s WHERE %s=%d' %
                                         (table_name, table_attri, table_id))
        result = DB_Service.mainDB_Cursor.fetchall()
        log_message = ("Data readed from %s table where ID=%d " %
                       (table_name, table_id))
        file_log.logInfo("Common_Services.py", "view_Data", log_message)
    except (DB_Service.mysqldb.Error, DB_Service.mysqldb.Warning, TypeError, ValueError) as e:
        DB_Service.mysqldb.rollback()
        print('Error:Unable to fetch data.')
        log_message = ("Failed to read data from %s table where ID=%d " %
                       (table_name, table_id))
        file_log.logError("Common_Services.py", "view_Data", log_message, e)
    DB_Service.mysqldb.close()
    return list(result)


def view__All_Data(table_name):
    try:
        DB_Service.mainDB_Cursor.execute('SELECT * from %s' % (table_name))
        result = DB_Service.mainDB_Cursor.fetchall()
        log_message = ("Data readed from %s table" %
                       (table_name))
        file_log.logInfo("Common_Services.py", "view_All_Data", log_message)
    except (DB_Service.mysqldb.Error, DB_Service.mysqldb.Warning, TypeError, ValueError) as e:
        DB_Service.mysqldb.rollback()
        print('Error:Unable to fetch data.')
        log_message = ("Failed to read data from %s table " %
                       (table_name))
        file_log.logError("Common_Services.py",
                          "view_All_Data", log_message, e)
    DB_Service.mysqldb.close()
    return list(result)
