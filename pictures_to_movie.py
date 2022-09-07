# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 15:06:23 2022

@author: Matic
"""

import os
import moviepy.editor as mp

# new_path = 'C:\\Users\\Matic\\Documents\\1_služba\\termalna kamera\\rpi0_pwr\\'

os.chdir('C:\\Users\\Matic\\Documents\\1_služba\\termalna kamera\\rpi0_pwr')

files = os.listdir()
print(files)
# for i in range(len(files)):
#     os.rename(path+files[i], str(i))
# print(files)

clip = mp.ImageSequenceClip(files, fps = 100) 

# print(clip)
# print(type(clip))

# clip.ipython_display(width = 280)

clip.write_videofile('video.mp4', fps=100)