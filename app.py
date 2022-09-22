from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images

images = [
    "https://media2.giphy.com/media/cfuL5gqFDreXxkWQ4o/giphy.gif?cid=ecf05e4760qvxlezzdwgf3ye088c9dq20f2pazwrznas2md8&rid=giphy.gif&ct=g"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")