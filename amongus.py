# TODO part 1. import module
from bs4 import BeautifulSoup
import requests
import urllib.parse

# TODO part 2. 네이버에 '어몽 어스'대하여 뉴스 검색
# hint. urllib 와 beautifulsoup 를 이용한다.
key_word = urllib.parse.quote("어몽 어스")
url = "https://search.naver.com/search.naver?where=news&query=" + \
    key_word + "&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=" + \
    "2020.08.04&de=2020.08.18"
webpage = requests.get(url)
soup = BeautifulSoup(webpage.content, "html.parser")

# TODO part 3. 검색된 뉴스들에 대하여 제목을 ‘news_title’ 에 저장한다.
news_title = []
for t in soup.find_all('a', {'class': "_sp_each_title"}):
    title = t.get_text()
    news_title.append(title)

# TODO part 4. 검색된 뉴스들 중에서 제목에 ‘폴 가이즈’를 가진 제목을 found 에 저장한다.
found = []
for t in soup.find_all('a', {'class': "_sp_each_title"}):
    title = t.get_text()
    if '폴 가이즈' in title:
        found.append(title)

# TODO part 5. 검색된 뉴스들의 개수와 found을 출력한다.
news_title_len = len(news_title)
found_len = len(found)
print(news_title_len)
print(found_len)
