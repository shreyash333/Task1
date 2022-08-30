
import DB


def insert_Data(off_Name, off_Address):
    print("")
    try:
        DB.mainDB_Cursor.execute("SELECT * from Office")
        result = DB.mainDB_Cursor.fetchall()
        off_ID = len(result)+1
        DB.mainDB_Cursor.execute(
            'INSERT into Office values(%d, "%s" , "%s")' % (off_ID, off_Name, off_Address))
        DB.mysqldb.commit()
        print('Record inserted successfully...')
    except:
        print("Failed to insert record...")
    DB.mysqldb.close()
    return True


def update_Data(off_ID, off_Name, off_Address):
    try:
        DB.mainDB_Cursor.execute('UPDATE Office SET Office_Name="%s",Office_Address="%s"  WHERE Office_ID=%d' % (
            off_Name, off_Address, off_ID))
        DB.mysqldb.commit()
        print('Record updated successfully...')
    except:
        print("Failed to update record...")
    DB.mysqldb.close()
    return True
