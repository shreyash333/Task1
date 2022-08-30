import Common_Service
import Office_Service
import Employee_Service
import DB
import Technology_Service


def technology_functions():
    n = int(input(
        "(Technology) Select a option from below : \n1.Add new Technology \n2.Delete a Technology \n3.Update a Technology \n4.View Technology \n5.View All Technology \nEnter the action Number : "))

    if n == 1:
        s = input(
            "Enter the Technology \n")
        Technology_Service.insert_Data(s)

    elif n == 2:
        id = int(input("Enter the Technology ID : "))
        Common_Service.delete_Data(id, "Technology_ID", "Technology")

    elif n == 3:
        id = int(input("Enter the Technology ID : "))
        s = input(
            "Enter the Technology \n")
        Technology_Service.update_Data(id, s)

    elif n == 4:
        id = int(input("Enter the Technology ID : "))
        result = Common_Service.view_Data(id, "Technology_ID", "Technology")
        print("\t".join(map(str, result[0])))

    elif n == 5:
        result = Common_Service.view__All_Data("Technology")
        for i in result:
            print("\t".join(map(str, i)))

    else:
        print("Invalid Input")


def office_functions():
    n = int(input(
        "(Office) Select a option from below : \n1.Add new Office \n2.Delete a Office \n3.Update a office \n4.View Office \n5.View All Offices \nEnter the action Number : "))

    if n == 1:
        s = input(
            "Enter the data as - office name | office Address *(use | as seperator)* \n")
        x = s.split("|")
        for i in range(0, len(x)):
            x[i] = x[i].strip()
        Office_Service.insert_Data(x[0], x[1])

    elif n == 2:
        id = int(input("Enter the Office ID : "))
        Common_Service.delete_Data(id, "Office_ID", "Office")

    elif n == 3:
        id = int(input("Enter the Office ID : "))
        s = input(
            "Enter the updated value as - office name | office Address *(use | as seperator)* \n")
        x = s.split("|")
        for i in range(0, len(x)):
            x[i] = x[i].strip()
        Office_Service.update_Data(id, x[0], x[1])

    elif n == 4:
        id = int(input("Enter the Office ID : "))
        result = Common_Service.view_Data(id, "Office_ID", "Office")
        print("\t".join(map(str, result[0])))

    elif n == 5:
        result = Common_Service.view__All_Data("Office")
        for i in result:
            print("\t".join(map(str, i)))

    else:
        print("Invalid Input")


m = int(input("Select a option from below : \n1.Employee Service \n2.Office Service \n3.Technology Service \n4.Backup Data \n5.Recover Data \nEnter the action Number"))

if m == 1:
    print("")
elif m == 2:
    office_functions()
elif m == 3:
    technology_functions()
elif m == 4:
    print("")
elif m == 5:
    print("")
else:
    print("Invalid Input")
