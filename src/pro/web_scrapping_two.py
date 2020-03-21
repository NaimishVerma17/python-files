import requests
import bs4

req = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
print(req.text)

soup = bs4.BeautifulSoup(req.text, 'lxml')

headlines = soup.select('.mw-headline')
print(headlines)

for h in headlines:
    print(h.getText())
