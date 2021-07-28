import requests
from bs4 import BeautifulSoup

#'모가디슈'의 네이버 영화  리퓨 링크
url = "http://www.alba.co.kr/?NaPm=ct%3Dkrn4uici%7Cci%3Dcheckout%7Ctr%3Dds%7Ctrx%3D%7Chk%3De8163cc534484eb557a2956fd51c47f791f971b1"
#html 소스 가져오기
res = requests.get(url)

#html 파싱
soup = BeautifulSoup(res.text, 'html.parser') #string 형식을  html 형식으로 파싱

 #리뷰 리스트
ul = soup.find('ul',class_="goodsBox")

lis = ul.find_all('li')
# print(lis)
#  리뷰 제목 출력
aa = []
count = 0
for li in lis:
    count += 1
    try:
        a = li.find('span', class_="company")
        aa.append(a.text)
    except:
        pass
print(aa)




