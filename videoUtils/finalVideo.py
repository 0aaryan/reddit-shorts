from moviepy.editor import *
import os
import random
from moviepy.video.VideoClip import TextClip
#import settings

from moviepy.config import change_settings

change_settings({"IMAGEMAGICK_BINARY": "/home/aryan/magick"})



def prepareTranscript(transcript,screenSize):
    text_clips=[]
    textSize=(screenSize[0]-50,screenSize[1])
    #it is only creating margin from right side
    #for left side margin we need to add margin in the text clip

    #add like share and subscribe in the end
    transcript.append({'start':transcript[-1]['end'],'end':transcript[-1]['end']+5,'text':'LIKE,SHARE AND SUBSCRIBE'})
    for line in transcript:
        start=line['start']
        end=line['end']
        text=line['text']
        duration=end-start
        #upper case text
        text=text.upper()

        # text_clip=TextClip(text,fontsize=40,color='white',font="Liberation-Sans-Narrow-Bold-Italic")
        # text_clip.set_position('left','center').set_duration(duration)
        # text_clips.append(text_clip)
        #add translucent black background
        
        #text_clip=TextClip(text,fontsize=30,color='white',font="Dyuthi",method="caption",size=textSize)

        #add margin to bot right and left direction of 30
        text_clip=TextClip(text,fontsize=30,color='white',font="Dyuthi",method="caption",size=screenSize)
        text_color = ColorClip(size=screenSize, color=(0,0,0), duration=duration).set_opacity(0.2)
        text_clip = CompositeVideoClip([text_color, text_clip])
        
        text_clip=text_clip.set_duration(duration).set_position(("center","center"))
        text_clips.append(text_clip)
    return concatenate_videoclips(text_clips).set_position(("center","center"))

def createVideo(transcript,audioFile,inputFolder,outputFile,logo=None):
    #select a random video from input folder
    video=VideoFileClip(os.path.join(inputFolder,random.choice(os.listdir(inputFolder))))
    #add audio and transcript to video
    video=video.subclip(0,transcript[-1]['end']+5)    
    audioFile=AudioFileClip(audioFile)
    video=video.set_audio(audioFile)
    screenSize=video.size
    #give margin in x direction from both sides such that text is not touching the edges


    # trim video till audio ends + 5 seconds for like and subscribe
    #transcript should be in the center of the video
    #white big text
    #crop till last word of transcript

    transcript=prepareTranscript(transcript,screenSize)


    #add logo at top center
    if logo:
        logo=ImageClip(logo).set_duration(video.duration).set_position(("center","top"))
        logo=logo.resize(width=video.w,height=video.h/10)
        video=CompositeVideoClip([video,logo,transcript])
    else:
        video=CompositeVideoClip([video,transcript])

    #save video
    #output file contains the name of the audio file and path
    video.write_videofile(outputFile)

    #for trial save only 10 seconds

 

# transcript=[{'start': 0.0, 'end': 5.5, 'text': " What's a NSFW detail about a historical figure that's normally left out of the history books?"}, {'start': 5.5, 'end': 13.0, 'text': ' A bit late to the party, but during WW1, prostitutes in Britain were more expensive if they had SDDs.'}, {'start': 13.0, 'end': 21.0, 'text': ' This was because if a soldier hired them and got infected, the soldier could be honorably discharged and not have to fight in war.'}, {'start': 21.0, 'end': 27.0, 'text': ' Ancient Egyptians believed the god Autumn created the universe by masturbating to ejaculation'}, {'start': 27.0, 'end': 31.5, 'text': ' and that the ebb and flow of the Nile corresponded to how much he came.'}, {'start': 31.5, 'end': 36.0, 'text': ' To honor this, the Pharaohs ceremonially masturbated into the river.'}]
# profilePic="profilePic.png"
# videoFolder="tempVid"
# output="myvid.mp4"
# audio="audio1.mp3"
# logo="logo.png"



# createVideo(transcript= transcript,audioFile = audio,inputFolder = videoFolder,outputFile= output,logo=logo)



