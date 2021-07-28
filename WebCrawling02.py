import requests
from bs4 import BeautifulSoup
url = 'https://alba.co.kr'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
#beuatifulsoup 형식을 사용하여 .find() 사용 가능
#titles = soup.select('#MainSuperBrand > ul > li > a > span.company')
titles = soup.find('div',id='MainSuperBrand').find('ul',class_="goodsBox").find_all('li',class_='impact')
for x in titles:
    p = x.find('span',class_='company')
    print(p.text)
# for i in titles: 
#     print(i.text)