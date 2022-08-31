import Common_Service
import Office_Service
import Employee_Service
import DB_Service
import Technology_Service


# It contains Technology Service Menu and functions
def technology_functions():
    # Technology Menu
    n = int(input(
        "\n(Technology) Select a option from below : \n\t1.Add new Technology \n\t2.Delete a Technology \n\t3.Update a Technology \n\t4.View Technology \n\t5.View All Technology \nEnter the action Number : "))

    # case 1
    # Add new Technology
    if n == 1:
        s = input(
            "\nEnter the Technology \n")
        Technology_Service.insert_Data(s)

    # case 2
    # Delete a Technology
    elif n == 2:
        id = int(input("\nEnter the Technology ID : "))
        Common_Service.delete_Data(id, "Technology_ID", "Technology")

    # case 3
    # Update a Technology
    elif n == 3:
        id = int(input("\nEnter the Technology ID : "))
        s = input(
            "\nEnter the Technology \n")
        Technology_Service.update_Data(id, s)

    # case 4
    # View Technology
    elif n == 4:
        id = int(input("\nEnter the Technology ID : "))
        result = Common_Service.view_Data(id, "Technology_ID", "Technology")
        print("\t".join(map(str, result[0])))

    # case 5
    # View All Technology
    elif n == 5:
        result = Common_Service.view__All_Data("Technology")
        for i in result:
            print("\t".join(map(str, i)))

    # default case
    else:
        print("\nInvalid Input")


# It contains Office Service Menu and functions
def office_functions():
    # Office Menu
    n = int(input(
        "\n(Office) Select a option from below : \n\t1.Add new Office \n\t2.Delete a Office \n\t3.Update a office \n\t4.View Office \n\t5.View All Offices \nEnter the action Number : "))

    # case 1
    # Add new Office
    if n == 1:
        s = input(
            "\nEnter the data as - office name | office Address *(use | as seperator)* \n")
        x = s.split("|")
        for i in range(0, len(x)):
            x[i] = x[i].strip()
        Office_Service.insert_Data(x[0], x[1])

    # case 2
    # Delete a Office
    elif n == 2:
        id = int(input("\nEnter the Office ID : "))
        Common_Service.delete_Data(id, "Office_ID", "Office")

    # case 3
    # Update a office
    elif n == 3:
        id = int(input("\nEnter the Office ID : "))
        s = input(
            "\nEnter the updated value as - office name | office Address *(use | as seperator)* \n")
        x = s.split("|")
        for i in range(0, len(x)):
            x[i] = x[i].strip()
        Office_Service.update_Data(id, x[0], x[1])

    # case 4
    # View Offices
    elif n == 4:
        id = int(input("\nEnter the Office ID : "))
        result = Common_Service.view_Data(id, "Office_ID", "Office")
        print("\t".join(map(str, result[0])))

    # case 5
    # View All Offices
    elif n == 5:
        result = Common_Service.view__All_Data("Office")
        for i in result:
            print("\t".join(map(str, i)))

    # default case
    else:
        print("\nInvalid Input")


# It contains Employee Service Menu and functions
def employee_functions():
    # Employee menu
    n = int(input(
        "\n(Employee) Select a option from below : \n\t1.Employee Joining \n\t2.Employee Leaving \n\t3.Employee Details Update \n\t4.View Employee \n\t5.View All Employees\n Enter the action Number : "))

    # case 1
    # Employee Joining
    if n == 1:
        s = input(
            "\nEnter the data as - Emp Name | Emp Designation | Emp salary | Emp DOB | Emp techstack  *(use | as seperator)* \nNote - Enter salary without using comma and DOB format should be YYYY-MM-DD \n")
        x = s.split("|")
        for i in range(0, len(x)):
            try:
                x[i] = x[i].strip()
                x[i] = int(x[i])
            except ValueError:
                x[i] = x[i].strip()
        Employee_Service.insert_Data(x[0], x[1], x[2], x[3], x[4])

    # case 2
    # Employee Leaving
    elif n == 2:
        id = int(input("\nEnter the Employee ID : "))
        Common_Service.delete_Data(id, "Employee_ID", "Employee")

    # case 3
    # Employee Details Update
    elif n == 3:
        id = int(input("\nEnter the Employee ID : "))
        s = input(
            "\nEnter the updated value as - Emp Name | Emp Designation | Emp salary | Emp DOB | Emp techstack  *(use | as seperator)* \nNote - Enter salary without using comma and DOB format should be YYYY-MM-DD \n")
        x = s.split("|")
        for i in range(0, len(x)):
            try:
                x[i] = x[i].strip()
                x[i] = int(x[i])
            except ValueError:
                x[i] = x[i].strip()
        Employee_Service.update_Data(id, x[0], x[1], x[2], x[3], x[4])

    # case 4
    # View Employees
    elif n == 4:
        id = int(input("\nEnter the Employee ID : "))
        result = Common_Service.view_Data(id, "Employee_ID", "Employee")
        print("\t".join(map(str, result[0])))

    # case 5
    # View All Employees
    elif n == 5:
        result = Common_Service.view__All_Data("Employee")
        for i in result:
            print("\t".join(map(str, i)))

    # default case
    else:
        print("\nInvalid Input")


# main functions
def main():
    while (True):
        # main menu
        m = int(input("\nSelect a option from below : \n\t1.Employee Service \n\t2.Office Service \n\t3.Technology Service \n\t4.Backup Data \n\t5.Recover Data \n\t6.Exit \nEnter the action Number : "))

        # case 1
        if m == 1:
            employee_functions()
        # case 2
        elif m == 2:
            office_functions()
        # case 3
        elif m == 3:
            technology_functions()
        # case 4
        elif m == 4:
            DB_Service.backup_Data()
        # case 5
        elif m == 5:
            DB_Service.recover_Data()
        # case 6
        elif m == 6:
            break
        # default case
        else:
            print("\nInvalid Input")


if __name__ == "__main__":
    main()
