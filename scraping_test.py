import requests
from bs4 import BeautifulSoup as soup

r = requests.get("https://www.barclayhedge.com/research/indices/btop/index.html")

soup_content = soup(r.content)

print(soup_content.prettify)

for link in soup_content.find_all("form"):
	print(link.get("action"))

g_data = soup_content.find_all("input", {"name":"imageField"})

for item in g_data:
	print(item.get("src"))