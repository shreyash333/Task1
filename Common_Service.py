from cmath import log
from copy import error
from traceback import print_tb
import DB_Service
import file_log


# to remove the code redundancy these common functions are used by all three tables


# To delete record from a tabale
# It takes Table name, Table primary key attribute, ID
def delete_Data(table_id, table_attri, table_name):
    try:
        # deleting
        DB_Service.mainDB_Cursor.execute('DELETE FROM %s WHERE %s=%d' %
                                         (table_name, table_attri, table_id))
        DB_Service.mysqldb.commit()
        print('\n\t*****Record deteted successfully.*****')

        # logging
        log_message = ("Data Deleted from %s table where ID=%d " %
                       (table_name, table_id))
        file_log.logInfo("Common_Services.py", "delete_Data", log_message)

    # handling Exceptions
    except (DB_Service.mysqldb.Error, DB_Service.mysqldb.Warning, TypeError, ValueError) as e:
        DB_Service.mysqldb.rollback()
        print("\n\t*****Failed to delete record.*****")

        # logging
        log_message = ("Failed to delete data from %s table where ID=%d " %
                       (table_name, table_id))
        file_log.logError("Common_Services.py", "delete_Data", log_message, e)
    DB_Service.mysqldb.close()
    return True


# To read particular record from a table
# It takes Table name, Table primary key attribute, ID
def view_Data(table_id, table_attri, table_name):
    try:
        # reading
        DB_Service.mainDB_Cursor.execute('SELECT * from %s WHERE %s=%d' %
                                         (table_name, table_attri, table_id))
        result = DB_Service.mainDB_Cursor.fetchall()

        # logging
        log_message = ("Data readed from %s table where ID=%d " %
                       (table_name, table_id))
        file_log.logInfo("Common_Services.py", "view_Data", log_message)

    # handling Exceptions
    except (DB_Service.mysqldb.Error, DB_Service.mysqldb.Warning, TypeError, ValueError) as e:
        DB_Service.mysqldb.rollback()
        print('\n\t*****Unable to fetch data.*****')

        # logging
        log_message = ("Failed to read data from %s table where ID=%d " %
                       (table_name, table_id))
        file_log.logError("Common_Services.py", "view_Data", log_message, e)
    DB_Service.mysqldb.close()
    return list(result)


# To read all the record from a table
# It takes Table name
def view__All_Data(table_name):
    try:
        # reading
        DB_Service.mainDB_Cursor.execute('SELECT * from %s' % (table_name))
        result = DB_Service.mainDB_Cursor.fetchall()

        # logging
        log_message = ("Data readed from %s table" %
                       (table_name))
        file_log.logInfo("Common_Services.py", "view_All_Data", log_message)

    # handling Exceptions
    except (DB_Service.mysqldb.Error, DB_Service.mysqldb.Warning, TypeError, ValueError) as e:
        DB_Service.mysqldb.rollback()
        print('\n\t*****Unable to fetch data.*****')

        # logging
        log_message = ("Failed to read data from %s table " %
                       (table_name))
        file_log.logError("Common_Services.py",
                          "view_All_Data", log_message, e)
    DB_Service.mysqldb.close()
    return list(result)
