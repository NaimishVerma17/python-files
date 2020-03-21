import requests
import bs4

req = requests.get('https://evoqys.in')
# print(req.text)

soup = bs4.BeautifulSoup(req.text, 'lxml')
print(soup.title)
print(soup.title.getText())