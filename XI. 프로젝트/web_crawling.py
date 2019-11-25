#pip install beautifulsoup4
#pip install lxml

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__':
    #네이버 웹툰 > 이츠마인 제목 가져오기
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=710760&weekday=wed")
    soup = BeautifulSoup(data, "lxml") #httpResponse -> HTML
    # print(soup)
    html = "<html><head><meta charset='uft-8'></head><body>"
    cartoon_titles = soup.find_all("td",attrs={"class":"title"}) #<td class = "title">...</td>
    for cartoon_title in cartoon_titles:                          #cartoon_titles[:2]
        title = cartoon_title.find("a").text                      #<a href>text</a>
        link = cartoon_title.find("a").get("href")               #텍스트 가져오기
        link = "https://comic.naver.com" + link
        # print(title)
        # print(link)
        html+="<a href = '{}'>{}</a><br />".format(link, title)       #<a href = 'link'>title</a>
    html+="</body></html>"
    # print(html)
    outputSoup = BeautifulSoup(html, "lxml")
    prettyHtml = str(outputSoup.prettify())
    with open("이츠마인.html", "w", encoding = "utf-8") as f:
        f.write(prettyHtml)