from flask import Flask

# create the app
app = Flask(__name__)

# define a route
@app.route("/")
def home():
    return "Hello I am ACM🚀"

@app.route("/<username>")
def greetuser(username):
    return f"Hello {username}"
# run the server
if __name__ == "__main__":
    app.run(debug=True)

