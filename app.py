from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


files = []

@app.route("/")
def index():
    return render_template("index.html", files=files)

@app.route("/upload", methods=["POST"])
def upload():
    filename = request.form.get("filename")
    if not filename:
        return "Filename is required", 400
    if filename in files:
        return "File already exists", 400
    files.append(filename)
    return redirect(url_for("index"))

@app.route("/update", methods=["POST"])
def update():
    old_name = request.form.get("old_name")
    new_name = request.form.get("new_name")
    if old_name in files and new_name:
        files[files.index(old_name)] = new_name
    return redirect(url_for("index"))

@app.route("/delete/<filename>")
def delete(filename):
    if filename in files:
        files.remove(filename)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
