from pytube import YouTube
import time
import os

url = input('Enter the url: ')
yt = YouTube(url)

mpsel = int(input('1: MP4\n2: MP3\n'))

if mpsel == 1:
    print()
    ys = yt.streams.get_highest_resolution()
    ys.download()
    print('Video in MP4 format downloaded!\n')
    time.sleep(10)
    exit()

if mpsel == 2:
    print()
    ys = yt.streams.get_audio_only('mp4')
    ys.download()
    print('Video in MP3 format downloaded! Closing in 3 seconds.\n')
    thisFile = f"{yt.title}.mp4"
    base = os.path.splitext(thisFile)[0]
    os.rename(thisFile, base + ".mp3")
    time.sleep(3)
    exit()
