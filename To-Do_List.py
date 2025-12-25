import csv

# .:: Defining tasks ::. 
class Tasks():
    def __init__(self,name,description,priority,deadline):
        self.name = name
        self.description = description
        self.priority = priority
        self.deadline = deadline

    def __str__(self):
        return f"Name: {self.name} | Desc: {self.description} | Priority: {self.priority} | Deadline: {self.deadline}"


# .:: to do list class ::. 

class Todolists():
    def __init__(self):
        self.tasks = []

    def load_from_csv(self,filename):
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    task = Tasks(row[0], row[1], row[2], row[3])
                    self.tasks.append(task)
        except FileNotFoundError:
            print("file dosen't exist")

    def save_to_csv(self , filename):
        try :
            with open(filename, "w") as file:
                writer = csv.writer(file)
                for task in self.tasks :
                    writer.writerow([
                        task.name ,
                        task.description ,
                        task.deadline,
                        task.priority])
                    
            print(f"list was saved in {filename}")

        except : 
            print("unknown error")

    def add_task(self,task):
        self.tasks.append(task)
        print("Task added successfully!")


    def remove_task(self, index):
            try:
                removed = self.tasks.pop(index)
                print(f"Task '{removed.name}' removed.")
            except IndexError:
                print("Invalid task number!")

    def show_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i}. {task}")

                

todo = Todolists()
filename = "tasks.csv"
todo.load_from_csv(filename)

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Save and Exit")
    
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        todo.show_tasks()

    elif choice == "2":
        name = input("Enter task name: ")
        desc = input("Enter description: ")
        priority = input("Enter priority (High/Medium/Low): ")
        deadline = input("Enter deadline: ")
        new_task = Tasks(name, desc, priority, deadline)
        todo.add_task(new_task)

    elif choice == "3":
        todo.show_tasks()
        if todo.tasks:
            try:
                idx = int(input("Enter task number to remove: "))
                todo.remove_task(idx)
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        todo.save_to_csv(filename)
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")

