"""
Trim video 
"""

import cv2
import numpy as np
from moviepy.editor import *

clip = VideoFileClip('Chill Minecraft Hypixel parkour gameplay for commentary! (free to use).mp4')

clip = clip.subclip(0, 10)

clip.write_videofile("clip.mp4")