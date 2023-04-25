import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import playsound
import requests
import json
import os

class Audio:

    def googleSpeak(text):
        # Set the language code
        language = 'en'

        # Create a gTTS object and get the audio
        speech = gTTS(text)

        # Play the audio
        speech.save("./mp3/temp.mp3")
        playsound.playsound("temp.mp3", True)



    def recognize_speech(self):
        # Create a recognizer instance
        r = sr.Recognizer()

        # Define the audio source
        with sr.Microphone() as source:
            print("Speak something!")
            audio = r.listen(source)

        # Convert speech to text using Google API
        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I was unable to understand what you said.")
        except sr.RequestError as e:
            print("Error: {0}".format(e))



def baiduSpeak(text, api_key, secret_key):
    # Set the payload to send to the API endpoint
    payload = {
        "text": text,
        "cuid": "my_app",
        "tok": f"{api_key}:{secret_key}",
        "lan": "zh",
        "ctp": "1",
    }

    # Send a POST request to the Baidu API endpoint
    response = requests.post("http://tsn.baidu.com/text2audio", data=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the speech as an mp3 file
        with open("output.mp3", "wb") as f:
            f.write(response.content)

        # Play the mp3 file
        os.system("start output.mp3")

    else:
        print(f"Request failed with status code {response.status_code}")