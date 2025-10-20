rom flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# مسار حفظ المهام
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
DATA_FILE = os.path.join(DATA_DIR, 'tasks.json')


def load_tasks():

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    return {"Q1": [], "Q2": [], "Q3": [], "Q4": []}


def save_tasks(tasks):
   
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)



tasks = load_tasks()


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add():
    task_text = request.form.get('task')
    category = request.form.get('category')
    if task_text and category in tasks:
        tasks[category].append({"text": task_text, "done": False})
        save_tasks(tasks)
    return redirect(url_for('index'))


@app.route('/delete/<category>/<int:task_id>')
def delete(category, task_id):# تحميل المهام عند بدء التشغيل
    if category in tasks and 0 <= task_id < len(tasks[category]):
        tasks[category].pop(task_id)
        save_tasks(tasks)
    return redirect(url_for('index'))


@app.route('/toggle/<category>/<int:task_id>')
def toggle(category, task_id):
    """تبديل حالة المهمة (تم / لم تتم)"""
    if category in tasks and 0 <= task_id < len(tasks[category]):
        tasks[category][task_id]["done"] = not tasks[category][task_id]["done"]
        save_tasks(tasks)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

