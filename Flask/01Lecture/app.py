from flask import Flask,  render_template


app = Flask(__name__)

@app.route("/")
def home():
    #  return "Welcome to Home Page!"
    return render_template('home.html')
 
@app.route("/about")
def about():
    # return "About Page"
    return render_template('about.html')
    

@app.route("/contact")
def contact():
    # return "Contact Page"
    return render_template('contact.html')
    

@app.route("/user/<name>")
def greet_user(name):
    return f"Hello, {name}!"


@app.route("/post/<int:id>")
def show_post(id):
    return f"Post ID: {id}"

if __name__ == "__main__":
    app.run(debug=True)