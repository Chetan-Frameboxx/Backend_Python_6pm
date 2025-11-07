from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")  # Not secure for production

        # Simple validation
        if not name or not email or not password:
            return "All fields are required!", 400

        # Redirect to success page with data
        return redirect(url_for("success", name=name, email=email))
    
    return render_template("register.html")

@app.route("/success")
def success():
    name = request.args.get("name")
    email = request.args.get("email")
    return render_template("success.html", name=name, email=email)

if __name__ == "__main__":
    app.run(debug=True)
