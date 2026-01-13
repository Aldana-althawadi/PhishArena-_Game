from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Simulate to Educate – Phishing Training System"

if __name__ == "__main__":
    app.run(debug=True)
