#  Flask CRUD App — Code Explanation

## 1. Importing Required Modules
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
```

- **Flask** – Framework to build web applications.  
- **render_template** – Used to load HTML templates.  
- **request** – Used to access data from HTML forms (like form input values).  
- **redirect** – Redirects users to another route after an action (like after adding a task).  
- **url_for** – Dynamically generates the URL for a function (so we don’t hardcode routes).  
- **SQLAlchemy** – ORM (Object Relational Mapper) for working with databases easily.

---

##  2. Initialize Flask App
```python
app = Flask(__name__)
```
Creates the main Flask application object — this represents your web app.

---

##  3. Database Configuration
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
```

- Tells Flask to use a **SQLite database** named `tasks.db` stored locally.  
- Disables modification tracking (to save memory).  
- Initializes the `db` object — this will be used to interact with the database.

---

##  4. Database Model (Table Definition)
```python
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Task {self.id} - {self.title}>"
```

Defines a **Task table** in the database:

- **id** → Integer column, primary key (unique ID for each task).  
- **title** → String column, can’t be empty (`nullable=False`).  
- `__repr__()` → For debugging — shows task info when printed.

---

##  5. Create Database Tables
```python
with app.app_context():
    db.create_all()
```

This ensures the database and its tables are created before the app runs.

`app.app_context()` allows SQLAlchemy to access the app configuration properly.

---

##  6. Routes

### (a) Home Route — View All Tasks
```python
@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)
```

- Fetches all tasks from the database.  
- Renders an HTML page (`index.html`) and passes all tasks to it.

➡️ The template can loop through `tasks` and display them.

---

### (b) Add Task Route
```python
@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    new_task = Task(title=title)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))
```

- Gets the task title from the submitted HTML form (`request.form`).  
- Creates a new `Task` object and adds it to the database.  
- Commits (saves) the change.  
- Redirects back to the home page to show the updated list.

---

### (c) Delete Task Route
```python
@app.route('/delete/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))
```

- Takes a task **id** from the URL (like `/delete/3`).  
- Fetches that task from the database.  
- Deletes it and commits the change.  
- Redirects back to the homepage.

If the task doesn’t exist, `get_or_404()` automatically shows a **404 error page**.

---

## (d) Update Task Route (Optional)
```python
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.title = request.form['title']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', task=task)
```

- Shows an edit form with the current task data (GET).  
- Updates the record when the form is submitted (POST).  
- Saves changes and redirects to the home page.

---

##  7. Run the App
```python
if __name__ == '__main__':
    app.run(debug=True)
```

- Runs the Flask app in debug mode.  
- Debug mode automatically reloads the app when you change code and provides helpful error messages.

---

##  Summary

| Part | Purpose |
|------|----------|
| Flask setup | Initializes the web app |
| SQLAlchemy config | Connects to the database |
| Task model | Defines the table structure |
| `/` route | Displays all tasks |
| `/add` route | Adds a new task |
| `/delete/<id>` route | Deletes a task |
| `/update/<id>` route | Updates a task |
| `app.run()` | Starts the application |
