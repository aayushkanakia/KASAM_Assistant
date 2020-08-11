# importing speech recognition package from google api 
import datetime
import webbrowser
import speech_recognition as sr  
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import wolframalpha # to calculate strings into formula 
from selenium import webdriver # to control browser operations 
from datetime import time

currentDT = datetime.datetime.now()


r = sr.Recognizer()

num = 1
def assistant_speaks(output): 
    global num 
  
    # num to rename every audio file  
    # with different name to remove ambiguity 
    num += 1
    print("KASAM: ", output) 
  
    toSpeak = gTTS(text = output, lang ='en', slow = False) 
    # saving the audio file given by google text to speech 
    file = (str(num)+" .mp3")  
    toSpeak.save(file) 
      
    # playsound package is used to play the same file. 
    playsound.playsound(file, True)  
    os.remove(file) 
  
  
  
def get_audio(): 
  
    rObject = sr.Recognizer() 
    audio = '' 
  
    with sr.Microphone() as source: 
        print("Speak...") 
          
        # recording the audio using speech recognition 
        audio = rObject.listen(source, phrase_time_limit = 5)  
    print("Stop.") # limit 5 secs 
  
    try: 
  
        text = rObject.recognize_google(audio, language ='en-IND') 
        return text 
  
    except: 
  
        assistant_speaks("I am sorry sir I did not quite get you") 
        return 0








# Driver Code 
if currentDT.hour < 12:
    assistant_speaks("Good Morning! How may I assist you?")
elif 12 <= currentDT.hour < 18:
    assistant_speaks("Good Afternoon! How may I assist you?")
else:
    assistant_speaks("Good Evening! How may I assist you?")


a = get_audio()

if "time" in str(a):
    assistant_speaks("It is " + str(currentDT))

elif "Netflix" in str(a) or "netflix" in str(a):
    assistant_speaks("Streaming Netflix!")
    os.system("start Netflix:")

elif "Spotify" in str(a) or "spotify" in str(a):
    assistant_speaks("Spotify right up on your screen sir!")
    os.system("start Spotify:")

elif "Itunes" in str(a) or "itunes" in str(a):
    assistant_speaks("Loading all your tracks sir!")
    os.system("start itunes:")

elif "Google" in str(a):
    webbrowser.open('www.google.com')

elif "Hi" in str(a) or "Hey" in str(a) or "yo" in str(a) or "Hello" in str(a):
    assistant_speaks("Hello! I am KASAM, your new virtual assistant. And who might you be?")
    b = get_audio()
    assistant_speaks("Greetings!" + b )

elif "locate" in str(a):
    assistant_speaks("Ok! What shall I locate for you?")
    c = get_audio()
    assistant_speaks("Locating " + str(c))
    webbrowser.open("https://www.google.com/maps/search/" + str(c))   

elif "Google search" in str(a) or "search Google" in str(a):
    assistant_speaks("YEAH! What shall I search for on Google?")
    d = get_audio()
    webbrowser.open("https://google.com/search/" + str(d))

elif "calculator" in str(a):
    assistant_speaks("Opening Calculator for you!")
    os.system("start Calculator:")

elif "calendar" in str(a):
    assistant_speaks("Opening Calendar for you!")
    os.system("start Calendar:")

elif "word" in str(a):
    assistant_speaks("Opening Microsoft Word!")
    os.system("start Word:")

elif "Excel" in str(a):
    assistant_speaks("Opening Microsoft Excel!")
    os.system("start Excel:")
elif "exit" in str(a) or "bye" in str(a) or "goodbye" in str(a):
    assistant_speaks("Aye aye! Goodbye!")
    'break'

