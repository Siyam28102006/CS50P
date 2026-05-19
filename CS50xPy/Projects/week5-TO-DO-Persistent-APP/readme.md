# Persistent To-Do App

A command line task manager that saves and loads tasks from a file.

## Features
- Add multiple tasks at once
- Delete task by number
- View all current tasks
- Clear entire list with confirmation
- Save tasks to a .txt file
- Load tasks from a saved file
- Input validation throughout

## How to run
python todo.py

## Example

Save Tasks as : mytasks

-----MENU-----
1 : Add task
2 : Delete task
3 : View Tasks
4 : Clear List
5 : Load
6 : Save file
7 : Exit

Select A Task to Proceed With : 1
Enter Amount of tasks to be added : 2
Enter a task 1: Buy groceries
Enter a task 2: Study Python
2 Tasks were Added Successfully

Select A Task to Proceed With : 6
(tasks saved to mytasks.txt)

Select A Task to Proceed With : 5
(tasks loaded from mytasks.txt)

## How saving works
- Tasks are saved as plain text, one task per line
- Load option reads the file and restores your list
- Closing the app without saving will lose unsaved tasks

## What I learned
- File I/O with open(), read(), write()
- Persistent data between sessions
- Separating save and load logic into functions
- Real world app feel with file-based memory
