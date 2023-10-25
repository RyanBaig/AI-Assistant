import os
import speech_recognition as sr
from gtts import gTTS
from functions import *

def process_speech():
    """
    Process speech input by:
    - Creating a speech recognizer
    - Recording audio from a microphone
    - Recognizing speech using Google's speech recognition
    - Sending the detected speech to the Falcon-7B-Instruct model for generating a response
    - Printing the generated text
    - Converting the generated text to speech and saving it as an audio file
    - Playing the generated audio
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        detected_speech: str =  recognizer.recognize_google(audio)
        print("Detected speech:", detected_speech)


        response = query({"inputs": detected_speech})

        parsed_response: str = response["generated_text"]
        better_response = parsed_response.replace(detected_speech, "")
        
        print("Generated text:", better_response)

        tts = gTTS(text=better_response, lang='en', tld="co.in")
        tts.save("audio.mp3")

        os.system("start audio.mp3")

    except sr.UnknownValueError:
        print("No speech detected")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    try:
        process_speech()
    except KeyboardInterrupt:
        pass