class Record:
    def __init__(self):
        self.record = []

    def addR(self, a):
        self.record.append(a)
    def remR(self, b):
        self.record.remove(b)
    def searchR(self, c):
        return c in self.record
    def isEmpty(self):
        return (self.record == [])

    def __str__(self):
        return (str(self.record))

class Task_Manager(Record):
    def __init__(self):
        self.r=Record()
        with open("Audit.txt", 'w') as f:
            f.write("Activity Log\n")
        f.close()
    def addTask(self, a):
        if self.r.searchR(a):
            self.logActivity(f"Add {a}: Unsuccessful (already exists)")
            raise Exception(f"{a}: already exists")
        else:
            self.r.addR(a)
            self.logActivity(f"Add {a}: Successful")

    def remTask(self, b):
        if self.r.searchR(b):
            self.r.remR(b)
            self.logActivity(f"Delete {b}: Successful")
        else:
            self.logActivity(f"Delete {b}: Unsuccessful (does not exist)")
            raise Exception(f"{b}: does not exist, deletion not possible")
    def searchTask(self, c):
        if self.r.searchR(c):
            self.logActivity(f"Search {c}: Successful")
        else:
            self.logActivity(f"Search {c}: Unsuccessful (does not exist)")
            raise Exception(f"{c}: does not exist")

    def printTask(self):
        if self.r.isEmpty():
            print("Tasks are completed")
        else:
            print(self.r.record) #have to check again
    def saveTask(self):
        self.logActivity("Task is saved successfuly")

    def logActivity(self, message):
        with open("Audit.txt", 'a') as f:
            f.write(message + "\n")
        f.close()

t = Task_Manager()

try:
    n = int(input('''Choose an operation:
    1. Create new tasks
    2. Remove existing tasks
    3. Search for existing tasks
    4. Print all existing tasks
    5. Save a log of the activity of the user in a txt file.
    6. Exit Option
    '''))

    while n != 6:
        try:
            if n == 1:
                print("Create and Enter a new task")
                a = input("Enter the task: ")
                t.addTask(a)
                print("Added Successfully")
            elif n == 2:
                b = input("Which task to remove: ")
                t.remTask(b)
                print("Task deleted")
            elif n == 3:
                c = input("Which task do you want to search for: ")
                t.searchTask(c)
                print("Search is completed")
            elif n == 4:
                print("Here are the tasks which are left")
                t.printTask()
            elif n == 5:
                t.saveTask()
                print("Saved a log file")
            else:
                print("Invalid option. Please choose a valid operation.")
        except Exception as e:
            print(e)

        n = int(input('''Choose an operation:
        1. Create new tasks
        2. Remove existing tasks
        3. Search for existing tasks
        4. Print all existing tasks
        5. Save a log of the activity of the user in a txt file.
        6. Exit Option
        '''))

except ValueError:
    print("Please enter a valid number. Program is over.")
print(("Thanks for using"))
