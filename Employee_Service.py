
import DB_Service
import file_log


def insert_Data(emp_Name, emp_Designation, emp_Salary, emp_DOB, emp_TechStack):
    try:
        DB_Service.mainDB_Cursor.execute(
            'SELECT * from Technology WHERE Technology_ID=%d' % (emp_TechStack))
        techstack_exist = DB_Service.mainDB_Cursor.fetchall()
        if (len(techstack_exist) == 0):
            print("Invalid TechStack entered")
            return True
        else:
            DB_Service.mainDB_Cursor.execute(
                'INSERT into Employee (Name, Designation, Salary, DOB, TechStack) values( "%s" , "%s", %d, "%s", %d)' % (emp_Name, emp_Designation, emp_Salary, emp_DOB, emp_TechStack))
            DB_Service.mysqldb.commit()
            print('Record inserted successfully...')
            log_message = ("Data inserted to Employee table")
            file_log.logInfo("Employee_Services.py",
                             "insert_Data", log_message)
    except (DB_Service.mysqldb.Error, DB_Service.mysqldb.Warning, TypeError, ValueError) as e:
        DB_Service.mysqldb.rollback()
        print("Failed to insert record...")
        log_message = ("Failed to insert data in Employee table")
        file_log.logError("Employee_Services.py",
                          "insert_Data", log_message, e)
    DB_Service.mysqldb.close()
    return True


def update_Data(emp_ID, emp_Name, emp_Designation, emp_Salary, emp_DOB, emp_TechStack):
    try:
        DB_Service.mainDB_Cursor.execute('UPDATE Employee SET Name="%s",Designation="%s", Salary=%d, DOB="%s", TechStack=%d  WHERE Employee_ID=%d' % (
            emp_Name, emp_Designation, emp_Salary, emp_DOB, emp_TechStack, emp_ID))
        DB_Service.mysqldb.commit()
        print('Record updated successfully...')
        log_message = ("Data updated in Employee table where ID=%d" % (emp_ID))
        file_log.logInfo("Employee_Services.py", "update_Data", log_message)
    except (DB_Service.mysqldb.Error, DB_Service.mysqldb.Warning, TypeError, ValueError) as e:
        DB_Service.mysqldb.rollback()
        print("Failed to update record...")
        log_message = (
            "Failed to update data in Employee table where ID=%d" % (emp_ID))
        file_log.logError("Employee_Services.py",
                          "update_Data", log_message, e)
    DB_Service.mysqldb.close()
    return True
