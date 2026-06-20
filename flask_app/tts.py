from gtts import gTTS
import os

def text_to_audio(text):

    os.makedirs("outputs", exist_ok=True)

    output_file = "outputs/output.mp3"

    tts = gTTS(text=text, lang='en')
    tts.save(output_file)

    return output_file