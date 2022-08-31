
import DB_Service
import file_log


def insert_Data(off_Name, off_Address):
    try:
        DB_Service.mainDB_Cursor.execute(
            'INSERT into Office (Office_Name, Office_Address) values( "%s" , "%s")' % (off_Name, off_Address))
        DB_Service.mysqldb.commit()
        print('Record inserted successfully...')
        log_message = ("Data inserted to Office table")
        file_log.logInfo("Office_Services.py", "insert_Data", log_message)
    except (DB_Service.mysqldb.Error, DB_Service.mysqldb.Warning, TypeError, ValueError) as e:
        DB_Service.mysqldb.rollback()
        print("Failed to insert record...")
        log_message = ("Failed to insert data in Office table")
        file_log.logError("Office_Services.py",
                          "insert_Data", log_message, e)
    DB_Service.mysqldb.close()
    return True


def update_Data(off_ID, off_Name, off_Address):
    try:
        DB_Service.mainDB_Cursor.execute('UPDATE Office SET Office_Name="%s",Office_Address="%s"  WHERE Office_ID=%d' % (
            off_Name, off_Address, off_ID))
        DB_Service.mysqldb.commit()
        print('Record updated successfully...')
        log_message = ("Data updated in Office table where ID=%d" % (off_ID))
        file_log.logInfo("Office_Services.py", "update_Data", log_message)
    except (DB_Service.mysqldb.Error, DB_Service.mysqldb.Warning, TypeError, ValueError) as e:
        DB_Service.mysqldb.rollback()
        print("Failed to update record...")
        log_message = (
            "Failed to update data in Office table where ID=%d" % (off_ID))
        file_log.logError("Office_Services.py",
                          "update_Data", log_message, e)
    DB_Service.mysqldb.close()
    return True
