import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys
import requests
import time




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)    
    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Good Morning")
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Good Evening")
        print("Good Evening")
    print("I am Pluto sir. Please tell me how may I help you....") 
    speak("I am Pluto sir. Please tell me how may I help you") 
       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:  
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  

    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    return query   

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('djtushar4902@gmail.com','coccoccoc3')
    server.sendmail('djtushar4902@gmail.com', to, content)    
    server.close()

def givenews():
    apiKey = '483968ba8e02471595f2c0f864261f56'
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={apiKey}"
    r = requests.get(url)
    data = r.json()
    data = data["articles"]
    flag = True
    count = 0
    for items in data:
        count += 1
        if count > 10:
            break
        print(items["title"])
        to_speak = items["title"].split(" - ")[0]
        if flag:
            speak("Today's top ten Headlines are : ")
            flag = False
        else:
            speak("Next news :")
        speak(to_speak)



def giveweather():
    api_address="http://api.openweathermap.org/data/2.5/weather?units=metric&appid=0c42f7f6b53b244c78a418f4f181282a&q=Delhi"
    url = api_address 
    json_data = requests.get(url).json()
    format_add = json_data['weather'][0]['main']
    d = json_data['main']['pressure']
    e = json_data['main']['humidity']
    print(f"The weather of Delhi Today is {format_add}")
    speak(f"The weather of Delhi today is {format_add}")
    print(f"The air pressure is {d} atmospheric pressure")
    speak(f"The air pressure is {d} atmospheric pressure")
    print(f"The humidity in air is {e} %")
    speak(f"The humidity in air is {e} percent")


def givetemperature():
    api_address ="http://api.openweathermap.org/data/2.5/weather?units=metric&appid=0c42f7f6b53b244c78a418f4f181282a&q=Delhi"    
    url = api_address  
    json_data = requests.get(url).json()
    a = json_data['main']['temp']
    b = json_data['main']['temp_min']
    c = json_data['main']['temp_max']
    d = json_data['main']['feels_like']
    if (a == b and b== c):
        print(f"The average temperature and the highs and lows are the exact same that is {a} degree celsius")
        speak(f"The average temperature and the highs and lows are the exact same that is {a} degree celsius")
        print(f"But to be very honest it feels like {d} degree celsius when you go outside")
        speak(f"But to be very honest it feels like {d} degree celsius when you go outside")
    else:
        print(f"The average temperature in Delhi is {a} degree celsius")
        speak(f"The average temperature in Delhi is {a} degree celsius")
        print(f"But to be very honest it feels like {d} degree celsius when you go outside")
        speak(f"But to be very honest it feels like {d} degree celsius when you go outside")
        print(f"Though the temperature can goes down to {b} degree celsius")
        speak(f"Though the temperature can goes down to {b} degree celsius")
        print(f"Also the temperature could rise up to {c} degree celsius")
        speak(f"Also the temperature could rise up to {c} degree celsius") 



def clear():
    _ = os.system('cls')


if _name_ == "_main_":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")

            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)



        elif 'who are you' in query or 'what can you do' in query:
            speak("I am PLuto version 1 point O your personal assistant. I am programmed to do some tasks like opening youtube google, gmail and stackoverflow, predict time, playing your favourite video, playing music, searching queries on wikipedia, predict weather and temperature too In different cities, get top headline news from times of india and last but not the least I can send your mails too")


        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Bhaskar Nag")
            print("I was built by Bhaskar Nag")

        elif 'open youtube' in query:
            speak('Opening youtube ')  
            webbrowser.open("youtube.com")
           
        elif 'open google' in query:
            speak('Opening google')
            webbrowser.open("google.com") 

        elif 'open course era' in query:
            speak('Opening Coursera ') 
            webbrowser.open("coursera.com") 

        elif 'open udemy' in query:
            speak('opening udemy')
            webbrowser.open("udemy.com")
        
        elif 'search'  in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(5)


        elif 'open stack overflow' in query:
            speak('opening stack overflow')
            webbrowser.open("stackoverflow.com")

        elif 'open gmail' in query:
            speak('opening gmail')
            webbrowser.open("gmail.com")  
             
        elif 'open LinkedIn' in query:
            speak('opening linkedin..')
            webbrowser.open("linkedin.com")     

        elif 'play music' in query:
            music_dir = "D:\Music"
            songs = os.listdir(music_dir)
          
            speak('Playing music..')
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play video' in query:
            video_dir = "D:\Friends Season 1 COMPLETE 720p.BRrip.sujaidr (pimprg)"  
            video = os.listdir(video_dir)
            speak('playing video...')
            os.startfile(os.path.join(video_dir, video[0])) 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)  
            speak(f"Sir, the time is {strTime}")  

        elif 'open visual studio' in query:
            codePath = "C:\\Users\\bhaskar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"    
            speak("Opening Visual studio code...")
            os.startfile(codePath)

        elif 'open vlc' in query:
            codePath = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"    
            speak("Opening VLC Media Player...")
            os.startfile(codePath)


        elif 'open pycharm' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2018.3.2\\bin\\pycharm64.exe"    
            speak("Opening PyCharm IDE...")
            os.startfile(codePath)  

        elif 'open anydesk' in query:
            codePath = "C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe"    
            speak("Opening Anydesk...")
            os.startfile(codePath)    


        elif 'email to bhaskar' in query:
            try:
                speak("What should I say?..")
                content = takeCommand()
                to = "bhaskar.nag2937@gmail.com"
                sendEmail(to, content)
                print("Email has been sent!")
                speak("Email has been sent!")    
            except Exception as e:
                print(e)
                speak("Sorry!! we could not deliver your email at this moment")
       
        elif 'headlines' in query or 'news' in query or 'headline' in query:
            givenews()
            
        elif 'weather' in query or 'quote' in query:
            giveweather() 

        elif 'temperature' in query or 'temp' in query:
            givetemperature()   


        elif 'quit' in query or 'exit' in query:
            speak("Good bye sir!! Have a wonderful day ahead... ")
            sys.exit(0)