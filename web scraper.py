import requests
from bs4 import BeautifulSoup

url="https://www.yellowpages.com/los-angeles-ca/coffee-shops"
r=request.get(url)

soup = BeautifulSoup(r.content)

links=soup.find_all("a")

for link in links:
	if "http" in link.get("href"):
		print "<a href='%s'>'%s'</a>" %(link.get("href"),link.text)


g_data = soup.find_all("div",{"class":"info-section info-secondary"})


for item in g_data:
	print item.text

	




