import requests
import bs4
from lxml import etree


target_url = input().strip() #urlの入力
res = requests.get(target_url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.content, "lxml")

with open('test.html', 'w') as file:
    file.write(soup.get_text())

search_target = input().strip() #検索ワード入力

for line in open('test.html'):
    if search_target in line:
        print(line)