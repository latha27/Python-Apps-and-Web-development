from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(0, 9)
    today_date = datetime.today().year
    return render_template('index.html', today=today_date)

if __name__=="__main__":
    app.run(debug=True)