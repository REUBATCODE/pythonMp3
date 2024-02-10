from pytube import YouTube
from moviepy.editor import *

def downloadNconvert(url):
    #Downloading the video
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    end = video.download()

    #Converting the video to mp3
    name_mp3 = yt.title + ".mp3"
    video_clip = AudioFileClip(end)
    video_clip.write_audiofile(name_mp3)

    #Removing the original file
    os.remove(end)

    print(f"File downloaded and converted: {name_mp3}")

#Example
url = "https://www.youtube.com/watch?v=uMY71QLyQgI" #Cien años - Pedro Infante
downloadNconvert(url)
