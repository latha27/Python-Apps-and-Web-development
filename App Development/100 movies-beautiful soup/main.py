from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
yc_web_page = response.text
# soup = BeautifulSoup(, 'html.parser')

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
anchor_tag = soup.find_all(name="a", class_="titlelink")

article_text = []
article_link = []
for article in anchor_tag:
    article_text.append(article.get_text())
    article_link.append(article.get("href"))
print(article_text)
print(article_link)
# upvote_tag = [score.get_text() for score in soup.find_all(name="span", class_="score")]
upvote_tag = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(upvote_tag)

# upvote_list = []
# for upvote in upvote_tag:
#    upvote_list.append(int(upvote.split()[0]))
#print(upvote_list)
#temp = 0
#link = 0
#text = 0
##for i in range(len(upvote_tag)):
#    for j in range(i):
#        if temp < upvote_tag[i] and upvote_tag[i] < upvote_tag[j]:
#            temp = upvote_tag[j]
#            link = article_link[j]
#            text = article_text[j]
#        elif temp < upvote_tag[i] and upvote_tag[j] < upvote_tag[j]:
#            temp = upvote_tag[i]
#            link = article_link[i]
#            text = article_text[i]
#        else:
#            temp
#print(temp)
#print(link)
#print(text)

max_upvote = max(upvote_tag)
# print(index(max_upvote))

index_upvote = upvote_tag.index(max_upvote)
print(index_upvote)
index_text = article_text[index_upvote]
print(index_text)
index_link = article_link[index_upvote]
print(index_link)