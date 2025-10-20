  
# 📝 To-Do Application

## 🚀 Introduction
This project is a simple **To-Do web app** built using **Python (Flask)** and **Docker**.  
It allows users to **add**, **view**, and **delete** tasks through a web interface.  

The app runs inside a **Docker container**, making it easy to deploy and run anywhere without manually installing Python or Flask.

---

## 🧰 Tools Used
- Python (Flask)
- Docker
- HTML
- GitHub
- Json

---

## ⚡ How It Works
The application is a simple Flask web app that lets users manage a list of tasks.

1. When a user adds a task through the form, it’s stored in a Python list in memory.  
2. The task list is then displayed on the homepage.  
3. Each task has a **delete** button, which removes that specific task from the list.  
4. Flask handles the logic, and HTML templates display the data dynamically in the browser.

---

## 🖼️ Project Preview
![Todo App Screenshot](https://github.com/afnandior/todo-app/blob/main/picture.jpg?raw=true)


---

## 🔗 Project Links
- **GitHub Repository:** [https://github.com/afnandior/todo-app](https://github.com/afnandior/todo-app)  
- **Docker Hub:** [https://github.com/afnandior/todo-app](https://github.com/afnandior/todo-app)

---

## 📦 Run with Docker
```bash
docker build -t todo-app .
docker run -p 5000:5000 todo-app
