import cv2
 
def split_frames(video_path: str, output_folder: str, fps: int):
    """Split video into frames @ 1 fps.

    TODO:
    * create output folders when it doesn't exist already

    Args:
        video_path (str): _description_
        output_folder (str): _description_
        fps (int): _description_
    """
    print(f"Splitting {video_path} and saving to {output_folder}")
    capture = cv2.VideoCapture(video_path)
    
    frame_num = 0 

    # Check if camera opened successfully
    if (capture.isOpened() == False): 
        print("Error opening video stream or file")
    
    # Save 1 frame per second of video
    while(capture.isOpened()):
        success, frame = capture.read()

        if frame_num % fps == 0:
            if success: 
                cv2.imwrite(f'{output_folder}/frame_{frame_num // fps}.jpg', frame)
                frame_path = f'{output_folder}/frame_{frame_num // fps}.jpg'
                print(frame_path)
            else:
                break
    
        frame_num += 1

    capture.release()

if __name__ == "__main__":
    video_path = ""
    output_path = ""
    split_frames()
