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


def download(link: str, root_folder: str, filename: str, audio: bool = True) -> None:
    """download videos from youtube
    TODO:
    * change file format to whatever we want
    * split audio and video by not calling download twice.
    * why is download being called twice??

    """
    ydl_opts = {
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'outtmpl': f'{root_folder}/{filename}',
    }
    if audio:
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    
if __name__ == "__main__":
    link = "https://www.youtube.com/watch?v=2gPUdfL4IWs&t=1s"
    folder = "output"
    filename = "rgss"
    download(link, folder, filename)