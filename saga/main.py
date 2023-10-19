from video import split_frames
from download import download 

if __name__ == "__main__":
    print("start")
    link = "https://www.youtube.com/watch?v=2gPUdfL4IWs&t=1s"
    folder = "output"
    filename = "rgss"
    download(link, folder, filename)
    print("download")
    fps = download(link, folder, filename, audio=False)

    print("split")
    video_path = f"{folder}/{filename}.mp4"
    output_folder = f"{folder}/{filename}/frames"
    split_frames(video_path, output_folder, fps)