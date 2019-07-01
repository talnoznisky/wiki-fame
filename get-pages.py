import requests
import wikipedia
import pyttsx3
from BeautifulSoup import BeautifulSoup

topics = []
data = []

url = 'http://www.wikitrends.net/'
soup = BeautifulSoup(requests.get(url).content)

for d in soup.findAll('div', {'class':'col-md-7 col-xs-5'}):
    for b in d.findAll('b'):
        topics.append(b.contents)

for a in topics[0]:
    title = a.encode('utf-8')
    categories =  wikipedia.WikipediaPage(title=a).categories
    for i in categories:
        i.encode('utf-8')
    data.append([title,categories])

for i in topics[0:2]:
    text = ('The topic is %s and its categories are %s' %(data[0][0], ", ".join(data[0][1])))
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
