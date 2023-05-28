import re
from datetime import datetime

Data={"fName":["menna"], "lName":["hesham"],"email":["menna@gmail.com"],"password":["1819"],"mobile":["01068619317"]}
project={"Data":["menna","menna"], "title":["ol","zae"],"details":["wop","zzzz"], "target":["20000","155000"],"startDate":["5-2-2023","14-5-2023"],"endDate":["25-4-2024","2-8-2024"]}

def login():
    email = input("enter your email: ")
    password = input("enter your password: ")
    if email in Data["email"] and password == Data["password"][Data["email"].index(email)]:
    print("Login successful!")
     print("Welcome, " + Data["fName"][Data["email"].index(email)])
     return email
    else:
      print("Invalid Data")
     return None

def createProject(email):

    title=input("enter title: ")

    details=input("enter details: ")

    target=input("enter total target: ")
    if target.isnumeric():
        startDate=input("enter start date (format: dd-mm-yyyy): ")
        if datetime.strptime(startDate, "%d-%m-%Y"):
            endDate=input("enter end date (format: dd-mm-yyyy): ")
            if datetime.strptime(endDate, "%d-%m-%Y"):
                projects["user"].append(Data["fName"][Data["email"].index(email)])
                projects["title"].append(title)
                projects["details"].append(details)
                projects["target"].append(target)
                projects["startDate"].append(startDate)
                projects["endDate"].append(endDate)
            else:
                print("invalid, enter end date (format: dd-mm-yyyy)")
        else:
            print("invalid, enter start date (format: dd-mm-yyyy)")
    else:
        print("please enter target in numbers")


def view_user_projects(login_email):

    for x in range(len(projects["user"])):
        if projects["user"][x] == Data["fName"][Data["email"].index(email)]:
            print(f"Project {x+1}:")
            print(f"User: {projects['user'][x]}")
            print(f"Title: {projects['title'][x]}")
            print(f"Details: {projects['details'][x]}")
            print(f"Total target: {projects['target'][x]}")
            print(f"Start date: {projects['startDate'][x]}")
            print(f"End date: {projects['endDate'][x]}")
            print()



def deleteProject(index,login_email):
    index -= 1
    if projects["user"][index] == users["fName"][users["email"].index(login_email)]:
        for key in projects:
            projects[key].pop(index)
        print("Project deleted successfully.")
    else:
        print("you are not authorized to delete this project")

def editProject(index,login_email):
    index-=1
    if projects["user"][index] == users["fName"][users["email"].index(login_email)]:
        updated_title = input("Enter the updated title: ")
        updated_details = input("Enter the updated details: ")
        updated_target = input("Enter the updated target: ")
        updated_start_date = input("Enter the updated start date (format: dd-mm-yyyy): ")
        updated_end_date = input("Enter the updated end date (format: dd-mm-yyyy): ")
        projects["title"][index] = updated_title
        projects["details"][index] = updated_details
        projects["target"][index] = updated_target
        projects["startDate"][index] = updated_start_date
        projects["endDate"][index] = updated_end_date

        print("updated successfully")
    else:
        print("you are not authorized to update this project")



flag=True
flag2=True
while flag:
    print("1-Register")
    print("2-Login")
    choice = int(input("press 1 to register and 2 to login: "))
    if choice==1:
        firstname=input("enter first name: ")
        if firstname.isalpha():

            lastname = input("enter last name: ")
            if lastname.isalpha():

                pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                email = input("enter email: ")
                if re.match(pattern, email):

                    password = input("enter password: ")
                    confirmpassword = input("enter confirm password: ")
                    if password==confirmpassword:

                        mobile = input("enter your mobile number: ")
                        pattern = r"^(?:\+?20)?(10|11|12|15|16|17|18|19)(?:\d{8})$"
                        if re.match(pattern, mobile):
                            users["fName"].append(firstname)
                            users["lName"].append(lastname)
                            users["email"].append(email)
                            users["password"].append(password)
                            users["mobile"].append(mobile)

                        else:
                            print("invalid mobile number")
                    else:
                        print("confirm password is not equal to password")
                else:
                    print("The email is invalid.")
            else:
                print("last name is invalid")
        else:
            print("first name is invalid")
    elif choice==2:
        login_emaill=login()
        if login_emaill:
            flag = False
            while flag2:
                ch = int(input("press 1 to create project\npress 2 to view your projects\npress 3 to delete a project\npress 4 to edit a project\npress 5 to quit\n"))
                if ch == 1:
                    createProject(login_emaill)
                elif ch == 2:
                    view_user_projects(login_emaill)
                elif ch==3:
                    indexToDelete=int(input("enter project number to delete: "))
                    if indexToDelete < 0 or indexToDelete > len(projects["title"]):
                        print("invalid index to delete")
                    else:
                        deleteProject(indexToDelete,login_emaill)
                elif ch==4:
                    indextoEdit=int(input("enter index of project to edit"))
                    if indextoEdit <0 or indextoEdit >len(projects["title"]):
                        print("invalid index to edit")
                    else:
                        editProject(indextoEdit,login_emaill)
                elif ch==5:
                    flag2=False
                else:
                    print("invalid choice")



    else:
        print("invalid choice")

