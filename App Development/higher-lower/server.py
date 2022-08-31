from flask import Flask
from random import randint

app = Flask(__name__)

number = randint(0, 9)

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

@app.route('/<int:numb>')
def hello(numb):
    if number > numb:
        return f'<h1 style="color:blue;">{numb} is too low</h1>' \
               '<img src="https://i.giphy.com/media/jD4DwBtqPXRXa/giphy.webp">'
    elif number < numb:
        return f'<h1 style="color:red;">{numb} is too high</h1>'\
               '<img src="https://i.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.webp">'
    elif number == number:
        return f'<h1 style="color:green;">{numb} is right</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'



if __name__ == "__main__":
    app.run(debug=True)