import requests as rq
from bs4 import BeautifulSoup
import re
import pandas as pd

def Get_news(url0):
    page0 = rq.get(url0)
    soup0 = BeautifulSoup(page0.text, features="html.parser")
    date_info = str(soup0.find_all('time'))
    date = ''.join(re.findall(r'\d+\s[а-я]+', date_info)) + ' 2022'
    title = str(soup0.find_all('title')[0])[7:-29]
    author_info = str(soup0.find_all('div', class_="article-authors__info"))
    author = ''.join(re.findall(r"[А-Я][а-я]+\s[А-Я][а-я]+", author_info))
    text_list = soup0.find_all('p', class_="box-paragraph__text")
    text = []
    for i in text_list:
      text.append(i.text)
    text_final = ' '.join(text)
    return url, date, title, author, text_final


url = 'https://www.vedomosti.ru/ecology'
page = rq.get(url)
soup = BeautifulSoup(page.text, features="html.parser")
urls = []
for link in soup.find_all('a'):
    if "/ecology/release" in link.get('href') and ('https://www.vedomosti.ru' + link.get('href')) not in urls:
        urls.append('https://www.vedomosti.ru' + link.get('href'))

links = []
for url in urls:
    page0 = rq.get(url)
    soup0 = BeautifulSoup(page0.text, features="html.parser")
    for link in soup0.find_all('a'):
        try:
            if link.get("data-vr-contentbox-url") is not None:
                links.append('https://www.vedomosti.ru' + link.get("data-vr-contentbox-url"))
        except:
            pass

news = []
for link in links:
    news0 = Get_news(link)
    news.append(news0)

df = pd.DataFrame(news)
df.head()
df.columns = ['Ссылка', 'Дата', 'Заголовок', 'Автор', 'Текст' ]
df.to_excel('vedomosti_news.xlsx')
