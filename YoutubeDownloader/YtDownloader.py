from pytubefix import YouTube, Playlist
import os
from pathlib import Path

downloadPath = str(os.path.join(Path.home(), 'Downloads'))
link = input('Enter the link of the video or playlist: ')

if 'list=' in link:
    playlist = Playlist(link)
    res = input("Enter the resolution: ")
    res1 = res + "p"
    for video in playlist.videos:
        video.streams.filter(res = res1).first().download(downloadPath) 
    print("Videos Downloaded!")

else:
    video = YouTube(link)

    print('Title:', video.title)
    print('Author:', video.author)
    print(f'Length {video.length/60:.2f} min')

    res = input("Enter the resolution: ")
    res1 = res + "p"
    video.streams.filter(res = res1).first().download(downloadPath) 

    print("Video Downloaded!")