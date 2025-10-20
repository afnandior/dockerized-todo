from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = {
    "Q1": [],
    "Q2": [],
    "Q3": [],
    "Q4": []
}

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_text = request.form.get('task')
    category = request.form.get('category')
    if task_text and category in tasks:
        tasks[category].append({"text": task_text, "done": False})
    return redirect(url_for('index'))

@app.route('/delete/<category>/<int:task_id>')
def delete(category, task_id):
    if category in tasks and 0 <= task_id < len(tasks[category]):
        tasks[category].pop(task_id)
    return redirect(url_for('index'))

@app.route('/toggle/<category>/<int:task_id>')
def toggle(category, task_id):
    """Toggle checkbox status"""
    if category in tasks and 0 <= task_id < len(tasks[category]):
        tasks[category][task_id]["done"] = not tasks[category][task_id]["done"]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
