# Lecture 31: Introduction to Flask

##  Learning Objectives
By the end of this lecture, students will be able to:
 Understand what Flask is and why it is used.  
 Install Flask and set up a development environment.  
 Create their first Flask application.  
 Understand and implement basic routing in Flask.  

---

## 1. What is Flask?
Flask is a lightweight web framework for Python.  

It is called a **microframework** because it does not include tools like database abstraction or form validation by default – you can add them as needed.  

**Use cases:**
- Building small to medium web apps
- REST APIs
- Rapid prototyping

**Key Features:**
- Minimalistic and simple
- Built-in development server and debugger
- Supports templating (Jinja2)
- Easy integration with databases

---

## 2. Installing Flask
Make sure Python is installed:
```bash
python --version
```

Install Flask using pip:
```bash
pip install flask
```

Verify installation:
```bash
python -m flask --version
```

**Tip:** Use a virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
pip install flask
```

---

## 3. Project Structure
Minimal Flask project:
```
project/
│
├── app.py       # Main Flask application
├── templates/   # HTML templates
└── static/      # CSS, JS, images
```

*Note: For Lecture 31, we will only create `app.py`.*

---

## 4. Creating Your First Flask App

**Step 1:** Create `app.py`
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

**Step 2:** Run the app
```bash
python app.py
```

Open browser → `http://127.0.0.1:5000/`  

Output: **Hello, Flask!**  

**Explanation:**
- `Flask(__name__)` → creates app instance
- `@app.route("/")` → defines a route
- `home()` → function that returns content
- `app.run(debug=True)` → starts server with auto-reload

---

## 5. Routing Basics
**Route:** URL pattern that maps to a Python function (view function).  

**Example routes:**
```python
@app.route("/")
def home():
    return "Welcome to Home Page!"

@app.route("/about")
def about():
    return "About Page"

@app.route("/contact")
def contact():
    return "Contact Page"
```

**Dynamic Routes:**
```python
@app.route("/user/<name>")
def greet_user(name):
    return f"Hello, {name}!"
```

- `<name>` → dynamic part of URL  
- Can capture strings, integers, etc.:  
```python
@app.route("/post/<int:id>")
def show_post(id):
    return f"Post ID: {id}"
```

**Routing Tips:**
- Routes must be unique
- Routes can have trailing slashes `/`
- Use meaningful URLs

---

## 6. Flask Server Options
- `debug=True` → enables hot reload and error display
- Default host → `127.0.0.1` (localhost)
- Default port → `5000`

**Custom port example:**
```python
app.run(debug=True, host='0.0.0.0', port=8000)
```

---

## 7. Common Errors & Troubleshooting
- **ModuleNotFoundError: No module named 'flask'** → check pip install & virtual environment  
- **Address already in use** → change port or kill existing process  
- **IndentationError** → Python is indentation-sensitive  

---

## 8. Practice Exercises
1. Create a Flask app with 3 routes: `/`, `/about`, `/contact`. Display unique text for each route.  
2. Add a dynamic route `/greet/<username>` that greets the user by name.  
3. Run the app with a custom port (`8000`) and test it in a browser.  
