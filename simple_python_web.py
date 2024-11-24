from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h3>hello everyone </h3><br><p>This is my second website, this website was created using Python, not HTML<br>if you don't believe me you can check this code on my github</p><br><a href='https://github.com/EizenEnzu'>my github</a><br><img src='dhito.jpeg' alt='my childhood photo'width='300'height='300'>"
