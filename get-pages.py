import requests
import wikipedia
from BeautifulSoup import BeautifulSoup


links = []
topics = []
data = []

url = 'http://www.wikitrends.net/'
soup = BeautifulSoup(requests.get(url).content)


for d in soup.findAll('div', {'class':'col-md-7 col-xs-5'}):
    for b in d.findAll('b'):
        topics.append(b.contents)

for a in topics[0]:
    title = a
    categories =  wikipedia.WikipediaPage(title=a).categories
    data.append([title,categories])

print data
