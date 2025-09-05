import pyttsx3
import speech_recognition 
import subprocess
import pywhatkit
import datetime
import qrcode
from tkinter import *
import pyaudio 
from pygame import mixer
import speedtest
import requests
from bs4 import BeautifulSoup
import os
import random
import webbrowser
import keyboard 
import pyautogui
from plyer import notification

for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [  activate ] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("wrong password,Try Again")

from INTRO import play_gif
#play_gif

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
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

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "activate"  in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "hello" in query:                                #simple conversion
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query or "i m fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query or "how r u" in query:
                    speak("Perfect, sir")
                elif "thank you" in query or "thank" in query:
                    speak("you are welcome, sir")
                elif "bye" in query:
                    speak("bye , sir have nice day")
                elif "what you can do jarvis" in query or "work properly" in query:
                    speak("sorry boss something wrong")

                elif "open google search" in query:                         ##open google
                    speak("ok boss, waittt")
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "open google" in query:
                    webbrowser.open("google.com")
                
                elif "open facebook" in query:        
                    speak("just wait bosss")                      #open insta,faceook
                    webbrowser.open("facebook.com")
                elif "open instagram" in query :
                    speak("just wait bosss")
                    webbrowser.open("instagram.com")
                    
                elif "open wikipedia search" in query:                      #open wikipedia
                    speak("searching start wait sir")
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                elif "open wikipedia" in query :
                    speak("just wait bosss")
                    webbrowser.open("wikipedia.org")
  
                                                                     #alarm
                elif "set the alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                                                                      #news
                elif "news" in query:                         
                    speak("just wait sir")
                    from NewsRead import latestnews
                    latestnews()

                elif "close" in query:                                #close tab or .com
                    from Dictapp import closeappweb
                    closeappweb(query)
        
                elif "open youtube search" in query:                        #open youtube
                    speak("searching start wait sir")
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "open youtube" in query:
                    webbrowser.open("youtube.com")
                                                                      #time and date
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")                
                elif "date" in query:
                    day= int(datetime.datetime.now().day)
                    month= int(datetime.datetime.now().month)
                    year= int(datetime.datetime.now().year)
                    speak("boss today's date is ")
                    speak(day)
                    speak(month)
                    speak(year)
                                                                     #click pic using camera
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
                                                                      #screenshot
                elif "screenshot" in query:
                    import pyautogui #pip install pyautogui
                    im = pyautogui.screenshot()
                    list=[m for m in range(100)]
                    r=random.choice(list)
                    im.save(f"ss{r}.jpg")                     
                    speak("done boss")     
                                                                        #CALCULATE                
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                                                                        #PLAY rock paper 
                elif "rock paper" in query:
                    from game import game_play
                    game_play()
                elif "tic" in query or "tic toy" in query or "tiktoy" in query:
                    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    turn = 1 # 1 for X and 0 for O
                    print("Welcome to Tic Tac Toe")
                    while(True):
                        from game2 import printBoard
                        printBoard(xState, zState)
                        if(turn == 1):
                            print("X's Chance")
                            value = int(input("Please enter a value: "))
                            xState[value] = 1
                        else:
                            print("O's Chance")
                            value = int(input("Please enter a value: "))
                            zState[value] = 1
                        from game2 import checkWin
                        cwin =checkWin(xState, zState)
                        if(cwin != -1):
                            print("Match over")
                            break
        
                        turn = 1 - turn
                elif "deactivate" in query:                             #DEACTIVE JARVIS
                    speak("jarvis deactivated sir")
                    exit()
                                                                         # SET SCHEDULE
                elif "schedule my day" in query or "set my schedule" in query:     
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                                                                      #SHOW SHEDULE
                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("C:\Windows\Media\Alarm01.wav")
                    mixer.music.play()
                    notification.notify(
                    title = "My schedule :-",
                    message = content,
                    timeout = 15  ) 
                                                            
                                                        #STOP, PLAY ,MUTE, VOLUME UP,DOWN SETTING OF YOUTUBE
                elif "stop video" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play video" in query or "start video" in query :
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "volume up" in query or "volume decrease" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query or "volume decrease" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
                                                                         #REMEMBER
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak(""+rememberMessage)
                    
                    remember = open("Remember.txt","w")
                    remember.write(rememberMessage)
                    remember.close()
                                                                           #REMEMBER SHOW
                elif "what do you remember" in query or "missing" in query:
                    remember = open("Remember.txt","r")
                    rr=remember.read()
                    speak(rr)
                    notification.notify(
                        title = "remember",
                        message = rr,
                        timeout = 15
                    )  
                                                                            #PLAY FAV SONG
                elif "tired" in query or "play song" in query or "play my favourite songk" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                    b = random.choice(a)
                    if b==1:
                       webbrowser.open("https://www.youtube.com/watch?v=ZdFIOTWP4Og")
                    if b==3:
                       webbrowser.open("https://www.youtube.com/watch?v=IpfFjlIFA4Y")
                    if b==2:
                       webbrowser.open("https://www.youtube.com/watch?v=sJc8s0DKTHE&list=RDsJc8s0DKTHE&start_radio=1&rv=3lws1R5ouPwk")

                elif "whatsapp" in query:                             #WHATSAPP MSG
                    speak("one minute boss")
                    from Whatsapp import sendMessage
                    sendMessage()
                                                                       #SHUTDOWN SYSTEM
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown , yenter es or no boss")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                       speak("shut down processing")
                       os.system("shutdown /s /t 1")
 
                    elif shutdown == "no":
                       speak("ok sir")
                       break
                                                                         #CHANGE JARVIS PASSWORD
                elif "change password" in query or "change my password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")
                elif "open" in query:                              #EASY open software
                    speak("openning sir ")
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter") 
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net= wifi.upload()/1048576  #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}") 

                elif "ipl score" in query:                                 # ipl score
                    from plyer import notification  #pip install plyer
                    import requests #pip install requests
                    from bs4 import BeautifulSoup #pip install bs4
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[2].get_text()
                    
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )
                                                                              #block website     
                elif "focus mode" in query or "block website" in query:
                    speak("Are you sure that you want to enter block website :- [1 for YES / 2 for NO ")
                    a = int(input("Are you sure that you want to enter block website :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("FocusMode.py")
                        exit()
                    else:
                        pass
                                                                        # block website graph
                elif "show my focus" in query or 'show blocked site graph' in query:
                    from FocusGraph import focus_graph
                    focus_graph()
                
                elif "translate" in query:                      #translate sentense in other language
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)

                elif "generate qr code" in query or "qr code" in query:
                    speak("ok boss, please enter following ")
                    print("ok boss, please enter link or msg which are stored in qrcode")
                    data=input("enter msg or link")
                    img=qrcode.make(data)
                    speak("enter file name")
                    file=input("enter qrcode file save as - ")
                    img.save(file+".png")
       
                    
                    