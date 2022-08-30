
import DB


def insert_Data(tech_Name):
    try:
        DB.mainDB_Cursor.execute("SELECT * from Technology")
        result = DB.mainDB_Cursor.fetchall()
        tech_ID = len(result)+1
        DB.mainDB_Cursor.execute(
            'INSERT into Technology values(%d, "%s")' % (tech_ID, tech_Name))
        DB.mysqldb.commit()
        print('Record inserted successfully...')
    except:
        print("Failed to insert record...")
    DB.mysqldb.close()
    return True


def update_Data(tech_ID, tech_Name):
    try:
        DB.mainDB_Cursor.execute('UPDATE Technology SET Technology_Name="%s"  WHERE Technology_ID=%d' % (
            tech_Name, tech_ID))
        DB.mysqldb.commit()
        print('Record updated successfully...')
    except:
        print("Failed to update record...")
    DB.mysqldb.close()
    return True
