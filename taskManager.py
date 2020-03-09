check = True
checkUser = 0
Login_Register = input("Welcome,\nType L for Login, R to Register\n")
if Login_Register == "r" or Login_Register == "R":
    f = open("user.txt","a+")
    username = input("Please enter your Username! ")
    password = input("Please enter your password! ")
    password_confirm = input("Please enter your password again! ")
    f.write(f"\nUsername:{username} Password:{password}\n") #f writes through the txt file
    f.close()
    print("You have successfully Registered\nEnjoy ",username)

if Login_Register == "l" or Login_Register =="L":      #this is where you chosse between loggin in and registering
    while check:
        with open("user.txt", "r") as f:
            username1 = input("Enter your username: ")#user's username
            password1 = input("Enter your password: ")#user's password
            for line in f: #users multiple usernames and passwords will be written to a txt file
                if("Username:"+username1+" Password:"+password1) == line.strip():
                    print("you are logged in") #if("Username:"+username1+" Password:"+password1) == line.strip(): if this succeeds it will print out "you are logged in" otherwise  it breaks out 
                    check = False
                    checkUser = 1
                    break
                
                    

main = input("Please select one of the following options: \n r - register user \n a - add task \n va - view all tasks \n vm - view my tasks \n e - exit \n")        #if the users logged in the it take them to this optional menu
if main == "r":
    adUser_name = input("Please enter your username:    ")
    if adUser_name == "admin":
        userRegister = input("d - Display statistics \n")

            #This will count the number of registered users in the users file and add that value to the userLine_count variable
        userLine_count = 0
        userFile = open("user.txt", "r")
        userFile_var = userFile.readlines()
        for line in userFile_var:
            userLine_count += 1

            #This will count the number of tasks in the task file and store the value in the taskLine_count variabel
            tasksLine_count = 0
            with open("tasks.txt", "r") as tasksFile_count:
                for line in tasksFile_count:
                    tasksLine_count += 1
            #If the user picks the prompt, then the statistics will be displayed on screen
            if userRegister == "d":
                print("The amount of Users registered is:  " + str(userLine_count) + "\nThe amount of Current Tasks Open is:  " + str(tasksLine_count))

            #IF the user is not the admin then this message will show up and end the program
            else:
                print("Registration Access is only granted to the Admin!")

    #This is for adding a task to a person
if main == "a":
    userTask = input("Enter username of person assigned to task:   ")
    userTask_title = input("Enter task title:   ")
    userTask_description = input("Enter task description:   ")
    userTask_dueDate = input("Enter task due Date (yyyy-mm-dd):   ")
    userTask_dateAssigned = input("Enter current date(dd/mm/yyyy):   ")
    userTask_status = "NO"
    with open("tasks.txt", "a") as userTask_file:
        userTask_file.write("\n" + userTask + " - " + userTask_title + " - " + userTask_description + " - " + userTask_dueDate + " - " + userTask_dateAssigned + " - " + userTask_status)
        userTask_file.close()
    
        
if main == "va":
    with open("tasks.txt", "r+") as userTask_file:
            userTaskDisplay = userTask_file.read()
            print("These are the current tasks:  \n") 
            print("(Username - Task - Task Description - Task Due Date - Task Deadline - Task Completion Status)  \n")
            print(userTaskDisplay)
            print("\n")

if main == "vm":
    print("View my task")
    userName_prompt = input("Enter username:    ")
    with open("tasks.txt","r") as userFile:
            userTasks_file = userFile.readlines()
            for user in userTasks_file:    #For loop will run through each line of the code first and split them by the hyphen and then it will find the first position in the array and match that to the name in the tasks file and print out the whole line which has the tasks for that name.
                userTaskInfo = user.split(" - ")
                if userName_prompt == userTaskInfo[0]:
                    print(user)
        
if main == "e":                     #if main == "e": it is used to exit the program
    print("You have successfully existed the program")
            


    
 
        

