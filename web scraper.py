import requests
from bs4 import BeautifulSoup
import NavigableString

url="https://www.yellowpageskolkata.com/cat_h/h_Hotels.html"
r=requests.get(url)

soup = BeautifulSoup(r.content)

links=soup.find_all("a")

for link in links:
	if "http" in link.get("href"):
		print "<a href='%s'>'%s'</a>" %(link.get("href"),link.text)


g_data = soup.find_all("div",{"align":"right"})


for item in g_data:
	print item.contents[0].find_all("a",{"color":"#575757"})
#print item.contents[1]

	




