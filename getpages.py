import requests
import wikipedia
import pyttsx3
import pafy
import vlc
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
    categories = wikipedia.WikipediaPage(title=title).categories[0:6]
    categories = [i.encode('utf-8') for i in categories]
    categories = ", ".join(categories)
    data.append([title,categories])

# prepare_audio()
url = "https://www.youtube.com/watch?v=xy9r0vhOVpk"
video = pafy.new(url)
best = video.getbest()
playurl = best.url

Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.audio_set_volume(77)
player.play()



# turn reader off when audio is over:
# https://stackoverflow.com/questions/49141463/how-to-wait-until-a-sound-file-ends-in-vlc-in-python-3-6
# https://www.olivieraubert.net/vlc/python-ctypes/doc/
for i in data:
    text = ('The topic is {topic} and its categories are {cats}'.format(topic=i[0],cats=i[1]))
    # print(text)
    while player.get_state() != 6:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
