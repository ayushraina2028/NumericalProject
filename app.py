from flask import Flask, render_template
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)
app.debug = True

@app.route("/")
def homepage():
    return render_template("index.html");


if __name__ == "__main__":
    app.run(host = "0.0.0.0")