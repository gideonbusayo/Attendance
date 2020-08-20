from flask import Flask, redirect, render_template, request

app = Flask(__name__)
attendances = []
@app.route("/")
def attendance():
    return render_template ("tasks.html", attendances=attendances)

@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template ("add.html")
    else:
        todo = request.form.get("task")
        attendances.append(todo)
        return redirect("/")
