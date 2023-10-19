import os
from moviepy.editor import *


def gif_to_mov(gif_path, output_path):
    clip = VideoFileClip(gif_path).loop(duration=10)

    width, height = clip.size
    if width % 2 != 0:
        width -= 1
    if height % 2 != 0:
        height -= 1
    clip = clip.resize((width, height))

    clip.write_videofile(output_path, fps=24, codec="libx264")


dir_path = "/Users/hudzah/Downloads/photos2"

for filename in os.listdir(dir_path):
    if filename.endswith(".gif"):
        gif_path = os.path.join(dir_path, filename)
        output_path = os.path.join(dir_path, filename[:-4] + ".mov")
        gif_to_mov(gif_path, output_path)
