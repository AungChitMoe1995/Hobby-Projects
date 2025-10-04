from flask import Flask, render_template

# create the app
app = Flask(__name__)

# define a route


@app.route("/")
def home():
    items = ['Apple', 'Banana', 'Cherry']
    return render_template("home.html", title= "Home Page", items = items)

@app.route("/about")
def about():
    return render_template("about.html", title = "About")


@app.route("/<username>")
def greetuser(username):
    capatilized_username = username.upper()
    greetwithusername = f"Hello {capatilized_username}"
    return """
    <h1>greetwithusername</h1>
    """

@app.route("/multiply/<int:a>/<int:b>")
def multiply(a, b):
    result = a*b
    return f"The result is {result}."


# run the server
if __name__ == "__main__":
    app.run(debug=True)

