"""
Trim video 
"""

import cv2
import numpy as np
from moviepy.editor import *

clip = VideoFileClip('clips/Chill Minecraft Hypixel parkour gameplay for commentary! (free to use).mp4')

clip = clip.subclip(0, 12)

clip.write_videofile("clips/clip.mp4")