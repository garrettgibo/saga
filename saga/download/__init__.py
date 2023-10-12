from __future__ import unicode_literals
import youtube_dl

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


def download(link, root_folder, filename) -> None:
    """download videos from youtube
    TODO:
    * change file format to whatever we want
    * split audio and video
    * why is download being called twice??

    """
    ydl_opts = {
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'outtmpl': f'{root_folder}/{filename}'
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        # TODO: find out how to save to specific location with a certain filename
        ydl.download([link])
    
if __name__ == "__main__":
    link = "https://www.youtube.com/watch?v=2gPUdfL4IWs&t=1s"
    folder = "output"
    filename = "rgss"
    download(link, folder, filename)