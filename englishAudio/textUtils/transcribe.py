import whisper
model = whisper.load_model("base")


# result = model.transcribe("output.mp3")
# for res in result["segments"]:
#     print(res["start"], res["end"], res["text"])


def audio_to_transcript(audio_file):
    result = model.transcribe(audio_file)
    transcript = []
    for res in result["segments"]:
        transcript.append({
            "start": res["start"],
            "end": res["end"],
            "text": res["text"]
        })
    return transcript
