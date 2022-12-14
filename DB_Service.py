import mysql.connector
import file_log

# main DB
mysqldb = mysql.connector.connect(
    host="localhost", user="root", password="123456", database="TCS", auth_plugin='mysql_native_password')
mainDB_Cursor = mysqldb.cursor()

# Backup DB
mysqldb1 = mysql.connector.connect(
    host="localhost", user="root", password="123456", database="TCS_Backup", auth_plugin='mysql_native_password')
backupDB_Cursor = mysqldb1.cursor()


# It copy the current main DB to Backup DB
def backup_Data():
    # getting tables of main DB
    mainDB_Cursor.execute('SHOW TABLES;')
    mainDB_table_names = []
    for record in mainDB_Cursor.fetchall():
        mainDB_table_names.append(record[0])

    # getting tables of backup
    backupDB_Cursor.execute('SHOW TABLES;')
    backupDB_table_names = []
    for record in backupDB_Cursor.fetchall():
        backupDB_table_names.append(record[0])

    try:
        # copying data
        for table_name in mainDB_table_names:
            if table_name in backupDB_table_names:
                backupDB_Cursor.execute('DROP Table %s' % (table_name))
            backupDB_Cursor.execute(
                f'CREATE TABLE {table_name} SELECT * FROM TCS.{table_name}')
        print("\n\t*****Data Backup Successfully.*****")

        # logging
        log_message = ("Data Backup completed successfully")
        file_log.logInfo("DB_Service.py",
                         "backup_Data", log_message)

    # handling Exceptions
    except (mysqldb1.Error, mysqldb1.Warning, TypeError, ValueError) as e:
        print("\n\t*****Failed to Backup data.*****")

        # logging
        log_message = ("Failed to backup data")
        file_log.logError("DB_Service.py",
                          "backup_Data", log_message, e)
    return True


# It copy th ebackup DB to current main DB
def recover_Data():
    # getting tables of main DB
    mainDB_Cursor.execute('SHOW TABLES;')
    mainDB_table_names = []
    for record in mainDB_Cursor.fetchall():
        mainDB_table_names.append(record[0])

    # getting tables of backup
    backupDB_Cursor.execute('SHOW TABLES;')
    backupDB_table_names = []
    for record in backupDB_Cursor.fetchall():
        backupDB_table_names.append(record[0])

    try:
        # copying data
        for table_name in backupDB_table_names:
            if table_name in mainDB_table_names:
                mainDB_Cursor.execute('DROP Table %s' % (table_name))
            mainDB_Cursor.execute(
                f'CREATE TABLE {table_name} SELECT * FROM TCS_Backup.{table_name}')
        print("\n\t*****Data Recovered Successfully.*****")

        # logging
        log_message = ("Data Recover completed successfully from backup")
        file_log.logInfo("DB_Service.py",
                         "recover_Data", log_message)

    # handling Exceptions
    except (mysqldb1.Error, mysqldb1.Warning, TypeError, ValueError) as e:
        print("\n\t*****Failed to Recover data.*****")

        # logging
        log_message = ("Failed to recover data from backup")
        file_log.logError("DB_Service.py",
                          "recover_Data", log_message, e)
    return True
