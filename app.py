from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# File where tasks will be saved
DATA_FILE = 'data/tasks.json'

# ---------------------------------------------
# Load tasks from the file when the app starts
# ---------------------------------------------
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {"Q1": [], "Q2": [], "Q3": [], "Q4": []}
    return {"Q1": [], "Q2": [], "Q3": [], "Q4": []}

# ---------------------------------------------
# Save tasks to the file
# ---------------------------------------------
def save_tasks(tasks):
    os.makedirs('data', exist_ok=True)  # Create 'data' folder if it doesn't exist
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# ---------------------------------------------
# Load tasks when the app starts
# ---------------------------------------------
tasks = load_tasks()

# ---------------------------------------------
# Home route - display tasks
# ---------------------------------------------
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# ---------------------------------------------
# Add a new task
# ---------------------------------------------
@app.route('/add', methods=['POST'])
def add():
    task_text = request.form.get('task')
    category = request.form.get('category')
    if task_text and category in tasks:
        tasks[category].append({"text": task_text, "done": False})
        save_tasks(tasks)  # Save after adding
    return redirect(url_for('index'))

# ---------------------------------------------
# Delete a task
# ---------------------------------------------
@app.route('/delete/<category>/<int:task_id>')
def delete(category, task_id):
    if category in tasks and 0 <= task_id < len(tasks[category]):
        tasks[category].pop(task_id)
        save_tasks(tasks)  # Save after deleting
    return redirect(url_for('index'))

# ---------------------------------------------
# Toggle task status (done / not done)
# ---------------------------------------------
@app.route('/toggle/<category>/<int:task_id>')
def toggle(category, task_id):
    if category in tasks and 0 <= task_id < len(tasks[category]):
        tasks[category][task_id]["done"] = not tasks[category][task_id]["done"]
        save_tasks(tasks)  # Save after toggling
    return redirect(url_for('index'))

# ---------------------------------------------
# Run the Flask application
# ---------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
