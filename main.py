from scrapeUtils.reddit import get_post_and_replies
from textUtils.tts import textToSpeech
from textUtils.transcribe import audio_to_transcript
from videoUtils.finalVideo import createVideo
import argparse
import re
import os
from dictPosts import dict_list




# url="https://www.reddit.com/r/AskReddit/comments/n94deo/people_who_got_caught_having_sex_at_work_what/"


# def compileVideo(url,outputFolder,numOfVids=1,wordLimit=100,commentLimit=25,vidFolder=None):
    
#     texts,error = get_post_and_replies(post_url =url,num_vids=numOfVids,word_limit=wordLimit,commentLimit=commentLimit)
    
#     if error:
#         print(texts)
#         return
    
#     #create output folder
#     if not os.path.exists(outputFolder):
#         os.makedirs(outputFolder)
#         os.makedirs(os.path.join(outputFolder,"audio"))
    
#     foldercount=0
#     #count number of folders in audio
#     for folder in os.listdir(os.path.join(outputFolder,"audio")):
#         foldercount+=1


#     os.makedirs(os.path.join(outputFolder,f"audio/post{foldercount+1}"))
    
#     #enumerate through texts
#     print(f"created output/audio/post{foldercount+1}")
#     transcripts=[]
#     for i,text in enumerate(texts):
#         #text to speech
#         print(f"creating audio{i+1}")
#         #textToSpeech(text=text,outputFileName=os.path.join(outputFolder,f"audio/post{foldercount+1}/audio{i+1}.mp3"))
#         #audio to text
#         print(f"creating transcript{i+1}")
#         transcript=audio_to_transcript(os.path.join(outputFolder,f"audio/post{foldercount+1}/audio{i+1}.mp3"))
#         transcripts.append(transcript)
#     print(transcripts)


#     #create video

#     for i,transcript in enumerate(transcripts):
#         print(f"creating video{i+1}")
#         #if video is less than 20 seconds skip
#         if len(transcript[-1]["end"])<20:
#             continue
            
#         #create video
#         createVideo(
#             transcript=transcript,
#             outputFileName=os.path.join(outputFolder,f"video/post{foldercount+1}/video{i+1}.mp4"),
#             audioFile=os.path.join(outputFolder,f"audio/post{foldercount+1}/audio{i+1}.mp3"),

#         )

# #compileVideo(url,"output",numOfVids=3,wordLimit=100,commentLimit=5,vidFolder="../media/gameplayVids/minecraft_oneMin")

# audioFile="/output/audio/post1/audio1.mp3",
# inputFolder="../media/gameplayVids/minecraft_oneMin",
# outputFile="/output/video/post1/video1.mp4"
# transcript=[{'start': 0.0, 'end': 3.8000000000000003, 'text': ' People who got caught having sex at work what happened.'}, {'start': 3.8000000000000003, 'end': 6.84, 'text': ' They were a married couple but both employees.'}, {'start': 6.84, 'end': 9.92, 'text': ' They got caught screwing at the Christmas party.'}, {'start': 9.92, 'end': 13.72, 'text': ' Nothing happened for a few weeks, then they both got fired because they were collecting'}, {'start': 13.72, 'end': 17.96, 'text': " the gym membership stipend but couldn't show proof of attendance."}, {'start': 17.96, 'end': 21.68, 'text': ' Pretty sure that was the first and only time the company enforced the stipend rule.'}]

# # audioFile = os.path.join(os.path.dirname(__file__), audioFile)
# # inputFolder = os.path.join(os.path.dirname(__file__), inputFolder)
# # outputFile = os.path.join(os.path.dirname(__file__), outputFile)

# createVideo(
#     transcript=transcript,
#     audioFile=audioFile,
#     inputFolder=inputFolder,
#     outputFile=outputFile
    
# )







def redditLinkToVideo(url,
                      numOfVids=1,
                      wordLimit=100,
                      inputVidFolder="media/gameplayVids/minecraft_oneMin",
                      outputVidFolder="output",
                      logo="media/profile/logo.png",):
    


    #get post and replies
    texts,error = get_post_and_replies(post_url =url,num_vids=numOfVids,word_limit=wordLimit,commentLimit=numOfVids*5)
    if error:
        print(texts)
        return

    print(str(len(texts))+" posts found")

    postDir=""

    #create output folder
    if not os.path.exists(outputVidFolder):
        os.makedirs(outputVidFolder)
        os.makedirs(os.path.join(outputVidFolder,"post1"))
        postDir=os.path.join(outputVidFolder,"post1")
        print(f"created output/post1")
    else:
        #count number of folders in audio
        foldercount=0
        for folder in os.listdir(outputVidFolder):
            foldercount+=1
        os.makedirs(os.path.join(outputVidFolder,f"post{foldercount+1}"))
        postDir=os.path.join(outputVidFolder,f"post{foldercount+1}")
        print(f"created output/post{foldercount+1}")

    #enumerate through texts
    transcripts=[]
    audioFiles=[]
    for i,text in enumerate(texts):
        #text to speech
        print(f"creating audio{i+1}")


        #text to speech api limit = 5000 bytes
        #5000 bytes = 5000/8 = 625 characters
        #sif greater than 600 char just send first 600
        if len(text)>600:
            text=text[:600]
        try:
            textToSpeech(text=text,outputFileName=os.path.join(postDir,f"audio{i+1}.mp3"))
        except:
            print("error creating audio")
            print("skipping")
            continue
        audioFiles.append(os.path.join(postDir,f"audio{i+1}.mp3"))

        #audio to text
        print(f"creating transcript{i+1}")
        transcript=audio_to_transcript(os.path.join(postDir,f"audio{i+1}.mp3"))

        #add transcript to list
        transcripts.append(transcript)

        #create video

        print(f"creating video{i+1}")
        #if video is less than 20 seconds skip
        if transcript[-1]["end"]<20:
            continue

        #create video
        createVideo(
            transcript=transcript,
            outputFile=os.path.join(postDir,f"video{i+1}.mp4"),
            audioFile=os.path.join(postDir,f"audio{i+1}.mp3"),
            inputFolder=inputVidFolder,
            logo=logo

        )


    print(f"created {len(transcripts)} videos")




def dictsToVideos(dictList, outputVidFolder="output", inputVidFolder="media/gameplayVids/minecraft_oneMin", logo="media/profile/logo.png"):

    postDir=""

    #create output folder
    if not os.path.exists(outputVidFolder):
        os.makedirs(outputVidFolder)
        os.makedirs(os.path.join(outputVidFolder,"post1"))
        postDir=os.path.join(outputVidFolder,"post1")
        print(f"created output/post1")
    else:
        #count number of folders in audio
        foldercount=0
        for folder in os.listdir(outputVidFolder):
            foldercount+=1
        os.makedirs(os.path.join(outputVidFolder,f"post{foldercount+1}"))
        postDir=os.path.join(outputVidFolder,f"post{foldercount+1}")
        print(f"created output/post{foldercount+1}")

    #enumerate through texts
    transcripts=[]
    audioFiles=[]
    for i,dictionary in enumerate(dictList):
        text = ""
        for j,key in enumerate(dictionary.keys()):
            #leave first key out as it is question
            if j==0:
                text+=dictionary[key]
            else:
                text+=f" {j}. {dictionary[key]}"
    
        #text to speech


        print(f"creating audio{i+1}")


        #text to speech api limit = 5000 bytes
        #5000 bytes = 5000/8 = 625 characters
        #sif greater than 600 char just send first 600
        if len(text)>600:
            text=text[:600]
        try:
            textToSpeech(text=text,outputFileName=os.path.join(postDir,f"audio{i+1}.mp3"))
        except:
            print("error creating audio")
            print("skipping")
            continue
        audioFiles.append(os.path.join(postDir,f"audio{i+1}.mp3"))

        #audio to text
        print(f"creating transcript{i+1}")
        transcript=audio_to_transcript(os.path.join(postDir,f"audio{i+1}.mp3"))

        #add transcript to list
        transcripts.append(transcript)

        #create video

        print(f"creating video{i+1}")
        #if video is less than 20 seconds skip
        if transcript[-1]["end"]<20:
            continue

        #create video
        createVideo(
            transcript=transcript,
            outputFile=os.path.join(postDir,f"video{i+1}.mp4"),
            audioFile=os.path.join(postDir,f"audio{i+1}.mp3"),
            inputFolder=inputVidFolder,
            logo=logo

        )

    print(f"created {len(transcripts)} videos")


if __name__ == "__main__":
    #creating cli
    # -ru redditLinkToVideo
    # -n number of videos
    # -w word limit
    # -i input video folder
    # -o output video folder

    parser = argparse.ArgumentParser(description='Reddit to video')
    parser.add_argument('-ru', '--redditUrl', type=str, help='reddit url')
    parser.add_argument('-n', '--numOfVids', type=int, help='number of videos')
    parser.add_argument('-w', '--wordLimit', type=int, help='word limit')
    parser.add_argument('-i', '--inputVidFolder', type=str, help='input video folder')
    parser.add_argument('-o', '--outputVidFolder', type=str, help='output video folder')
    
    #multiple urls urlfile -rus urls.txt
    parser.add_argument('-rus', '--redditUrlFile', type=str, help='reddit url file')    
    parser.add_argument('-d', '--dictList', type=str, help='dict list')
    
    args = parser.parse_args()
    #dict_list to video
    #check if args are valid

    if args.numOfVids is None:
        args.numOfVids=1
    if args.wordLimit is None:
        args.wordLimit=100
    if args.inputVidFolder is None:
        args.inputVidFolder="media/gameplayVids/minecraft_oneMin"
    if args.outputVidFolder is None:
        args.outputVidFolder="output"

    if args.redditUrl is not None:
        redditLinkToVideo(url=args.redditUrl,
                          numOfVids=args.numOfVids,
                          wordLimit=args.wordLimit,
                          inputVidFolder=args.inputVidFolder,
                          outputVidFolder=args.outputVidFolder)
    
    if args.redditUrlFile is not None:
        with open(args.redditUrlFile) as f:
            urls = f.readlines()
        urls = [x.strip() for x in urls] 
        for i,url in enumerate(urls):
            print(f"creating video {i+1} of {len(urls)}")
            redditLinkToVideo(url=url,
                          numOfVids=args.numOfVids,
                          wordLimit=args.wordLimit,
                          inputVidFolder=args.inputVidFolder,
                          outputVidFolder=args.outputVidFolder)
            
            
    if args.dictList is not None:
        #if -d is given but no file is given
        if args.dictList=="default":
            dictsToVideos(dictList=dict_list,outputVidFolder=args.outputVidFolder,inputVidFolder=args.inputVidFolder,logo="media/profile/logo.png")
        else:
            #print use default dict_list
            print("use dictPosts to use this feature")
    
#to convert post.py that contains dict_list to video
#python main.py -d post.py -o output -i media/gameplayVids/minecraft_oneMin




        
    




