from fnmatch import translate
from time import sleep
from googletrans import Translator
import googletrans #pip install googletrans
from gtts import gTTS
import googletrans
import pyttsx3
import speech_recognition 
import os
from pygame import mixer
import time


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def translategl(query):
    speak("SURE SIR")
    print(googletrans.LANGUAGES)
    translator = Translator()
    speak("Choose the language in which you want to translate")
    b = input("To_Lang :- ")
    try:

        text_to_translate = translator.translate(query,src = "auto",dest= b,)
        text = text_to_translate.text
    
        speakgl = gTTS(text=text, lang=b, slow= False)
        speakgl.save("voice.mp3")
        mixer.init()

        mixer.music.load("voice")
        mixer.music.play()

        
        time.sleep(5)
        os.remove("voice.mp3")
    except:
        print("sorry boss , Unable to translate at this time tyr within 24 hour, something wrong in system ")
        speak("sorry boss , Unable to translate at this time tyr within 24 hour, something wrong in system ")
#query = takeCommand().lower()
#translategl(query)

