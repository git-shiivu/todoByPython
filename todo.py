
#initailize empty array for store todos
todoList = []

#open file and read it, if it is avilable if not, pass or skip it
try:
    with open("todo.txt", "r") as f:
        for line in f:
          todoList.append(line.strip())
except FileNotFoundError:
    pass

#a function for READ the ToDos
def readToDo():
  if(len(todoList) == 0):
    print("The list is empty!")
  else:
    print("The List/s is/are:\n")
    for i in range(len(todoList)):
      print(str(i+1 )+ ") " + todoList[i])

#a function for ADD a ToDo
def addToDo():
  todoList.append(input("Enter the To-do: "))
  print("\nThe To-Do ADDED successfully!\n")
  readToDo()

#a function for UPDATE a ToDo
def updateToDo():
  indexOfTodo = (int(input("Enter thier Serial number to UPDATE: "))- 1)
  todoList[indexOfTodo] = input("Enter updated ToDo: ")
  print("\nThe To-Do UPDATED successfully!\n")
  readToDo()

#a function for DELETE a ToDo
def deleteToDo():
  todoList.pop(int(input("Enter thier Serial number to DELETE: "))- 1)
  
  print("\nThe data was DELETED succssfully!\n")
  readToDo()

#a function for CLEAR a ToDo
def clearToDo():
  todoList.clear()

  print("\nThe data was CLEAR succssfully!\n")
  readToDo()



#it is a function for select the oprations such as READ, WRITE, UPADTE, DELETE, and EXIT
def selection():

  print("\n1 stands for ADD To-Do\n2 stands for UPDATE To-Do\n3 stands for READ To-Dos\n4 stands for DELETE To-Do\n5 for CLEAR all To-Dos\n6 for EXIT from Terminal\n")

  #"want" is a variable that stores user input for performing operation
  want = int(input("What do you want: "))

  if(want == 1):
    addToDo()
  elif(want == 2):
    updateToDo()
  elif(want == 3):
    readToDo()
  elif(want == 4):
    deleteToDo()
  elif(want == 5):
    clearToDo()
  elif(want == 6):
    print("\nThank you!\n")
    exit()
  else:
    print("\nInvalid option selected.\n")

#it is a loop for selecting n time of oprations, it will never stop untill user is setisfied...
while(True):
  selection()
  with open("todo.txt", "w") as f:
    for i in range(len(todoList)):
      f.write(todoList[i]+"\n")