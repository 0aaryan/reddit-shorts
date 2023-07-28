from google.cloud import texttospeech as tts
import os

#credientials file name is google-credentials.json
#and storedd in post directory


def  textToSpeech(inputFileName=None, text=None,outputFileName="audio.mp3"):
    path = os.path.join(os.path.dirname(__file__), "google_credentials.json")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path
    input=""
    if inputFileName is not None:
        with open(inputFileName, 'r') as f:
            input = f.read()
    elif text is not None:
        input=text


    config = {
    "audioConfig": {
        "audioEncoding": "LINEAR16",
        "effectsProfileId": [
        "small-bluetooth-speaker-class-device"
        ],
        "pitch": 0,
        "speakingRate": 1
    },
    "input": {
        "text": "Google Cloud Text-to-Speech enables developers to synthesize natural-sounding speech with 100+ voices, available in multiple languages and variants. It applies DeepMind’s groundbreaking research in WaveNet and Google’s powerful neural networks to deliver the highest fidelity possible. As an easy-to-use API, you can create lifelike interactions with your users, across many applications and devices."
    },
    "voice": {
        "languageCode": "en-US",
        "name": "en-US-Neural2-J"
    }
    }

    text_input = tts.SynthesisInput(text=input)
    #set speed to 1.2
    voice_params = tts.VoiceSelectionParams(
        language_code="en-US", name="en-US-Neural2-J"
    )

    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16,speaking_rate=1.0,pitch=-5.0)

    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input,
        voice=voice_params,
        audio_config=audio_config,


    )
    with open(outputFileName, 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file ' + outputFileName)

if __name__ == "__main__":
    textToSpeech(inputFileName="input.txt",outputFileName="output.mp3")
