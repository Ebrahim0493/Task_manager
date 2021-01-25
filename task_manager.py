import datetime
# This is all my variabla names within the task
user_names = ""
user_passwords = ""
login = False
logged = False
exit = False
register = False
add = False
view_all = False
view_mine = False
admin = False
user_name = ""

# we have 2 menues in this task a menu where any user can do the below and a admin menu where only admin can do certain things


def menu():
    return ("""
Please select one of the options below:
a-add task
va-view all tasks
vm-view my tasks
gr-generate reports
ds-display statistics
e-exit          
""")

# refer to above comment please


def admin_menu():
    return ("""
Please select one of the options below:
r-register user
a-add task
va-view all tasks
vm-view my tasks
gr-generate reports
ds-display statistics
e-exit          
""")


# this for loop allows us to split the sentaces within the user txt file aswell as remove any unwanted spaces
users = open("user.txt", "r")
for line in users:
    temp = line.strip()
    temp = temp.split(", ")
    user_names += temp[0]
    user_passwords += temp[1]

users.close()


# This is where we are allowed to register a user to user txt file using a if else statment
def reg_user():
    task_user = input("please enter name on the register: ")
    if admin == False:
        print("only admin can add tasks")
    task_user_password = input("please enter password on the register: ")
    if task_user in user_names:
        print("user already exists.")
    else:
        with open("user.txt", "a") as f:
            f.write(f"\n{task_user}, {task_user_password}")

# This is if else statment allows only admin to add tasks to a certain user


def add_task():
    task_user = input("please assign task here: ")
    if task_user not in user_names:
        print("user does not exit")
    else:
        task_title = input("please insert task title: ")
        description = input("please insert task description: ")
        assigned_date = input("please insert date: ")
        due_date = input("please insert due date: ")
        completed = ("no")

        with open("tasks.txt", "a") as f:
            f.write(f"""
\n{task_user},{task_title},{description},{assigned_date},{due_date},{completed}""")

# view all allows a user to view all the tasks that there are on the system (tasks within tasks txt file)


def view_all():
    tasks = open("tasks.txt", "r")
    num_task = 0
    for task in tasks:
        task_user, task_title, description, assigned_date, due_date, completed = task.split(
            ",")
        num_task += 1
        print(f"""
Task: {num_task}
Username: {task_user}
Task at hand: {task_title}
Brief description: {description}
Start date: {assigned_date}
End date: {due_date}
Completed: {completed}
""")

# here a user can view all his or her tasks


def view_mine():
    num_task = 0
    task_user = open("tasks.txt", "r+")
    for line in task_user:
        task_user, task_title, description, assigned_date, due_date, completed = line.split(
            ",")
        num_task += 1
        if user_name == task_user:
            print(f"""
Task: {num_task}
Username: {task_user}
Task at hand: {task_title}
Brief description: {description}
Start date: {assigned_date}
End date: {due_date}
Completed: {completed}
""")

# here we are generting reports from the tasks txt file to view completnes, due dates and incompleteness of tasks


def generate_reports():
    with open("tasks.txt", "a")as f:
        data = f.read()
        user_task = data.count('Task Title')
        task_completed = data.count("Yes")
        task_incomplete = data.count("No")
        today = datetime.datetime.today()
        overdue = 0
        for line in f:
            if not line.startswith("Due Date"):
                continue
            field, value = line.split(":")
            if field == "Due Date":
                if datetime.datetime.strptime(value.strip(), '%Y-%m-%d') < today:
                    overdue = overdue + 1
                    ab = (overdue/user_task)*100
                    abb = (task_incomplete/user_task)*100
                    output = f"""
Total number of tasks: {task_incomplete}
Total number of completed tasks: {task_completed}  
Total number of incomplete tasks: {task_incomplete}
The percentage of overdue tasks is: {ab} 
The percentage of incomplete jobs is: {abb} 
"""
                    with open("task_overview.txt", "w") as file:
                        file.write(output)


def display_statistics():
    num_lines = sum(1 for line in open('user.txt'))

    data1 = open('tasks.txt', 'r').read()
    usr_check = input(
        "Please input a user name to write details of that user.\n")
    user_count = data1.count(user_names)
    task_incomplete = data1.count("No")
    task_percentage = (user_count/task_incomplete)*100
    output = f"""
The number of registered users is: {num_lines}
The user {user_names} has total tasks of: {user_count}
{usr_check}'s percentage of total tasks is: {task_percentage}
"""

    with open("user_overview.txt", "w") as file1:
        file1.write(output)


while logged == False:
    user_name = input("please enter your user name.")
    user_password = input("please enter your user password.")

    if user_name not in user_names:
        print("Incorrect username")

    elif user_password not in user_passwords:
        print("Password incorrect")

    else:
        logged = True

  # this if statement checks if a user is looged into the system
if logged == True:
    while exit == False:

        if admin == True:
            print(admin_menu())

        else:
            print(menu())
        option = input(":")

        # this if allows you to exit the program
        if option == ("e"):
            exit = True
            print("Thank you Good Bye")

        if option == ("a"):
            add_task()

        if option == ("r"):
            reg_user()

        if option == ("va"):
            view_all()

        if option == ("vm"):
            view_mine()

        if option == ("gr"):
            generate_reports()

        if option == ("ds"):
            display_statistics()


def mark_complete(complete, index):
    with open("tasks.txt", "r") as f:
        lines = f.readlines()
    lines[index] = complete + '\n'
    with open("tasks.txt", "w") as tasks:
        tasks.writelines(lines)


mark_complete("Thank you!", 0)
