# ✅ To-Do List Application (Python)

This is a simple **console-based To-Do List application** built using Python.  
It allows the user to **add tasks, view tasks, and remove tasks**, and all tasks are stored permanently in a **text file (`tasks.txt`)**.

---

## 🎯 Objective
- Practice **Python basics**
- Understand how to use **lists** for storing multiple data values
- Learn **file handling** using `open()`, `read()`, and `write()`
- Develop an **interactive CLI (Command Line Interface)** application

---

## 🛠️ Features
| Feature | Description |
|--------|-------------|
| Add Task | Add a new task to the list and store it in the file |
| View Tasks | Display all saved tasks |
| Remove Task | Delete a task by selecting its number |
| Persistent Storage | Tasks remain saved even after program exit |

---

## 💻 How It Works
The program stores tasks in a file named **`tasks.txt`**.

- When the program starts → it loads tasks from the file  
- When a task is added → it writes the task to the file  
- When a task is removed → it updates the file  

This ensures tasks are **NOT lost** even after closing the application.

---

## 📌 Requirements
- Python 3.x
- Works on Windows, Mac, and Linux

---

## ▶️ How to Run
1. Download or clone the repository
2. Open terminal / command prompt in the project folder
3. Run:

```bash
python todo.py

📁 ToDo-Application
 │
 ├── todo.py        # Main Python Program
 ├── tasks.txt      # Auto-created file to store tasks
 └── README.md      # Project Documentation

##📝 Sample Output

==== TO-DO LIST MENU ====
1. View Tasks
2. Add Task
3. Remove Task
4. Exit
Choose an option:

##🧠 What I Learned

How to handle files in Python (read, write)

How lists store multiple values and update dynamically

How to create menus and take user input

How to structure a Python project cleanly

##📜 License

This project is for learning and internship training purposes.
Feel free to modify and use it.

##⭐ Author

Dharani K V
Backend Developer
