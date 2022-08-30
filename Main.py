import Common_Function
import Office
import Employee
import DB
import TechStack

n = int(input(
    "(Office) Select a option from below : \n1.Insert new Office \n2.View Office \n3.Update a office \n4.Delete a Office \n5.View All Office\n Enter the action Number"))
if n == 1:
    s = input(
        "Enter the data as - office name | office Address *(use | as seperator)* \n")
    x = s.split("|")
    for i in range(0, len(x)):
        x[i] = x[i].strip()
    Office.insert_Data(x[0], x[1])

elif n == 2:
    id = int(input("Enter the Office ID : "))
    result = Common_Function.view_Data(id, "Office_ID", "Office")
    print("\t".join(map(str, result[0])))

elif n == 3:
    id = int(input("Enter the Office ID : "))
    s = input(
        "Enter the updated value as - office name | office Address *(use | as seperator)* \n")
    x = s.split("|")
    for i in range(0, len(x)):
        x[i] = x[i].strip()
    Office.update_Data(id, x[0], x[1])

elif n == 4:
    id = int(input("Enter the Office ID : "))
    Common_Function.delete_Data(id, "Office_ID", "Office")

elif n == 5:
    result = Common_Function.view__All_Data("Office")
    for i in result:
        print("\t".join(map(str, i)))

else:
    print("Invalid Input")
