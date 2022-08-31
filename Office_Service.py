
import DB_Service
import file_log


# It addes recrord to Office table
def insert_Data(off_Name, off_Address):
    try:
        # inserting
        DB_Service.mainDB_Cursor.execute(
            'INSERT into Office (Office_Name, Office_Address) values( "%s" , "%s")' % (off_Name, off_Address))
        DB_Service.mysqldb.commit()
        print('\n\t*****Record inserted successfully.*****')

        # logging
        log_message = ("Data inserted to Office table")
        file_log.logInfo("Office_Services.py", "insert_Data", log_message)

    # handling Exceptions
    except (DB_Service.mysqldb.Error, DB_Service.mysqldb.Warning, TypeError, ValueError) as e:
        DB_Service.mysqldb.rollback()
        print("\n\t*****Failed to insert record.*****")

        # logging
        log_message = ("Failed to insert data in Office table")
        file_log.logError("Office_Services.py",
                          "insert_Data", log_message, e)
    DB_Service.mysqldb.close()
    return True


# It update a record in Office table
def update_Data(off_ID, off_Name, off_Address):
    try:
        # updating
        DB_Service.mainDB_Cursor.execute('UPDATE Office SET Office_Name="%s",Office_Address="%s"  WHERE Office_ID=%d' % (
            off_Name, off_Address, off_ID))
        DB_Service.mysqldb.commit()
        print('\n\t*****Record updated successfully.*****')

        # logging
        log_message = ("Data updated in Office table where ID=%d" % (off_ID))
        file_log.logInfo("Office_Services.py", "update_Data", log_message)

    # handling Exceptions
    except (DB_Service.mysqldb.Error, DB_Service.mysqldb.Warning, TypeError, ValueError) as e:
        DB_Service.mysqldb.rollback()
        print("\n\t*****Failed to update record.*****")

        # logging
        log_message = (
            "Failed to update data in Office table where ID=%d" % (off_ID))
        file_log.logError("Office_Services.py",
                          "update_Data", log_message, e)
    DB_Service.mysqldb.close()
    return True
