import cv2
import os

def extract_frames(video_path, output_folder="frames", interval=30):
    os.makedirs(output_folder, exist_ok=True)

    vidcap = cv2.VideoCapture(video_path)
    count = 0
    frame_paths = []

    while True:
        success, image = vidcap.read()
        if not success:
            break
        if count % interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{count}.jpg")
            cv2.imwrite(frame_filename, image)
            frame_paths.append(frame_filename)
        count += 1

    vidcap.release()
    return frame_paths
