
import DB_Service
import file_log


def insert_Data(tech_Name):
    try:
        DB_Service.mainDB_Cursor.execute(
            'INSERT into Technology (Technology_Name) values( "%s")' % (tech_Name))
        DB_Service.mysqldb.commit()
        print('\n\t*****Record inserted successfully.*****')
        log_message = ("Data inserted to Technology table")
        file_log.logInfo("Technology_Services.py", "insert_Data", log_message)
    except (DB_Service.mysqldb.Error, DB_Service.mysqldb.Warning, TypeError, ValueError) as e:
        DB_Service.mysqldb.rollback()
        print("\n\t*****Failed to insert record.*****")
        log_message = ("Failed to insert data in Technology table")
        file_log.logError("Technology_Services.py",
                          "insert_Data", log_message, e)
    DB_Service.mysqldb.close()
    return True


def update_Data(tech_ID, tech_Name):
    try:
        DB_Service.mainDB_Cursor.execute('UPDATE Technology SET Technology_Name="%s"  WHERE Technology_ID=%d' % (
            tech_Name, tech_ID))
        DB_Service.mysqldb.commit()
        print('\n\t*****Record updated successfully.*****')
        log_message = (
            "Data updated in Technology table where ID=%d" % (tech_ID))
        file_log.logInfo("Technology_Services.py", "update_Data", log_message)
    except (DB_Service.mysqldb.Error, DB_Service.mysqldb.Warning, TypeError, ValueError) as e:
        DB_Service.mysqldb.rollback()
        print("\n\t*****Failed to update record.*****")
        log_message = (
            "Failed to update data in Technology table where ID=%d" % (tech_ID))
        file_log.logError("Technology_Services.py",
                          "update_Data", log_message, e)
    DB_Service.mysqldb.close()
    return True
