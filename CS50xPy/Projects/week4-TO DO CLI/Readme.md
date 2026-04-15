# CLI To-Do App

A command line task manager built in Python.

## Features
- Add multiple tasks at once
- View all current tasks
- Delete a specific task by name
- See total tasks remaining
- Clear entire list with confirmation prompt
- Input validation throughout
- Prevents empty or whitespace-only tasks

## How to run
python Note Taker.py

## Example

-----MENU-----
01 : Add task
02 : Delete task
03 : View Tasks
04 : Tasks Left to do
05 : Clear List
06 : Exit

Enter the Option : 1
Enter the amount of task: 2
Enter a task 1: Buy groceries
Enter a task 2: Study Python
Total 2 tasks added newly!!

Enter the Option : 3
Your tasks are :
1.Buy groceries
2.Study Python

Enter the Option : 4
Total tasks left to do : 2

Enter the Option : 2
Your tasks are :
1.Buy groceries
2.Study Python
Enter the task you want to delete: Buy groceries
Task deleted successfully.

## What I learned
- Structuring code into clean functions
- No logic in main() except function calls
- User experience thinking (.strip(), confirmation prompts)
- List methods (append, remove, clear)
- Input validation and edge case handling
