from download import download 

if __name__ == "__main__":
    link = "https://www.youtube.com/watch?v=2gPUdfL4IWs&t=1s"
    folder = "output"
    filename = "rgss"
    download(link, folder, filename)
    download(link, folder, filename, audio=False)