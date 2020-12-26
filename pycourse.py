import sqlite3 as sq

#functionality

class DatabaseManage(object):

    def __init__(self):
        global con
        try:
            con = sq.connect('courses.db')
            with con:
               global cur=con.cursor()
                cur.execute("Create table if not exists course(ID integer primary key autoincrement ,name Text, description Text,price text, is_private boolean Not NUll 1)")
        except Exception:
            print("Unable to create a db")


#TODO: create data

def insert_data(self,data):
    try:
        with con:
            cur.con.cursor()
            cur.execute(
                
                "Insert into course(name,description,price,is_private) Values (?,?,?,?)",data
            )
    except Exception:
         return False  

def fetch_data(self):
    try:
        with con:
            cur.con.cursor()
            cur.execute("Select *from courses")
        return cur.fetchall()
    except Exception:
         return False 
def del_data(self,id):
    try:
        with con:
            cur.con.cursor()
            sql = "Delete from courese Where id=?"
            cur.execute(
                
                "sql",[id] )
    except Exception:
         return False 






#TODO:provide interface to user

def main():
    print("*\n"*40)
    print("\n ::Course management::\n")
    print("*\n"*40)

    db= DatabaseManage()
    print("#\n"*40)
    print("\n::user manual:: \n")
    print("#\n"*40)

    print('1 Insert new course')
    print('2 show all course')
    print('3 Delete a courde (ID)')
    print("#\n"*40)

    choice = input("\n Enter a choice: ")

    if choice == "1":
        name=input("\n Enter course name: ")
        description =input("\n Enter description: ")
        price=input("\n Enter price: ")
        private=input("\n Is this course private(0/1): ")

        if db.insert_data([name,description,price,private]):
            print('course inserted successfullt')
        else:
            print('something is wrong')

    elif choice=='2':
        print("\n Course list::")   

        for index,i in (db.fetch_data()):
            print("\n sl:no : "+ str(index +1)) 
            print("\n course ID : "+ str(i[0]))
            print("\n course name : "+ str(i[1])) 
            print("\n course description : "+ str(i[2]))
            print("\n course pricr  : "+ str(i[3]))   
            private='yes' if item[4] else 'NO'
            print("\n Is private : "+ private) 
            print("\n")
    elif choice=='3':
        record_id = input("enter course id: ")

        if db.delete_data(record_id):
            print("Course was deleted with a")
        else:
            print('oops something went wrong') 
    else:
            print("\n Bad choice")   
             


if __name__ == "__main__":
    main()




       








    







