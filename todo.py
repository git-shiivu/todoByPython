todoList = []

try:
    with open("todo.txt", "r") as f:
        for line in f:
          todoList.append(line.strip())
except FileNotFoundError:
    pass


def readToDo():
  if(len(todoList) == 0):
    print("The list is empty!")
  else:
    print("The List/s is/are:\n")
    for i in range(len(todoList)):
      print(str(i+1 )+ ") " + todoList[i])

def addToDO():
  todoList.append(input("Enter the To-do: "))
  print("The To-Do ADDED successfully!\n")
  readToDo()

def updateToDO():
  indexOfTodo = (int(input("Enter thier Serial number to UPDATE: "))- 1)
  todoList[indexOfTodo] = input("Enter updated ToDo: ")
  print("The To-Do UPDATED successfully!\n")
  readToDo()

def deleteToDo():
  todoList.pop(int(input("Enter thier Serial number to DELETE: "))- 1)
  
  print("The data was DELETED succssfully!\n")
  readToDo()

def selection():

  print("\n1 stands for ADD To-Do\n2 stands for UPDATE To-Do\n3 stands for READ To-Dos\n4 stands for DELETE To-Do\n5 for EXIT from Terminal\n")
  want = int(input("What do you want: "))

  if(want == 1):
    addToDO()
  elif(want == 2):
    updateToDO()
  elif(want == 3):
    readToDo()
  elif(want == 4):
    deleteToDo()
  elif(want == 5):
    print("Thank you!")
    exit()
  else:
    print("Invalid option selected.")

while(True):
  selection()
  with open("todo.txt", "w") as f:
    for i in range(len(todoList)):
      f.write(todoList[i]+"\n")