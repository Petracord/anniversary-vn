from PIL import Image
from os.path import join, exists
import os
import shutil

orig_path = join("cgs", "original")
folders = os.listdir(orig_path)

processed_path = join("cgs", "processed")
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
        w_ratio = 1920 / w
        h_ratio = 1080 / h
        ratio = max(w_ratio, h_ratio)
        
        img = img.resize((int(w * ratio), int(h * ratio)), resample=Image.BICUBIC)
        img.save(join(target_dir, f"{file.split(".")[0]}.webp"), "WEBP", quality=100)