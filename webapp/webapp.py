# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def greetings():
    return "Hey, how's it going?"

if __name__ == '__main__':
    app.run(debug=True)

