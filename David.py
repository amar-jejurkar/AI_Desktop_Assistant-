# Artificial Intenligence voice Assistant software


import pyttsx3                   #pip install Pyttsx3   
import speech_recognition as sr      #pip install Speech_Recognition
import datetime
import wikipedia                    #pip install wikipedia
import webbrowser                    #pip install webbrowser
import os
import smtplib
import playsound
import json 
import ctypes 
import subprocess 
import requests 
import pyaudio
import time
import wolframalpha
 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")   

    else:
        print("Good Evening!") 
        speak("Good Evening!")  
    
    print("I am Artificial intelligence assistant . Please tell me how may I help you")
    speak("I am Artificial intelligence assistant. Please tell me how may I help you")       

def takeCommand():
    

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('amarjejurkar58@gmail.com', 'amarjejurkar@2105')     #Enter your email and password
    server.sendmail('amarjejurkar58@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif ' open youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(0.5)

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("google is open now")

        elif 'open amazon' in query:
                webbrowser.open("https://www.amazon.com")
                speak("amazon is open now")     


        elif 'play music' in query:
            music_dir = 'C:\\Users\\DELL\\Music\\gana' #Enter your system song location
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            time.sleep(0.5)
            


        elif ' time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(f"Sir, the time is {strTime}")   
            speak(f"Sir, the time is {strTime}")
            

        elif 'open word' in query:
            wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE" #Mention location of word in your system
            os.startfile(wordPath)

        elif 'open powerpoint' in query:
            wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE" #Mention location of word in your system
            os.startfile(wordPath)    
                    
        
        elif "who made you" in query or "who created you"  in query:
            speak("I was built by computer science engineer ")
        
        elif 'who are you' in query:
            speak('I am G-one version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')

        
        elif 'calculation' in query:
           speak('I can answer to computational and geographical questions  and what question do you want to ask now')
           question=takeCommand()
           app_id="KH9EW4-6423HHHXEY "
           client = wolframalpha.Client('R2K75H-7ELALHR35X')
           res = client.query(question)
           answer = next(res.results).text
           speak(answer)
           print(answer) 

        elif "weather" in query:
            api_key="e2e0898d068d84b27f1a2b8c56513485"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))   

        elif 'search'  in query:
            query = query.replace("https://www.google.com", "")
            webbrowser.open_new_tab(query)
            time.sleep(5)     


              
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")

 
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

          


        elif 'email to rahul' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "amaryourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend amar bhai. I am not able to send this email")    

                
        else:
            exit