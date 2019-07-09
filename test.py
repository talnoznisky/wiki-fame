import requests
import wikipedia
import pyttsx3
import pafy
import vlc
from BeautifulSoup import BeautifulSoup
from getaudio import prepare_audio

data = ["poop","poop","poop","poop","poop","poop","poop","poop",
"poop","poop","poop","poop","poop","poop","poop","poop","poop",
"poop","poop","poop","poop","poop","poop","poop","poop","poop","poop",
"poop","poop","poop","poop","poop","poop","poop","poop","poop"]

# prepare_audio()
url = "https://www.youtube.com/watch?v=zLTZPK8HhFI"
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

    # print(text)
    if player.get_state() != 6:
        text = i
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
