from flask import Flask, render_template, request, redirect, url_for
from api_handler import currency_converter
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        from_currency = request.form["from-currency"]
        to_currency = request.form["to-currency"]
        currency_amount = request.form["amount"]
        result = currency_converter(from_currency, to_currency, currency_amount)
        return redirect(url_for("home", result=result))
    return render_template("index.html", result=request.args["result"])


@app.route("/result")
def exchange_result():
    return request.args["result"]


if __name__ == "__main__":
    app.run(debug=True)