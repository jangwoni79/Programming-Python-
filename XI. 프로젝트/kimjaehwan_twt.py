#pip install beautifulsoup4
#pip install lxml
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

if __name__ == '__main__':
    #김재환_트위터 가져오기
    with urlopen("https://twitter.com/KJH_officialtwt/status/1200942668907347969") as data:
        j = json.loads(data.read()) #httpResponse -> json
    html = "<html><head><meta charset='uft-8'></head><body>"
    jaehwan_titles = j["data"]["main"]["webtoonEpisodes"]    #data.webtoon.webtoonEpisodes
    for cartoon_title in jaehwan_titles:
        title = cartoon_title["title"]
        thumbnail = cartoon_title["thumbnailImage"]["url"]
        url = cartoon_title["id"]
        url = "http://webtoon.daum.net/webtoon/viewer/"+str(url)
        html+="<a href='{}'><img src='{}' />{}</a>".format(url, thumbnail, title)
    html += "</body></html>"

    outputSoup = BeautifulSoup(html, "lxml")
    prettyHtml = str(outputSoup.prettify())
    with open("취향저격 그녀.html", "w", encoding="utf-8") as f:
        f.write(prettyHtml)




