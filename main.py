from flask import Flask

app = Flask("SuperScrapper")

@app.route("/")
def home():
  return "Hello! Welcome to mi casa"

app.run(host="0.0.0.0")