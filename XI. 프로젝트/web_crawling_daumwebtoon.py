#pip install beautifulsoup4
#pip install lxml
from urllib.request import urlopen
import json

if __name__ == '__main__':
    #네이버 웹툰 > 취향저격 그녀 제목 가져오기
    with urlopen("http://webtoon.daum.net/data/pc/webtoon/view/favorite") as data:
        j = json.loads(data.read()) #httpResponse -> json
    # print(j["data"]["webtoon"]["weebtooneEpisodes"][3]["title"])
    cartoon_titles = j["data"]["webtoon"]["webtoonEpisodes"]    #data.webtoon.webtoonEpisodes
    for cartoon_title in cartoon_titles:
        title = cartoon_title["title"]
        print(title)
        thumbnail = cartoon_title["thumbnailImage"]["url"]
        print(thumbnail)
        url = cartoon_title["id"]
        url = "http://webtoon.daum.net/webtoon/viewer/"+str(url)
        print(url)














    # html = "<html><head><meta charset='uft-8'></head><body>"
    # cartoon_titles = soup.find_all("td",attrs={"class":"title"}) #<td class = "title">...</td>
    # for cartoon_title in cartoon_titles:                          #cartoon_titles[:2]
    #     title = cartoon_title.find("a").text                      #<a href>text</a>
    #     link = cartoon_title.find("a").get("href")               #텍스트 가져오기
    #     link = "https://comic.naver.com" + link
    #     # print(title)
    #     # print(link)
    #     html+="<a href = '{}'>{}</a><br />".format(link, title)       #<a href = 'link'>title</a>
    # html+="</body></html>"
    # # print(html)
    # outputSoup = BeautifulSoup(html, "lxml")
    # prettyHtml = str(outputSoup.prettify())
    # with open("이츠마인.html", "w", encoding = "utf-8") as f:
    #     f.write(prettyHtml)