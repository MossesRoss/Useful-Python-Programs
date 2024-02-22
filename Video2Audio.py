import moviepy.editor as mpy
import os

def video_to_audio(video_path, output_path):
    clip = mpy.VideoFileClip(video_path)

    audio = clip.audio

    audio.write_audiofile(output_path)
    
    print("Video converted to audio successfully!")

video_path = "input_video.mp4"
output_path = "output_audio.mp3"

video_to_audio(video_path, output_path)
