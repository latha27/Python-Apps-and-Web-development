from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2")
movie_web_page = response.text

soup = BeautifulSoup(movie_web_page, 'html.parser')
movie_titles = [movie.get_text() for movie in soup.find_all(name="h3", class_="title")]
movie_titles.reverse()


with open("movies.txt", 'a', encoding='utf-8') as data:
    for movie in movie_titles:
        data.write(f"{movie}\n")













