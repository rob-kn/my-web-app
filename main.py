from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("profile.html", name="Rob")


if __name__ == "__main__":
    app.run(debug=True)
