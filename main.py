from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operator = request.form["operator"]
            if operator == "+": result = num1 + num2
            elif operator == "-": result = num1 - num2
            elif operator == "*": result = num1 * num2
            elif operator == "/": result = num1 / num2
            else: result = "Operator tidak valid"
        except Exception as e:
            result = f"Error: {e}"
    return render_template("index.html", result=result)

# BAGIAN INI HARUS ADA DI PALING BAWAH
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
