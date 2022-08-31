from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def inner():
        x = function()
        return f'<b>{x}</b>'
    return inner

def make_emphasis(function):
    def inner():
        x = function()
        return f'<em>{x}</em>'
    return inner
def make_underline(function):
    def inner():
        x = function()
        return f'<u>{x}</u>'
    return inner




@app.route('/')
@make_bold
@make_emphasis
@make_underline
def say_hello():
    return "Hello World"

@app.route('/bye')
def bye():
    return "Bye!"

if __name__ == "__main__":
    app.run(debug=True)