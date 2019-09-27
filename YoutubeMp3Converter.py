from __future__ import unicode_literals
import youtube_dl

#'outtmpl': '%(playlist)s/%(uploader)s/%(playlist_index)s - %(title)s.%(ext)s',
def dlLink(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'download_archive': 'downloaded_songs.txt',
        'outtmpl': '%(playlist)s/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #ydl.download(['https://www.youtube.com/watch?v=0-c2CrQ4vJw&list=PLy_hoHKuZKvTrbgfOVVS_WCqW28W4dw3d&index=91'])
        ydl.download([link])



link = ""
while link != "exit":
    link = raw_input("insert link or type 'exit' to exit the programm")
    if link != "exit":
        dlLink(link)
