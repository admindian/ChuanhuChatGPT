import speech_recognition as sr

Create a recognizer instance
r = sr.Recognizer()

Define the audio source
with sr.Microphone() as source: print("Speak something!") audio = r.listen(source)

Convert speech to text using Google API
try: text = r.recognize_google(audio) print("You said: " + text) except sr.UnknownValueError: print("Sorry, I was unable to understand what you said.") except sr.RequestError as e: print("Error: {0}".format(e))