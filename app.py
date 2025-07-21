from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return render_template("index.html")  

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        if password != confirm:
            return "Passwords do not match", 400

        if username in users:
            return "User already exists", 400

        users[username] = {"email": email, "password": password}
        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = users.get(username)
        if user and user["password"] == password:
            return redirect("/dashboard")
        else:
            return "Invalid credentials", 401

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("home.html")


@app.route("/cars")
def cars():
    return render_template("cars.html")

@app.route("/bikes")
def bikes():
    return "<h1>Bikes Page</h1>"

@app.route("/carspares")
def carspares():
    return "<h1>Car Spare Parts</h1>"

@app.route("/bikespares")
def bikespares():
    return "<h1>Bike Spare Parts</h1>"

if __name__ == "__main__":
    app.run(debug=True)
