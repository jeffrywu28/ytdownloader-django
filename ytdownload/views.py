from django.shortcuts import render
from pytube import YouTube
import os
url=''

def yt_download(request):
    return render(request, 'yt_main.html')

def download(request):
    global url
    url = request.GET.get('url')
    try:
        video = YouTube(url)
        resolusi_gambar = []
        stream_all = video.streams.filter(progressive=True,file_extension='mp4').all()
        for i in stream_all:
            resolusi_gambar.append(i.resolution)
        resolusi_gambar = list(dict.fromkeys(resolusi_gambar))
        embed_link = url.replace("watch?v=","embed/")
        return render(request,'yt_download.html',{'resolusi':resolusi_gambar,'embd':embed_link})
    except:
        return render(request,'sorry.html')

def download_complete(request, res):
    global url
    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    print(f'DIRECT :', f'{dirs}/Downloads')
    if request.method == "POST":
        YouTube(url).streams.get_by_resolution(res).download(homedir + '/Downloads')
        return render(request, 'download_complete.html')
    else:
        return render(request, 'sorry.html')