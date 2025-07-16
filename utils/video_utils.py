import cv2
import os
import subprocess

def extract_frames(video_path, output_dir='static/frames', interval=30):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    count, frame_num = 0, 0
    while True:
        success, frame = cap.read()
        if not success:
            break
        if count % interval == 0:
            cv2.imwrite(f"{output_dir}/frame{frame_num}.jpg", frame)
            frame_num += 1
        count += 1
    cap.release()

def extract_audio(video_path, audio_path='uploads/audio.wav'):
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)
    command = f"ffmpeg -i {video_path} -q:a 0 -map a {audio_path} -y"
    subprocess.call(command, shell=True)
    return audio_path
