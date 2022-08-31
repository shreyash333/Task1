Its a simple python code with MYSQL to perform CRUD operation along with logging and backup. 

It consist of three database tables :
Employee
Technology
Office

There are 5 main service :
1.Employee Service 
2.Office Service 
3.Technology Service 
4.Backup Data 
5.Recover Data

First three services have sub- services as CRUD operations
INSERT
DELETE
UPDATE
VIEW
VIEW ALL

Backup Data - saves data from main DB to backup DB

Recover Data - bring back the old data from backup to main DB

For Running - 
Run - "pip install -r requirements.txt"
Make tables in MYSQL using the queries in "Database.txt" file
Run - "python main.py"