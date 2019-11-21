from __future__ import unicode_literals
import youtube_dl

#'outtmpl': '%(playlist)s/%(uploader)s/%(playlist_index)s - %(title)s.%(ext)s',
def dlMusic(links):
    ydl_opts = {
        'format': 'bestaudio/best',
        'download_archive': 'downloaded_songs.txt',
        'outtmpl': 'music/%(playlist)s/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    for x in links:
        print(x)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            #ydl.download(['https://www.youtube.com/watch?v=0-c2CrQ4vJw&list=PLy_hoHKuZKvTrbgfOVVS_WCqW28W4dw3d&index=91'])
            ydl.download([x])

def dlVideos(links):
    ydl_opts = {
        'outtmpl' : 'videos/%(playlist)s/%(title)s.%(ext)s'
    }
    for x in links:
        print(x)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            #ydl.download(['https://www.youtube.com/watch?v=0-c2CrQ4vJw&list=PLy_hoHKuZKvTrbgfOVVS_WCqW28W4dw3d&index=91'])
            ydl.download([x])

def help():
    print("First: insert all links that you want to Download. You can insert playlist links to download a playlist.")
    print("Secound: Type 'music','mp3', 'go' or 'start' to Download as mp3 audio file. If you want to download Videos then type 'video' or 'mp4' ")
    print("Type 'help' or 'h' for this help")

help()
links = []
link = ""
while link != "exit":
    link = input("insert link or type 'exit' to exit the programm")
    if link == "start" or link == "go" or link == "mp3" or link == "music":
        dlMusic(links)
    if link == "video" or link == "mp4":
        dlVideos(links)
    if link == "help":
        help()
    else:
        links.append(link)
    #if link != "exit":
    #    dlLink(link)
