import requests
import wikipedia
import pyttsx3
from BeautifulSoup import BeautifulSoup
from getaudio import prepare_audio

topics = []
data = []

url = 'http://www.wikitrends.net/'
soup = BeautifulSoup(requests.get(url).content)

for d in soup.findAll('div', {'class':'col-md-7 col-xs-5'}):
    for b in d.findAll('b'):
        topics.append(b.contents)

for a in topics:
    title = str(a[0])
    categories = wikipedia.WikipediaPage(title=title).categories
    categories = [i.encode('utf-8') for i in categories]
    categories = ", ".join(categories)
    data.append([title,categories])

prepare_audio()

for i in data:
    text = ('The topic is {topic} and its categories are {cats}'.format(topic=i[0],cats=i[1]))
    # print(text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
