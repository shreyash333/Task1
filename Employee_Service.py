
import DB


def insert_Data(emp_Name, emp_Designation, emp_Salary, emp_DOB, emp_TechStack):
    try:
        DB.mainDB_Cursor.execute(
            'SELECT * from Technology WHERE Technology_ID=%d' % (emp_TechStack))
        techstack_exist = DB.mainDB_Cursor.fetchall()
        if (len(techstack_exist) == 0):
            print("Invalid TechStack entered")
            return True
        else:
            DB.mainDB_Cursor.execute("SELECT * from Employee")
            result = DB.mainDB_Cursor.fetchall()
            emp_ID = len(result)+1
            DB.mainDB_Cursor.execute(
                'INSERT into Employee values(%d, "%s" , "%s", %d, "%s", %d)' % (emp_ID, emp_Name, emp_Designation, emp_Salary, emp_DOB, emp_TechStack))
            DB.mysqldb.commit()
            print('Record inserted successfully...')
    except (DB.mysqldb.Error, DB.mysqldb.Warning, TypeError, ValueError, IndexError) as e:
        print("Failed to insert record...")
    DB.mysqldb.close()
    return True


def update_Data(emp_ID, emp_Name, emp_Designation, emp_Salary, emp_DOB, emp_TechStack):
    try:
        DB.mainDB_Cursor.execute('UPDATE Employee SET Name="%s",Designation="%s", Salary=%d, DOB="%s", TechStack=%d  WHERE Employee_ID=%d' % (
            emp_Name, emp_Designation, emp_Salary, emp_DOB, emp_TechStack, emp_ID))
        DB.mysqldb.commit()
        print('Record updated successfully...')
    except:
        print("Failed to update record...")
    DB.mysqldb.close()
    return True
