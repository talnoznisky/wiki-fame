import threading
import requests
import wikipedia
import pyttsx3
import pafy
import vlc
from BeautifulSoup import BeautifulSoup

topics = []
data = []
Instance = vlc.Instance()
player = Instance.media_player_new()

def play_audio(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

def intro():
    text = """
    good evening. this is a prelude to hold your attention
    while I download a list of the most viewed wikipedia
    articles from the last hour. Then I will attach some categorical definitions
    associated with each topic. I am hard at work on this task as we speak.
    And once I am done compiling that information I will quote unquote sing it to you.
    I will commence my song now.
    """
    play_audio(text)

def outro():
    text = """
    Oops! I got carried away and overran my musical framing device.
    Or did I? You decide. And whatever you choose, I am thankful for your audience.
    Have a splendid evening.
    """
    play_audio(text)
    text = ""
    play_audio(text)

def get_data():
    url = 'http://www.wikitrends.net/'
    soup = BeautifulSoup(requests.get(url).content)
    # scrape topics from wikitrends
    for d in soup.findAll('div', {'class':'col-md-7 col-xs-5'}):
        for b in d.findAll('b'):
            topics.append(b.contents)

    # pass topics to wikipedia api and get categories
    for a in topics:
        title = str(a[0])
        categories = wikipedia.WikipediaPage(title=title).categories[0:6]
        categories = [i.encode('utf-8') for i in categories]
        categories = ", ".join(categories)
        data.append([title,categories])


# turn reader off when audio is over:
# https://stackoverflow.com/questions/49141463/how-to-wait-until-a-sound-file-ends-in-vlc-in-python-3-6
# https://www.olivieraubert.net/vlc/python-ctypes/doc/

def get_video():
    url = "https://www.youtube.com/watch?v=xy9r0vhOVpk"
    # url = "https://www.youtube.com/watch?v=kjI-JaRWG7s"
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.audio_set_volume(77)

def play():
    player.play()
    for i in data:
        if player.get_state() != 6:
            text = ('The topic is {} and its categories are {}'.format(i[0],i[1]))
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()

t1 = threading.Thread(target=get_data)
t2 = threading.Thread(target=get_video)

t1.start()
t2.start()

intro()
play()
outro()
