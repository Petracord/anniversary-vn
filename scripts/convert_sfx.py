import ffmpeg
from os.path import join, exists
import os
import shutil

orig_path = join("audio", "original")
folders = os.listdir(orig_path)

processed_path = join("audio", "processed")
shutil.rmtree(processed_path)
os.makedirs(processed_path)

def process_wav(audio_in, audio_out):
    ffmpeg.input(audio_in) \
        .output(audio_out, acodec="libmp3lame", format="mp3", **{"q:a": 2}) \
        .run()

for folder in folders:
    target_dir = join(processed_path, folder)
    os.makedirs(target_dir)
    files = os.listdir(join(orig_path, folder))
    
    for file in files:
        ext = file.split(".")[-1]
        process_wav(join(orig_path, folder, file), join(processed_path, folder, file).replace(".wav", ".ogg").replace(".mp3",".ogg"))