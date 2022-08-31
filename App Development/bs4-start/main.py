from bs4 import BeautifulSoup
import lxml
with open("website.html", encoding='cp437') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)
all_anchor_tag = soup.find_all(name="a")
for tag in all_anchor_tag:
    # print(tag.getText())
    print(tag.get("href"))
