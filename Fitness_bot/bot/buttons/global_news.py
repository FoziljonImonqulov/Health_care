from bs4 import BeautifulSoup
import time
import requests

response = requests.get('https://www.everydayhealth.com/news/')

html = response.content.decode()

soup = BeautifulSoup(html, 'html.parser')

last_news = []

anchor_element = soup.find('a', target='_self')


def news__():
    for i in soup.find_all('div', {'class': 'category-index-article__content'})[:5]:
        name = i.find('a', {'class':'cr-anchor cr-anchor--mounted'})

        t = i.find('div', {'class': 'category-index-article__dek'})
        title = t.text
        link = i.a['href']
        a = i.find('span', {'class': 'category-index-article__author'})
        author = a.text
        date = i.find('span', {'class': 'category-index-article__date'})
        posted_date = date.text
        image_link = i.find()
        print(image_link)




news__()
