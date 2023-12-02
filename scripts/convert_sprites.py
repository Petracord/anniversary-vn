from PIL import Image
from os.path import join, exists
import os
import shutil

orig_path = join("sprites", "original")
folders = os.listdir(orig_path)

processed_path = join("sprites", "processed")
shutil.rmtree(processed_path)
os.makedirs(processed_path)

for f in folders:
    target_dir = join(processed_path, f)
    os.makedirs(target_dir)
    
    files = os.listdir(join(orig_path, f))
    
    for file in files:
        img = Image.open(join(orig_path, f, file))
        img = img.crop(img.getbbox())
        w, h = img.size
        ratio = 2000 / h
        img = img.resize((int(w * ratio), int(h * ratio)), resample=Image.BICUBIC)
        
        emotion = file.split("_")[-1].split(".")[0]
        img.save(join(target_dir, f"{emotion}.webp"), "WEBP", quality=100)