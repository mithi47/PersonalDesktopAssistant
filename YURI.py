from __future__ import with_statement
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from vosk import Model, KaldiRecognizer
import playsound
from playsound import playsound
import random
import cv2
import pyaudio
import sys
import pyautogui
import time
import operator
import requests
import pyjokes
import openai
import subprocess
from time import sleep
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget
from time import sleep
import imaplib
import email
import datetime
import psutil
from email.header import decode_header
import urllib.request
import numpy as np
import wmi
wmi_obj = wmi.WMI(namespace='wmi')



import requests

def check_internet_connection():
    try:
        requests.get("http://www.google.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False
if check_internet_connection():
    print("Internet connection is available")
    import pywhatkit
else:
    print("No internet connection available")
    
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!") 
    else:
        speak("Good Evening!")
 
    speak("Ready To assist . What can I do for you ?")

def takeCommand1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e: 
        print("Say that again please...") 
        return "None"
    return query

def notakecommand1():
    model = Model(r"C:\YURI\vosk-model-en-in-0.5")
    recognizer = KaldiRecognizer(model, 16000)

    mic = pyaudio.PyAudio()
 
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()
  

    while True:
        data = stream.read(4096)
        if recognizer.AcceptWaveform(data):
            rec = recognizer.Result()
            break
            
    
    print(rec)
    return rec
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        p2=subprocess.Popen(['python','C:\YURI\LISTEN.py'])
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        p2.terminate()
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e: 
        print("Say that again please...") 
        return "None"
    return query

def notakecommand():
    model = Model(r"C:\YURI\vosk-model-en-in-0.5")
    recognizer = KaldiRecognizer(model, 16000)

    mic = pyaudio.PyAudio()
 
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()
    p2=subprocess.Popen(['python','C:\YURI\LISTEN.py'])
    
    while True:
        data = stream.read(4096)
        if recognizer.AcceptWaveform(data):
            rec = recognizer.Result()
            break 
    p2.terminate()   
    print(rec)
    return rec





def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=889a39d0a34c457f9955f88c57ae243b'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day=["first","second","third"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

def generate_program(prompt):
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        n=1,
        stop=None,
    )
    
    program = response.choices[0].text.strip()

    return program



def whatsapp():
    from datetime import datetime
    from datetime import timedelta
    future_time = datetime.now() + timedelta(minutes=3)
    fu=future_time.strftime("%H:%M")
    return(fu)    

def queryy():
    
    if check_internet_connection() == True:
        take = takeCommand()
    elif check_internet_connection() == False:
        take = notakecommand()
    return take
def queryy1():
    
    if check_internet_connection() == True:
        take = takeCommand1()
    elif check_internet_connection() == False:
        take = notakecommand1()
    return take

def wake():
    while True:

        wake=queryy1().lower()
        if "yuri" in wake:
            break
        elif "yuki" in wake:
            break
        elif "uri" in wake:
            break

    playsound(r'C:\Yuri\mixkit-quick-win-video-game-notification-269.wav')

def main():
    wake()
    p1=subprocess.Popen(['python',"C:\YURI\ICON.py"])
    wishMe()
    
    while True:
        try:

            query = queryy().lower()
            
            if "hello" in query:
                    speak("Hello sir, how are you ?")

            elif "hello Uri are you awake" in query:
                    speak("yes sir!")

            elif "hello Yuri are you awake" in query:
                    speak("yes sir!")                
            
            elif "battery" in query:
                battery = psutil.sensors_battery()

                plugged = battery.power_plugged
                percent = battery.percent

                if plugged:
                    status = "charging"
                else:
                    status = "not charging"

                speak(f"Battery status: {percent}% ({status})")


            elif 'search on youtube' in query:
                query = query.replace("search on youtube", "")
                webbrowser.open(f"www.youtube.com/results?search_query={query}")    

            elif "tell me a joke" in query:
                joke = pyjokes.get_joke()
                speak(joke)    

            elif 'open youtube' in query:
                #if connect() == True:
                import pywhatkit
                speak("what you will like to watch ?")
                qrry = takeCommand().lower()
                pywhatkit.playonyt(f"{qrry}")

            elif "close youtube" in query:
                os.system("taskkill /im chrome.exe /f")
        

            elif "song on youtube" in query:
                #if connect() == True:
                import pywhatkit
                pywhatkit.playonyt("see you again")  

               

            elif 'close chrome' in query:
                os.system("taskkill /f /im chrome.exe")

            elif 'close youtube' in query:
                os.system("taskkill /f /im chrome.exe")
            
            elif 'open google' in query:
                speak("what should I search ?")
                qry = takeCommand().lower()
                webbrowser.open(f"{qry}")
                results = wikipedia.summary(qry, sentences=1)
                speak(results)

            elif 'google search' in query:
                speak("what should I search ?")
                qry = takeCommand().lower()
                webbrowser.open(f"{qry}")
                results = wikipedia.summary(qry, sentences=1)
                speak(results)

            elif 'close google' in query:
                os.system("taskkill /f /im msedge.exe")
            
            elif "play music" in query:
                music_dir = "C:\YURI"
                song_to_play = "music.mp3"
                songs = os.listdir(music_dir)
                for song in songs:
                    if song.endswith('.mp3') and song == song_to_play:
                        os.startfile(os.path.join(music_dir, song))

            elif "click my photo" in query:
                        pyautogui.hotkey('winleft','r')
                        pyautogui.typewrite('microsoft.windows.camera:')
                        pyautogui.press("enter")
                        pyautogui.sleep(2)
                        speak("SMILE")
                        pyautogui.press("enter")
                        pyautogui.sleep(2)
                        pyautogui.press("enter")

            elif "open camera" in query:
                        pyautogui.hotkey('winleft','r')
                        pyautogui.typewrite('microsoft.windows.camera:')
                        pyautogui.press("enter")

            elif "close camera" in query:
                    os.system("taskkill /im WindowsCamera.exe /f")

            elif 'play a movie' in query:
                npath = "C:\YURI\Boruto - Naruto the Movie (2015).mp4"

            elif 'play movie' in query:
                npath = "C:\YURI\Boruto - Naruto the Movie (2015).mp4"

            elif 'close movie' in query:
                os.system("taskkill /f /im vlc.exe")
            elif 'close music' in query:
                os.system("taskkill /f /im vlc.exe")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%I:%M %p") 
                speak(f"Sir, the time is {strTime}")
            elif "shut down the system" in query:
                os.system("shutdown /s /t 5")

            elif "shutdown the system" in query:
                os.system("shutdown /s /t 5")
            elif "restart the system" in query:
                os.system("shutdown /r /t 5")
            elif "lock the system" in query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        
            elif "open notepad" in query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)    
            elif "close notepad" in query:
                os.system("taskkill /f /im notepad.exe")
            elif "open command prompt" in query:
                os.system("start cmd")
    
            elif "close command prompt" in query:
                os.system("taskkill /f /im cmd.exe")

            elif "search for my resume" in query:
                pdf_path = "C:\\YURI\\RAIHAN_RESUME_UPDATED.pdf"
                os.startfile(pdf_path)

            elif "open files" in query:
                pyautogui.hotkey('winleft','r')
                pyautogui.typewrite('explorer')
                pyautogui.press('enter')

            elif "close files" in query:
                pyautogui.hotkey('ctrl','w')

            elif "search for file" in query:
                pyautogui.hotkey('ctrl', 'f')
                speak("what should i search")

            elif "search file" in query:
                pyautogui.hotkey('ctrl', 'f')
                speak("what should i search")

            elif "such fine" in query:
                pyautogui.hotkey('ctrl', 'f')
                speak("what should i search")


            elif "search for word" in query:
                pyautogui.hotkey('ctrl', 'f')
                speak("what should i search")

            elif "next" in query:
                pyautogui.press("enter")

                
            elif 'find' in query: 
                query = query.replace("find", "")
                pyautogui.write(f"{query}")

            elif "clear search" in query:
                pyautogui.hotkey('ctrl', 'f')
                pyautogui.press("backspace")   
            

            elif "clear all" in query:
                pyautogui.hotkey('ctrl', 'f')
                pyautogui.press("backspace")

            elif "close pdf" in query:
                os.system("taskkill /f /im msedge.exe") 

            elif "search for project report" in query:
                pdf_path = "C:\\YURI\\YURI_FINAL_REPORT.pdf"
                os.startfile(pdf_path)

            elif "project report" in query:
                pdf_path = "C:\\YURI\\YURI_FINAL_REPORT.pdf"
                os.startfile(pdf_path)
                
        
        
            elif "go to sleep" in query:
                speak(' alright then, I am switching off')
                playsound(r'C:\\Yuri\\mixkit-negative-tone-interface-tap-2569.wav')
                p1.terminate()
                main()

            elif "take screenshot" in query:
                speak('tell me a name for the file')
                name = takeCommand().lower()
                time.sleep(3)
                img = pyautogui.screenshot() 
                img.save(f"{name}.png") 
                speak("screenshot saved")

            

            elif "take a screenshot" in query:
                speak('tell me a name for the file')
                name = takeCommand().lower()
                time.sleep(3)
                img = pyautogui.screenshot() 
                img.save(f"{name}.png") 
                speak("screenshot saved")    
                
            elif "calculate" in query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("ready")
                    print("Listning...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string=r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided' : operator.__truediv__,
                    }[op]
                def eval_bianary_expr(op1,oper, op2):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("your result is")
                speak(eval_bianary_expr(*(my_string.split())))
            elif "what is my ip address" in query:
                speak("Checking")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    speak("your ip adress is")
                    speak(ipAdd)
                except Exception as e:
                    speak("network is weak, please try again some time later")
            elif "volume up" in query:
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
    
            elif "volume down" in query:
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")

            elif "increase volume" in query:
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
    
            elif "decrease volume" in query:
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
            

            elif "mute" in query:
                pyautogui.press("volumemute")

            elif "increase brightness" in query:
                current_brightness = wmi_obj.WmiMonitorBrightness()[0].CurrentBrightness
                new_brightness = int(min(current_brightness + 50, 100))
                methods = wmi_obj.WmiMonitorBrightnessMethods()[0]
                methods.WmiSetBrightness(new_brightness, 0)
                speak("Brightness increased.")

            elif "decrease brightness" in query:
                current_brightness = wmi_obj.WmiMonitorBrightness()[0].CurrentBrightness
                new_brightness = int(max(current_brightness - 50, 0))
                methods = wmi_obj.WmiMonitorBrightnessMethods()[0]
                methods.WmiSetBrightness(new_brightness, 0)
                speak("Brightness decreased.")
                
            elif "refresh" in query:
                pyautogui.moveTo(1551,551, 2)
                pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
                pyautogui.moveTo(1620,667, 1)
                pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')

            elif "scroll pdf" in query:
                #pyautogui.scroll(1000)
                pyautogui.click(x=350 , y=350)
                pyautogui.press('pagedown')
            
            elif "scroll down" in query:
                #pyautogui.scroll(1000)
                pyautogui.press('pagedown')

            elif "scroll up" in query:
                pyautogui.press('pageup')    

            elif "drag visual studio to the right" in query:
                pyautogui.moveTo(46, 31, 2)
                pyautogui.dragRel(1857, 31, 2)
            elif "drag Visual Studio to the right" in query:
                pyautogui.moveTo(46, 31, 2)
                pyautogui.dragRel(1857, 31, 2)    

            elif "open paint" in query:
                pyautogui.hotkey('winleft','r')
                pyautogui.typewrite('mspaint')
                pyautogui.press('enter')


            elif "draw a square" in query:
                pyautogui.moveTo(350, 350, duration=1)
                pyautogui.drag(100, 0, duration=0.25)  # move right
                pyautogui.drag(0, 100, duration=0.25)  # move down
                pyautogui.drag(-100, 0, duration=0.25)  # move left
                pyautogui.drag(0, -100, duration=0.25)  # move up
                speak("square drawn")
            
            elif "draw square" in query:
                pyautogui.moveTo(350, 350, duration=1)
                pyautogui.drag(100, 0, duration=0.25)  # move right
                pyautogui.drag(0, 100, duration=0.25)  # move down
                pyautogui.drag(-100, 0, duration=0.25)  # move left
                pyautogui.drag(0, -100, duration=0.25)  # move up
                speak("square drawn")

            elif "draw a triangle" in query:
                
                pyautogui.moveTo(699, 699, duration=1)
                pyautogui.drag(200, 200, duration=0.5)
                pyautogui.drag(-400, 0, duration=0.5)
                pyautogui.drag(200, -200, duration=0.5)
                speak("Triangle drawn")

            elif "draw triangle" in query:
                
                pyautogui.moveTo(699, 699, duration=1)
                pyautogui.drag(200, 200, duration=0.5)
                pyautogui.drag(-400, 0, duration=0.5)
                pyautogui.drag(200, -200, duration=0.5)
                speak("Triangle drawn")

            elif "Triangle" in query:
                
                pyautogui.moveTo(699, 699, duration=1)
                pyautogui.drag(200, 200, duration=0.5)
                pyautogui.drag(-400, 0, duration=0.5)
                pyautogui.drag(200, -200, duration=0.5)
                speak("Triangle drawn")


            elif "rectangular spiral" in query:

                pyautogui.moveTo(1111, 400, duration=1)
                distance = 300
                while distance > 0:
                    pyautogui.dragRel(distance, 0, 0.1, button="left")
                    distance = distance - 10
                    pyautogui.dragRel(0, distance, 0.1, button="left")
                    pyautogui.dragRel(-distance, 0, 0.1, button="left")
                    distance = distance - 10
                    pyautogui.dragRel(0, -distance, 0.1, button="left")
                    
                speak("Rectangular spiral drawn")

            
        

    # function to draw a tree
            elif "draw a tree" in query:
                pyautogui.click(1620, 190)

            # Select the brush tool
                pyautogui.click(930, 160)

    # Set the brush size to 20 pixels
                pyautogui.click(1090, 220)
                pyautogui.press('down', presses=5)
                pyautogui.click(930, 240)
                pyautogui.press('down', presses=7)

    # Draw the tree trunk
                pyautogui.moveTo(500, 500)
                pyautogui.dragTo(500, 400, duration=0.5)

    # Draw the tree branches
                pyautogui.moveTo(500, 400)
                pyautogui.dragTo(400, 400, duration=0.5)
                pyautogui.moveTo(500, 400)
                pyautogui.dragTo(600, 400, duration=0.5)
                pyautogui.moveTo(500, 400)
                pyautogui.dragTo(450, 350, duration=0.5)
                pyautogui.moveTo(500, 400)
                pyautogui.dragTo(550, 350, duration=0.5)
                speak("tree drawn")

      
            elif 'draw a house' in query:
        # draw the house
                pyautogui.moveTo(600, 600)
                pyautogui.dragRel(100, 0, duration=0.25)
                pyautogui.dragRel(0, -100, duration=0.25)
                pyautogui.dragRel(-100, 0, duration=0.25)
                pyautogui.dragRel(0, 100, duration=0.25)
                # draw the roof
                pyautogui.moveTo(600, 500)
                pyautogui.dragRel(50, -50, duration=0.25)
                pyautogui.dragRel(50, 50, duration=0.25)
                # draw the door
                pyautogui.moveTo(650, 600)
                pyautogui.dragRel(-30, 0, duration=0.25)
                pyautogui.dragRel(0, -50, duration=0.25)
                pyautogui.dragRel(30, 0, duration=0.25)
                speak("house drawn")

            elif "save document" in query:
                speak("saving document...")
                pyautogui.hotkey('ctrl', 's')
                time.sleep(1) # wait for the save dialog to appear
                speak("Please suggest a name for the file")
                name = takeCommand().lower()
                time.sleep(3)
                pyautogui.write(name + ".txt")
                time.sleep(1)
                pyautogui.press('enter')
                speak(f"Document {name} saved.")



            elif "save the drawing" in query:
                pyautogui.hotkey('ctrl', 's')
                pyautogui.write('drawing.png')
                pyautogui.hotkey('enter')
                speak("Drawing Saved")
            
            elif "save drawing" in query:
                pyautogui.hotkey('ctrl', 's')
                pyautogui.write('drawing.png')
                pyautogui.hotkey('enter')
                speak("Drawing Saved")

            elif "please save the drawing" in query:
                pyautogui.hotkey('ctrl', 's')
                speak("suggest a name for the file")
                query = query.replace("type", "")
                pyautogui.write(f"{query}")
                pyautogui.hotkey('enter')
                speak("Drawing Saved")


            elif 'erase all' in query:
                pyautogui.hotkey('ctrl', 'n')
                pyautogui.press("tab")
                pyautogui.press("enter")
                speak("drawing erased")


            elif "close paint" in query:
                os.system("taskkill /f /im mspaint.exe")

            elif "who are you" in query:
                print('My Name Is Yuri')
                speak('My Name Is Yuri')
                print('I can Do Everything that my creator programmed me to do')
                speak('I can Do Everything that my creator programmed me to do')
    
            elif "who created you" in query:
                print('I was created by Batch 11, I created with Python Language, in Visual Studio Code.')
                speak('I was created by Batch 11, I created with Python Language, in Visual Studio Code.')

            elif "open notepad and write my name" in query:
                pyautogui.hotkey('win')
                time.sleep(1)
                pyautogui.write('notepad')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.write("Mohamed Raihan", interval = 0.1)
            
            elif "open Notepad and write my name" in query:
                pyautogui.hotkey('win')
                time.sleep(1)
                pyautogui.write('notepad')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.write("Mohamed Raihan", interval = 0.1)

            elif "write my name" in query:
                pyautogui.write("Mohamed Raihan", interval = 0.1)

            elif "write my favourite sport" in query:
                pyautogui.write(" Football", interval = 0.1)

            elif "write my favourite player" in query:
                pyautogui.write(" Cristanio Ronaldo", interval = 0.1)    



            elif "open Notepad Android my name" in query:
                pyautogui.hotkey('win')
                time.sleep(1)
                pyautogui.write('notepad')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.write("Mohamed Raihan", interval = 0.1)
        
            elif "save document" in query:
                speak("saving document...")
                pyautogui.hotkey('ctrl', 's')
                time.sleep(1) # wait for the save dialog to appear
                speak("Please enter a name for the file")
                name = takeCommand().lower()
                time.sleep(3)
                pyautogui.write(name + ".txt") # enter the filename with .txt extension
                time.sleep(1)
                pyautogui.press('enter')
                speak(f"Document {name} saved.")
 

            elif 'save' in query:
                pyautogui.hotkey('ctrl', 's') 
                


            elif 'enter' in query:
                pyautogui.hotkey('enter')

            elif 'inter' in query:
                pyautogui.hotkey('enter')      

            

            elif "who am i" in query:
                speak("you are Mr. Mohamed Raihan")    

            elif "what is my favourite sport" in query:
                speak("your favourite sport is football")
            elif "who is my favourite player" in query:
                speak("your favourite player is Cristanio Ronaldo!")        
    
            elif 'type' in query: #10
                query = query.replace("type", "")
                pyautogui.write(f"{query}")
            
            elif "you are trash" in query:
                #rate = engine.getProperty('rate')
                engine.setProperty('rate', 125)
                speak("i am  trash but you are trash bin and i am always inside you hahaha")  


            elif 'open chrome' in query:
                os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')

            elif 'maximize this window' in query:
                pyautogui.hotkey('alt', 'space')
                time.sleep(1)
                pyautogui.press('x')

            elif 'maximize window' in query:
                pyautogui.hotkey('alt', 'space')
                time.sleep(1)
                pyautogui.press('x')
            
            elif 'google search' in query:
                query = query.replace("google search", "")
                pyautogui.hotkey('alt', 'd')
                pyautogui.write(f"{query}", 0.1)
                pyautogui.press('enter')

            elif 'Google search' in query:
                query = query.replace("google search", "")
                pyautogui.hotkey('alt', 'd')
                pyautogui.write(f"{query}", 0.1)
                pyautogui.press('enter')
                

            
            elif 'open new window' in query:
                pyautogui.hotkey('ctrl', 'n')

            elif 'open incognito window' in query:
                pyautogui.hotkey('ctrl', 'shift', 'n')
            elif 'minimise this window' in query:
                pyautogui.hotkey('alt', 'space')
                time.sleep(1)
                pyautogui.press('n')
            elif 'open history' in query:
                pyautogui.hotkey('ctrl', 'h')
            elif 'open downloads' in query:
                pyautogui.hotkey('ctrl', 'j')

            elif 'new tab' in query:
                pyautogui.hotkey('ctrl','t')    

            elif 'previous tab' in query:
                pyautogui.hotkey('ctrl', 'shift', 'tab')  

            elif 'next tab' in query:
                pyautogui.hotkey('ctrl', 'tab')
            elif 'close tab' in query:
                pyautogui.hotkey('ctrl', 'w')
            elif 'close window' in query:
                pyautogui.hotkey('ctrl', 'shift', 'w')

            elif 'clear browsing history' in query:
                pyautogui.hotkey('ctrl', 'shift', 'delete')


            elif 'Clear browsing history' in query:
                pyautogui.hotkey('ctrl', 'shift', 'delete')

            elif 'close chrome' in query:
                
                os.system("taskkill /f /im chrome.exe")    
        
            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")
            
            #to close youtube
            elif "close youtube" in query:
                os.system("taskkill /im chrome.exe /f")

            elif "youtube search" in query:
                #if connect() == True:
                import pywhatkit
                speak("What do you want me to search for?")
                search_term = takeCommand().lower()
                speak(f"Searching YouTube for {search_term}")
                pywhatkit.playonyt(search_term)
            
            elif "tell me news" in query:
                speak("please wait sir, feteching the latest news")
                news()

            

            elif "please send whatsapp message" in query:
                    #if connect() == True:
                    import pywhatkit
                    speak("Whom do you want to send the message")
                    per=takeCommand()
                    speak("What's the message you want to send")
                    msg=takeCommand()
                    speak("Your message will be sent shortly")
                    time.sleep(3)
                    pywhatkit.sendwhatmsg_instantly("+91"+per, msg)
                    speak("Message sent successfully!")

           
          
            elif "send a Whatsapp message" in query:
                    #if connect() == True:
                    import pywhatkit
                    speak("Whom do you want to send the message")
                    per=takeCommand()
                    speak("What's the message you want to send")
                    msg=takeCommand()
                    speak("Your message will be sent shortly")
                    time.sleep(3)
                    pywhatkit.sendwhatmsg_instantly("+917899688068"+per, msg)
                    speak("Message sent successfully!") 
                         

            elif "alarm" in query:
                speak("Say the time for the alarm in the format 'hour:minute am/pm' (example '7:30 am'):")
                
                try:
                    text = queryy()
                    print("You said: {}".format(text))
                    speak("You said: {}".format(text))
                    speak("Alaram set successfully")
                    # Parse the text input to extract the hour, minute, and am/pm indicator
                    time_parts = text.split()
                    hour, minute = [int(t) for t in time_parts[0].split(':')]
                    am_pm = time_parts[1].lower()

                    # Adjust the hour based on the am/pm indicator
                    if am_pm == 'p.m.' and hour != 12:
                        hour += 12
                    elif am_pm == 'a.m.' and hour == 12:
                        hour = 00

                    # Get the current time
                    now = datetime.datetime.now()

                    # Set the alarm time
                    alarm_time = datetime.datetime(now.year, now.month, now.day, hour, minute, 0)

                    # Wait until the alarm time is reached
                    while datetime.datetime.now() < alarm_time:
                        time.sleep(1)

                    # Play the alarm sound
                    speak("Time's up!")
                    speak("Time's up!")
                    speak("Time's up!")
                    # Add code here to play the alarm sound

                except Exception as e:
                    speak("Sorry, I didn't understand that.")
                    queryy() 

            

            elif "email" in query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath) 
                speak("whom do you want to send the  mail")
                per=takeCommand().lower()
                if per=="farooq":
                    receiver="hagalwadimohammed@gmail.com"
                    pyautogui.write(receiver)
                    pyautogui.write("\n\n")
                else:
                    receiver = per
                    receiver = receiver.lower().replace(" ", "")+"@gmail.com"
                    pyautogui.write(receiver)
                    pyautogui.write("\n\n") 
                    
                speak("What should be the subject of the email?")
                subject = takeCommand()
                pyautogui.write(subject)
                pyautogui.write("\n\n") 

                speak("What message would you like to include in the email?")
                body =takeCommand()
                pyautogui.write(body)
                pyautogui.write("\n\n") 
                speak("you said")
                speak(receiver)
                speak(subject)
                speak(body)

                while True:
                    speak("Check if details are correct")
                    response=takeCommand().lower()
                    if "yes" in response:
                        break
                    elif "yeah" in response:
                        break
                    else:
                        speak("What do you like to change")
                        rep=takeCommand().lower() 
                        if "email" in rep:
                            speak("Please tell the email id")
                            receiver=takeCommand()
                            receiver = receiver.lower().replace(" ", "")+"@gmail.com"
                            pyautogui.write(receiver)
                            pyautogui.write("\n\n") 
                        elif "subject" in rep:
                            speak("what do you want to be subject")
                            subject=takeCommand()
                            pyautogui.write(subject)
                            pyautogui.write("\n\n") 
                        elif "message" in rep:
                            speak("what do you want to be message")
                            body=takeCommand()
                            pyautogui.write(body)
                            pyautogui.write("\n\n") 
                message = f"Subject: {subject}\n\n{body}"
                try:
                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.login(username, password)
                    server.sendmail(username, receiver, message)
                    server.quit()
                    speak("Email sent successfully!")
                except Exception as e:
                    speak("Failed to send email.")
                os.system("taskkill /f /im notepad.exe")
                
            elif "inbox" in query:
                imap_server = 'imap.gmail.com'
                imap_port = 993
                mail = imaplib.IMAP4_SSL(imap_server, imap_port)

                # Log in to your account
                mail.login(username, password)

                # Select the mailbox to count messages in (in this case, the inbox)
                mail.select('INBOX')
                today = datetime.date.today()
                # Search for all messages in the selected mailbox
                result, data = mail.search(None, f'(SENTON {today.strftime("%d-%b-%Y")})')
                nummes = data[0].split()
                numm = len(nummes)

                senders = []
                for num in nummes:
                    result, data = mail.fetch(num, '(BODY[HEADER.FIELDS (FROM)])')
                    sender = email.message_from_bytes(data[0][1]).get('From')
                    senders.append(sender)

                speak(f"You have got {numm} mails from")
                for sender in set(senders):
                    speak(sender)
                speak("Do you want me to read out the subjects of the email")
                repp=takeCommand()
                if "yes" in repp:
                    for num in nummes:
                        result, data = mail.fetch(num, '(RFC822)')
                        raw_email = data[0][1]
                        email_message = email.message_from_bytes(raw_email)

                        # Get the subject of the email
                        subject = decode_header(email_message["Subject"])[0][0]
                        if isinstance(subject, bytes):
                            # If the subject is bytes, decode it to str
                            subject = subject.decode()

                        # Get the sender of the email
                        sender = decode_header(email_message["From"])[0][0]
                        if isinstance(sender, bytes):
                            # If the sender is bytes, decode it to str
                            sender = sender.decode()

                        speak("mail from")
                        speak(sender)
                        speak("Subject says")
                        speak(subject)
                else:
                    continue
            elif "open spotify" in query:
                pyautogui.hotkey('winleft', 'r')
                pyautogui.typewrite('C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.188.612.0_x86__zpdnekdrzrea0\\Spotify.exe')
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.press('playpause')
                

            elif "next track" in query:
                pyautogui.press('nexttrack')

            elif "pause" in query:
                pyautogui.press('playpause') 

            elif "stop" in query:
                pyautogui.press('playpause')

            elif "play" in query:
                pyautogui.press('playpause')

            elif "previous track" in query:
                pyautogui.press('prevtrack')
                pyautogui.press('prevtrack')
            
            elif "liked songs" in query:
                pyautogui.hotkey('winleft', 'r')
                pyautogui.typewrite('C:\\Users\\OneDrive\\Desktop\\Spotify.lnk')
                pyautogui.press('enter')
                time.sleep(3)
                pyautogui.hotkey('ctrl','l')
                time.sleep(2)
                pyautogui.write('liked songs')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.press('tab')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('enter')

            elif "live songs" in query:
                pyautogui.hotkey('winleft', 'r')
                pyautogui.typewrite('C:\\Users\\mohmmed raihaan\\OneDrive\\Desktop\\Spotify.lnk')
                pyautogui.press('enter')
                time.sleep(5)
                pyautogui.hotkey('ctrl','l')
                time.sleep(3)
                pyautogui.write('liked songs')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.press('tab')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('enter')

            elif "play liked songs" in query:
                pyautogui.hotkey('winleft', 'r')
                pyautogui.typewrite('C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.188.612.0_x86__zpdnekdrzrea0\\Spotify.exe')
                pyautogui.press('enter')
                time.sleep(5)
                pyautogui.hotkey('ctrl','l')
                time.sleep(3)
                pyautogui.write('liked songs')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.press('tab')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('enter')

            elif "play live songs" in query:
                pyautogui.hotkey('winleft', 'r')
                pyautogui.typewrite('C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.188.612.0_x86__zpdnekdrzrea0\\Spotify.exe')
                pyautogui.press('enter')
                time.sleep(5)
                pyautogui.hotkey('ctrl','l')
                time.sleep(3)
                pyautogui.write('liked songs')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.press('tab')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('enter')

            elif "close spotify" in query:
                os.system("taskkill /f /im spotify.exe")

            elif "look for a song" in query:
                speak("what do you want to hear")
                song=takeCommand()
                pyautogui.hotkey('winleft', 'r')
                pyautogui.typewrite('C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.188.612.0_x86__zpdnekdrzrea0\\Spotify.exe')
                pyautogui.press('enter')
                pyautogui.press('playpause')
                time.sleep(5)
                #pyautogui.press('playpause')
                
                time.sleep(10)
                pyautogui.hotkey('ctrl','l')
                time.sleep(5)
                pyautogui.write(song)
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.press('tab')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.press('enter')

            elif "open chat" in query:
                
                
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath) 

            
                speak("What should I do?")
                
            
                time.sleep(2)
                program_request = takeCommand()
                if "write a program to add two numbers" in program_request:
                    
                    program_prompt = "write a program to add two numbers."
                    program = generate_program(program_prompt)
                    pyautogui.write(program)
                    pyautogui.write("\n\n") 
                else:
                    
                    program_prompt = "write a program to " + program_request
                    program = generate_program(program_prompt)
                    pyautogui.write(program)
                    pyautogui.write("\n\n")  

            elif "write a program" in query:
            
                speak("What program would you like me to write?")
                time.sleep(2)

                program_request = takeCommand()
                program_prompt = "write a program " + program_request
                program = generate_program(program_prompt)
                pyautogui.write(program)
                pyautogui.write("\n\n") 

        
            elif "close chat" in query:
                
                    os.system("taskkill /f /im notepad.exe")

                
           
        


            elif "terminate" in query:
                speak(' alright then, I am switching off')
                p1.terminate()
                sys.exit()

            
                    
        except Exception as e:  
            print(e)

if __name__ == "__main__":
    main()
       
        

        
