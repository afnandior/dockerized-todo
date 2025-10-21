  
# 📝 To-Do Application

## 👥 Development Team
- **Alaa Ehab Mohamed Elshenawy**  
- **Esraa Mosaad Zaky Abdelrazek**

## ⚙️ Operation Team
- **Afnan Mohamed Ali Dior**  
- **Hind Alaa Fathy Abd El Halim Ahmed**  
- **Nancy Ahmed Mostafa Mohamed**
  
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
- JSON File (for storing tasks)

---

## ⚡ How It Works
The application is a simple Flask web app that lets users manage a list of tasks.

1. When a user adds a task through the form, it’s stored in a Python list in memory.  
2. The task list is then displayed on the homepage.  
3. Each task has a **delete** button, which removes that specific task from the list.  
4. Flask handles the logic, and HTML templates display the data dynamically in the browser.

---

## 🖼️ Project Preview
![Screen 2](https://raw.githubusercontent.com/afnandior/todo-app/main/screen2.jpeg)
![Screen 1](https://raw.githubusercontent.com/afnandior/todo-app/main/screen1.jpeg)




---

## 🔗 Project Links
- **GitHub Repository:** [https://github.com/afnandior/todo-app](https://github.com/afnandior/todo-app)  
- **Docker Hub:** [https://github.com/afnandior/todo-app](https://github.com/afnandior/todo-app)

---

## 📦 Run with Docker
```bash
docker build -t todo-app .
docker run -p 5000:5000 todo-app
