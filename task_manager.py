'''This is the section where you will import libraries'''
import datetime
from dateutil import parser
# functions
def reg_user():
    if user_name == 'admin':
        while True:
            new_user = input("Enter new username: ")
            #checking to see if the user is present in the database, if so then giving the admin a chance to try to add a different username.
            while True:
                if new_user in credentials:
                    print(f'there is a user already present in database with the name {new_user}. please try again')
                    new_user = input("Enter new username: ")
                else:
                    break
                
            new_password = input("Create a password for the user: ")
            #checking if the user passwords matches.
            confirmed_pass = input("Retype password: ")
            if confirmed_pass == new_password:
                with open('users.txt', 'a') as file:
                    file.write(f"\n{new_user}, {confirmed_pass}")
                    
            else:
                i = 2
                while i > 0:
                    print(f"Passwords don't match you have {i-1} tries to match the passwords.")
                    retype = input("Retype password: ")
                    if retype == new_password:
                        with open('users.txt', 'a') as file:
                            file.write(f"\n{new_user}, {retype}")
                            break
                        
                    i-=1
            print(f"{new_user} successfully created!")
            break
    else:
        print('only admins can register a user.')

def add_task():
    assing_tsk = input("Enter the username of who this task is assigned to: ")
    if assing_tsk in credentials:
        file = open('tasks.txt', 'a')
        tsk_title = input("Enter the title of the task: ")
        tsk_desc = input("Enter task description: ")
        due_date = input("Enter the date the task is due in DD/MM/YYYY format: ")
        current_date = input("Enter current date in DD/MM/YYYY: ")
        file.write(f"\n{assing_tsk}, {tsk_title}, {tsk_desc}, {due_date}, {current_date}, no")
        print(f"{tsk_title}, has been successfully being assigned to {assing_tsk}")
        file.close()
    else:
        print('user not present in the database. please register the new user before assigning a task')

def view_all():
    #linking the program to the task.txt file.
        file = open('tasks.txt', 'r')
        #storing all the data in task.txt into a list.
        data_task_list = file.readlines()
        #pos to determine the task number. and line to represent each indivdual line in the txt file.
        for pos,line in enumerate(data_task_list):
            #here is where the data in the each line is split, to individual elements, so data of each row can be accessed by seperated[i]
            seperated_data = line.split(', ')
            output = f'■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■[{pos}]■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n'
            output += f"Task Title: \t \t \t{seperated_data[1]}\n"
            output += f"Assigned To: \t \t \t{seperated_data[0]}\n"
            output += f"Date Assigned: \t \t \t{seperated_data[3]}\n"
            output += f"Due Date: \t \t \t{seperated_data[4]}\n"
            output += f"Task Complete: \t \t \t{seperated_data[5]}\n"
            output += f"Task Description: \t \t{seperated_data[2]}"
            print(output)
        file.close()

def view_mine():
    file_tsk = open('tasks.txt', 'r')
    data = file_tsk.readlines()
    
    for pos, line in enumerate(data):
        split_data = line.split(', ')
        
        #checking if the user has been assigned a task, and returning if the user does have a task present in the tasks.txt file
        if user_name == split_data[0]:
            output = f'■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■[{pos}]■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n'
            output += f"Task Title: \t \t \t{split_data[1]}\n"
            output += f"Assigned To: \t \t \t{split_data[0]}\n"
            output += f"Date Assigned: \t \t \t{split_data[3]}\n"
            output += f"Due Date: \t \t \t{split_data[4]}\n"
            output += f"Task Complete: \t \t \t{split_data[5]}\n"
            output += f"Task Description: \t \t{split_data[2]}"
            print(output)
        file_tsk.close()
    while True:
        user_choice = int(input("Enter the number of the task you would like to edit or type -1 to exit to the main menu: "))
        if user_choice < -1 or user_choice > pos:
            print("You have entered an invalid option, please try again: ")
            continue
        edit_data = data[user_choice]
        if user_choice == -1:
            break
        
        break
    #presenting the user with a menu,
    while True:
        output = f'■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■[Select a option]■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n'
        output += f"1- to mark task complete \n"
        output += f"2- to edit the task \n"
        output += f"3- to exit back to main menu \n"
        choice = int(input(output))
        #checking if user enters a valid input.
        if choice == 0 or choice >= 4:
            print("You have entered an invalid option, please try again: ")
            continue
        # marking the task complete.
        elif choice == 1:
            edit_choice_lst = edit_data.split(', ')
            edit_choice_lst[5] = "yes\n"
            new_data = ", ".join(edit_choice_lst)
            data[user_choice] = new_data
            with open('tasks.txt', 'w') as f:
                for line in data:
                    f.write(line)
        #checking if the task the user chose is completed.
        elif choice == 2:
            edit_data = data[user_choice]
            edit_info = edit_data.split(', ')
            if edit_info[-1] == 'yes\n':
                print("cannot edit a task that is complete, please enter a uncompleted task.")
                break
            #to allow user to edit task, due date and username, also kept within loop to allow the user to make more than one change.
            while True:
                output = f'■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■[Select a option]■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n'
                output += f"1- to edit the username \n"
                output += f"2- to edit the task due date \n"
                output += f"3- to esc \n"
                choice = int(input(output))
                if choice == 0 or choice >= 4:
                    print("You have entered an invalid option, please try again: ")
                    continue
                elif choice == 1:
                    new_user = input("Enter the name of the new username: ").lower()
                    edit_info[0] = new_user
                    new_data = ", ".join(edit_info)
                    data[user_choice] = new_data
                    with open('tasks.txt', 'w') as f:
                        for line in data:
                            f.write(line)
                elif choice == 2:
                    new_due_date = input("Enter the new date in dd/mm/yy format: ").lower()
                    edit_info[-2] = new_due_date
                    new_data = ", ".join(edit_info)
                    data[user_choice] = new_data
                    with open('tasks.txt', 'w') as f:
                        for line in data:
                            f.write(line)
                #to escape out.
                else:
                    break
        # to allow the user to escape back into the main menu.
        else:
            break

def generater():
    
    #the current date
    todays_date = datetime.datetime.now()
    
    #accessing the files
    overview = open('task_overiew.txt', 'w')
    task_file = open('tasks.txt', 'r')
    
    # putting the contents of the file in a list.
    data = task_file.readlines()
    
    #lists to store values so it can be manipulated
    
    completed_task = []
    uncompleted_task = []
    overdue = []
    total_task = []
    task_assigned = []
    
    #iterating over the contents of the file store/transform elements of the data.
    for pos, line in enumerate(data):
        each_task = line.split(', ')
        task_assigned.append(each_task[0])
        total_task.append(line)
        task_date = parser.parse(each_task[-2])
        task_counter = pos + 1
        if todays_date > task_date:
            overdue.append(each_task[0])
        if each_task[-1] == 'yes\n':
            completed_task.append(each_task[0])
        elif each_task[-1] == 'no\n':
            uncompleted_task.append(each_task[0])
    
    #information that is going to be written to the task_overiew text file   
    task_due = f"there is {len(overdue)} overdue tasks in the datebase"
    counter = f"the amount of tasks that have been generated is {task_counter}"
    complete = f"the amount of completed task {len(completed_task)}"
    uncomplete = f"the amount of uncompleted task {len(uncompleted_task)}"
    percent_uncomp = f"{(len(uncompleted_task)/task_counter)*100} % of the tasks in the datebase is incomplete"
    percent_due = f"{(len(overdue)/task_counter)*100} % of the tasks in the datebase is overdue"
    
    #writing to the txt.file
    overview.write(f"{counter} \n{complete} \n{uncomplete} \n{task_due} \n{percent_uncomp} \n{percent_due}")
    overview.close()
    task_file.close()
    
    #list of users and empt dict
    usersd = []
    dict = {}
    user_file = open('users.txt', 'r')
    u_info = user_file.readlines()
    #cleaning the data in the users.txt and storing the values in a list
    for user in u_info:
        users_data = user.split(',')
        users = users_data[0].strip(',')
        usersd.append(users)
    
    #creating a dict , with the user name being the key and the amount of times the task is assigned as a value
    for username in usersd:
        dict[username] = 0
        for task in task_assigned:
            if username == task:
                dict[username] += 1

    # storing the amount of completed task per user in a dict
    ct = {}
    for username in usersd:
        ct[username] = 0
        for complete_task in completed_task:
            if username == complete_task:
                ct[username] +=1       

    #storing the percentage of completed and not completed task in a dict
    cpt = {}
    ncpt = {}        
    for user, vale  in ct.items():
        for username, value in dict.items():
            if user == username:
                cpt[username] = 0
                ncpt[username] = 0
                if vale == 0:
                    cpt[username] = f"{0}%"
                    continue
                completes = vale/value * 100
                non_completed = 100 - completes
                cpt[username] = f"{completes}%"
                ncpt[username] = f"{non_completed}%"
    
    #collecting the users that have overdue tasks
    p_overdue = {}
    for user in usersd:
        p_overdue[user] = 0
        for value in overdue:
            if user == value:
                p_overdue[user] += 1

    #collecting the uncompleted task.
    un_ct = {}
    for user in usersd:
        un_ct[user] = 0
        for value in uncompleted_task:
            if user == value:
                un_ct[user] += 1
            
    overdue_uncomp = {}
    #getting the % of the uncompleted task that are over due. 
    
    for key, value in un_ct.items():
        overdue_uncomp[key] = 0
        for k, v in p_overdue.items():
            if key == k:
                if value == 0:
                    overdue_uncomp[key] = 0
                else:
                    percent = v/value * 100
                    overdue_uncomp[key] = f"{percent}%"

    #getting the % of the total task assigned to the user.
    per_of_task_assign = {}
    for key, value in dict.items():
        per_of_task_assign[key] = f"{(value/len(total_task) * 100)}%"
    

    with open('users_overview.txt', 'w') as f:
        f.write(f"the total number of number of users registered is {len(usersd)}\ntotal number of task that have been generated and tracked is {len(total_task)}\n")
        for name in usersd:
            f.write(f"{name}, total task assigned is {dict[name]}, {per_of_task_assign[name]} of the tasks is assigned to {name}, {cpt[name]} is complete, {ncpt[name]} needs to be completed, {overdue_uncomp[name]} is overdue and not completed\n")
              
    user_file.close()

def display_r():
    #in a while true loop so the user can stay and make more than one option. an escape key has been provided

    while True:
        output = f'■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■[Select a option]■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n'
        output += f"1- to view Task statistics \n"
        output += f"2- to view User statistics \n"
        output += f"3- to exit to main menu\n"
        output += 'Enter number: '
        choice = int(input(output))
        
        #checking user input

        if choice == 0 or choice >= 4:
            print("You have entered an invalid option, please try again: ")
            continue
        
        #presenting the user with the tasks overview

        if choice == 1:
            with open('task_overiew.txt', 'r') as f:
                tasks = f.readlines()
            
                output = f'■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■[Task Overview]■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n'
                output += f"{tasks[0]}"
                output += f"{tasks[1]}"
                output += f"{tasks[2]}"
                output += f"{tasks[3]}"
                output += f"{tasks[4]}"
                output += f"{tasks[5]}"
                print(output)
                
                    
        #this sections shows the user stats. its a different loop so the user has a chance to check multiple users at the same time.

        elif choice == 2:
            while True:
                output = f'■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■[Select a option]■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n'
                output += f"1- to view all user statistics \n"
                output += f"2- to view a specific user statistics \n"
                output += f"3- to exit to main menu\n"
                output += 'Enter number: '
                choice1 = int(input(output))
                
                #checking user input

                if choice1 == 0 or choice >= 4:
                    print("You have entered an invalid option, please try again: ")
                    continue
                
                #displaying all user values.

                if choice1 == 1:
                    with open('users_overview.txt', 'r') as f:
                        usersover = f.readlines()
                        #removing the first to elements.
                        del usersover[0:2]
                        
                        for info in usersover:
                            user = info.split(', ')
                            output = f'■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■[{user[0]}]■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n'
                            output += f'{user[1]}\n'
                            output += f'{user[2]}\n'
                            output += f'{user[3]}\n'
                            output += f'{user[4]}\n'
                            output += f'{user[5]}\n'
                            print(output)

                #this section provides the user to check individual stats of each user.

                elif choice1 == 2:
                    name = input("Enter the name of the specific user: ").lower()
                    with open('users_overview.txt', 'r') as f:
                        usersover = f.readlines()
                        del usersover[0:2]
                        for info in usersover:
                            user = info.split(', ')
                            if f'{name}'== user[0]:
                                output = f'■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■[{user[0]}]■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ \n'
                                output += f'{user[1]}\n'
                                output += f'{user[2]}\n'
                                output += f'{user[3]}\n'
                                output += f'{user[4]}\n'
                                output += f'{user[5]}\n'
                                print(output)
                elif choice1 == 3:
                    break
        elif choice == 3:
            break

#user credentials

users = open('users.txt', 'r')
credentials = {}

#storing the username and password in a dict.
for line in users:
    username, password = line.strip().split(',')
    #to get rid of the space in the password to prevent error or confusing in the output.
    p = password.replace(" ", "")
    credentials[username] = p
#promting the user to input credentials, looping through to check if the user has access to the system.
while True:
    user_name = input("Enter username: ")
    if user_name in credentials:
        i = 3
        #checking if the password matches the user. created a loop to give the user 3 chances.
        while i > 0:
            pass_word = input("Enter password: ")
            check = credentials[user_name]
            if pass_word == check:
                break
            else:
                print(f"you have entered the wrong password you have {i-1} attempts left")
            i -= 1
        break
    else:
        print("Username not recgonised, please try again")
       
users.close()

while True:
    if user_name == 'admin':
        print(f"current operating user: {user_name}")
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
s - show statistics
va - View all tasks
vm - view my task
gr - generate reports
ds - display statistics

e - Exit
: ''').lower()
        
    else:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
        print(f"current operating user: {user_name}")
        menu = input('''Select one of the following Options below:

a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
    
    if menu == 's':
        #opening files to get data from both users.txt and task.txt
        with open('tasks.txt', 'r') as task:
            stats_file_t = task.readlines()
        with open('users.txt', 'r') as users:
            stats_file_u = users.readlines()
        for pos, line in enumerate(stats_file_t):
            #to get each seperate line in the task.txt folder and iterate through
            split_file = line.split('\n')
            #because python starts the count from zero
            task_stat = pos + 1
        for pos, line in enumerate(stats_file_u):
            split_info = line.split('\n')
            user_stat = pos + 1
        print(f"the current number of tasks is {task_stat}, and total amount of users in the database is {user_stat}")




    elif menu == 'r':
    #calling the function that creates a users.
        reg_user()
            
    
    #presenting the user with the option to enter a task.
    elif menu == 'a':
        #promting the user to enter details about the task.
        add_task()
        
    #presenting the user with the option to view all task.    
    elif menu == 'va':
        #function to check all task assigned
        view_all()
    
    #presenting the user with the option to check task specific to the user.    
    elif menu == 'vm':
        #calling the function view_mine
        view_mine()
   
   
   #presenting the user with the option to generate results    
    elif menu == 'gr':
        generater()   
    
    elif menu == 'ds':
        display_r()


    elif menu == 'e':
        print('Goodbye!!!')
        exit()


    else:
        print("You have made a wrong choice, Please Try again")