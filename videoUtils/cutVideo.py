#import moviepy

#i want to cut one 1 hour video in 60 1 minute videos
#and save them in a folder named minecraft_{i}.mp4
#and save it in this "/media/gameplayVids/minecraft" folder

import moviepy.editor as mp
import os

clip = mp.VideoFileClip("../media/gameplayVids/minecraft.mp4")

sx=(clip.w/2)-202

#crop such that its 9:16 and center should be same
for i in range(80):

    one_minute = clip.subclip(i*60, (i+1)*60)
    #crop such that its 9:16 and center should be same
    one_minute = one_minute.crop(x1=sx, y1=0, x2=sx+404, y2=720)
    one_minute.write_videofile(f"../media/gameplayVids/minecraft_oneMin/minecraft_{i}.mp4")


