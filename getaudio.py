import pafy
import vlc

def prepare_audio():
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


if __name__ == "__main__":
    prepare_audio()
