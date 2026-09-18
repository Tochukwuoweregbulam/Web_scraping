from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.mangakakalot.gg/")

soup = BeautifulSoup(response.content, "html.parser")
content = soup.find_all("div", class_= "itemupdate first")
for div in content:
    link = div.find("a")

    if link:
        url =  link ["href"]
        print(url)