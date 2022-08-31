from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/guess/<name>')
def home(name):

    response = requests.get(f"https://api.genderize.io?name={name}")
    data_gender = response.json()["gender"]
    response = requests.get(f"https://api.agify.io?name={name}")
    data_age = response.json()["age"]
    return render_template('index.html', user_input=name, gender=data_gender, age=data_age)

@app.route('/blog')
def blog():
    url = "https://api.npoint.io/b4878f155dd0032defd2"
    response = requests.get(url)
    all_blogs = response.json()
    return render_template('blog.html', posts=all_blogs)


if __name__ =="__main__":
    app.run(debug=True)