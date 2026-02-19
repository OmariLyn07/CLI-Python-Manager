import json
import os
import random

class Task:
    def __init__(self, description, status):
        self.description = description
        self.status = status                
    
    def update_status(self):
        self.status = "completed"

class TaskManager:
    def create_task(self, tasks):
        print("Input task description:\n")
        description = str(input())
        task = Task(description, "pending")
        rand_num = random.randrange(0, 10000)
        while rand_num in tasks:
            rand_num = random.randrange(0, 10000)
        tasks[rand_num] = task
        return tasks
    
    def update_task(self, tasks):
        print("Which task was completed?")
        print(tasks)
        upd_task = str(input())
        if upd_task in tasks:
            if type(tasks[upd_task]) == list:
                tasks[upd_task][1] = "completed"
            else:
                tasks[upd_task].update_status()
        else:
            print("task doesnt exist")
        return tasks
    
    def save_file(self, tasks):
        data_to_json = {}
        for t in tasks:
            if type(tasks[t]) == Task:
                data_to_json[t] = [tasks[t].description, tasks[t].status]
            else:
                data_to_json[t] = tasks[t]

        with open("Tasks.txt", "w") as file:
            file.write(json.dumps(data_to_json, indent=4))

    def delete_task(self, tasks):
        print("Which task is to be deleted?")
        print(tasks)
        choice = str(input())
        if choice in tasks:
            tasks.pop(choice)
        else:
            print("task doesnt exist")
        print("Task deleted")
        return tasks

    def manager_start(self):
        tasks = {}
        if os.path.exists("Tasks.txt"):
            opened_file = open("Tasks.txt")
            reader = json.load(opened_file)
            print(reader)
            opened_file.close()
            for t in reader:
                task = Task(reader[t][0], reader[t][1])
                tasks[t] = task
        else:
            print(tasks)
        return tasks
    
    def print_menu(self):
        print("Select an option\n"
    "1. Add a new Task\n"
    "2. View all tasks\n"
    "3. Mark a task completed\n"
    "4. Delete a task\n"
    "5. Quit(Tasks will be saved to file)")
        
    def print_curr_tasks(self, tasks):
        for t in tasks:
            if type(tasks[t]) == Task:
                print(t, "", [tasks[t].description, tasks[t].status])
            else:
                print(t, "", tasks[t])


def main():
    print("Task Manager Initiated")
    taskM = TaskManager()
    tasks = taskM.manager_start()
    taskM.print_menu()
    selection = str(input())

    while selection != '5':
        match selection:
            case '1':
                tasks = taskM.create_task(tasks)
                taskM.print_menu()
            
            case '2':
                taskM.print_curr_tasks(tasks)
                taskM.print_menu()
            
            case '3':
                tasks = taskM.update_task(tasks)
                taskM.print_menu()
            
            case '4':
                tasks = taskM.delete_task(tasks)
                taskM.print_menu()
            
            case '5':
                print("Exiting Program...")
                break
            
            case _:
                print("Invalid selection")
                taskM.print_menu()

        selection = str(input("Make a new Selection: "))

    
    taskM.save_file(tasks)

if __name__ == '__main__':
    main()
    


'''
Step 1: Core Requirements
1. Program must allow:
• Adding a new task
• Viewing all tasks
• Marking a task as completed
• Deleting a task
• Saving tasks to a file
• Loading tasks from a file on start
2. Tasks must have:
• Unique ID or index
• Description
• Status (e.g., Pending/Completed)

Step 2: Constraints
3. No external tutorials or copy-pasting for core logic. You may search syntax, but not full implementations.
4. Use classes: At least one class for Task, one for TaskManager.
5. Store tasks in a file using Python’s built-in functionality (text or JSON).
6. Program must load existing tasks automatically when started.
7. Input validation: Prevent invalid choices (e.g., deleting a non-existent task).
8. Menu-driven interface in CLI — e.g., numbered options for actions.

Step 3: Optional Enhancements (Stretch Goals)
9. Sort tasks by priority or status when viewing.
10. Allow editing task descriptions.
11. Add timestamps for creation and completion.
12. Implement search/filter for tasks.
Save completed tasks to a separate file or archive them.

Step 4: Project Workflow Constraints
14. Do not write all code at once. Work in small steps:
• Step 1: Define Task class, create a few sample tasks in memory.
• Step 2: Build TaskManager class with add/view/delete.
• Step 3: Implement file save/load.
• Step 4: Build CLI menu.
15. Test each step manually before moving to the next.
16. Debug systematically: Print intermediate states to ensure data is correct.
17. Document your thought process in comments — explain class responsibilities and method purposes.

Step 5: Success Criteria
You will know you’ve succeeded if you can:
• Add, view, delete, mark complete tasks without errors.
• Exit the program, restart it, and see all tasks persist correctly.
• Navigate your menu without confusing crashes.
• Make a small enhancement from Step 3 independently.

'''