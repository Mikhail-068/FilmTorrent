import requests
import json
from bs4 import BeautifulSoup
import time


HEADERS = {'Accept': '*/*',
            'user_data': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/100.0.4896.88 Safari/537.36'}

url = 'http://hd.utorr.xyz/'
html = requests.get(url, headers=HEADERS).text
site = 'http://hd.utorr.xyz'

def new_film(blok_1):
    name = block_1.find(class_='post-title').text
    date_all = block_1.find(class_='data').find_all(class_='cell')
    date = date_all[0].text
    rating = block_1.find(class_='data').find(class_='orating_res').text
    film_info = block_1.find(class_='post-story').find('td').find_all('a')
    list_info = []
    for i in film_info:
        list_info.append(i.text)

    download = block_1.find(class_='post-data').find_all('li')[-1].find('a')['href']
    link = requests.get(download, headers=HEADERS).text
    soup = BeautifulSoup(link, 'lxml')
    tr = soup.find('table', class_='res85gtj').find('tbody').find_all('tr')
    td = tr[-1].find_all('td')
    torrent = f"{site}{td[-1].find('a')['href']}"
    return name, date, rating, list_info, torrent


list_name = ['']
soup = BeautifulSoup(html, 'lxml')
block_film = soup.find('div', id='dle-content').find_all(class_='post')

all = []
for block_1 in block_film:
    name, date, rating, list_info, download = new_film(block_1)

    dict_ = {}
    item_text = ['Фильмы', 'Дата', 'Рейтинг', 'Инфо', 'Скачать']
    item_data = [name.strip(), date, rating, list_info, download]

    for i in range(5):
        dict_[item_text[i]] = item_data[i]
    all.append(dict_)



with open(f"Data/Page {time.strftime('%H.%M %d.%b')}.json", "w") as file:
    json.dump(all, file, indent=2, ensure_ascii=False)

with open(f"filmtorrent.json", "w") as file:
    json.dump(all, file, indent=2, ensure_ascii=False)
