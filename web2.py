# web2.py
#웹서버에 요청
import urllib.request
#크롤링
from bs4 import BeautifulSoup

data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
#검색이 용이한 객체
soup = BeautifulSoup(data, "html.parser")

#ctrl + /
# <td class="title">
# 		<a href="/webtoon/detail? ">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>
cartoons = soup.find_all("td", class_="title")

print("갯수:{0}".format(len(cartoons)))
#10개중에 0번을 찾아서 다시 검색 ==> 문자열 리턴 
title = cartoons[0].find("a").text
link = cartoons[0].find("a")["href"]
print(title)
print(link)

for item in cartoons:
    title = item.find("a").text
    print( title.strip())