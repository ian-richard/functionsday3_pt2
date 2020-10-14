tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def tasks_status(list, status):
    list_of_ut = []
    for task in tasks:
        if task["completed"] == status:
            list_of_ut.append(task)
    return list_of_ut    

# print(tasks_status(tasks, True))

def task_desc(list):
    list_of_desc = []
    for task in tasks:
        list_of_desc.append(task["description"])
    return list_of_desc

# print(task_desc(tasks))

def task_time(list, time):
    list_time = []
    for task in tasks:
        if task["time_taken"] < time:
            list_time.append(task)
    return list_time

# print(task_time(tasks, 6))

def print_task(list, desc):
    for task in tasks:
        if task["description"] == desc:
            return task
    else:
        return "not found"

# print(print_task(tasks, "Walk Dog"))


def complete_task(list, desc):
    for task in tasks:
        if task["description"] == desc:
            task["completed"] = True
            return task
        
# print(complete_task(tasks, "Feed Cat"))

def add_task(list, desc, comp, time):
    new_entry = {"description": desc, "completed":comp, "time_taken":time}
    tasks.append(new_entry)
    return list


# print(add_task(tasks, "Hoovering", True, 20))


def print_menu():
    print("Menu:")
    print("1: Display All Tasks")
    print("2: Display Uncompleted Tasks")
    print("3: Display Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")

choice = input("enter your choice")

def user_choice(choice):
    while choice 
    print_menu()
    choice = input("enter your choice")
    

# print(user_choice())
    
