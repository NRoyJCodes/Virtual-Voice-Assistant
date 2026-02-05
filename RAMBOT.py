import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
import pyaudio
import time
import subprocess
from Greetings import query_reply
import requests

import wikipedia
import wolframalpha #This will be used to compute queries such as 'what is the weather today?'
from bs4 import BeautifulSoup #This will be used to scrape data from websites


class RAMBOT:

    def __init__(self,mic,engine):
        self.mic = mic
        self.engine = engine
        self.name = "RAMBOT"
        self.creator = "Manish"
        self.age = "I am created on april 2024"


    def listen(self):
        with self.mic as source:
            print("Listening...")
            audio = self.r.listen(source)
            query = self.r.recognize_google(audio)
            return query
        
    def speak(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query
    
    def wishme(self):
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            self.speak("Good Morning!")
        elif hour>=12 and hour<18:
            self.speak("Good Afternoon!")
        else:
            self.speak("Good Evening!")
        self.speak("I am your Assistant. Please tell me how may I help you")


    def results(self,query):
        try:
            # Wolfram Alpha API
            app_id = "GLJ2WH-VLQ6QQ8VYT"
            client = wolframalpha.Client(app_id)
            res = client.query(query)
            answer = next(res.results).text
            return answer
        except:
            try:
                # Wikipedia API
                wikipedia.set_lang("en")
                answer = wikipedia.summary(query, sentences=2)
                return answer
            except:
                try:
                    # Web Scraping
                    url = "https://www.google.com/search?q=" + query
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
                    res = requests.get(url, headers=headers)
                    soup = BeautifulSoup(res.text, 'html.parser')
                    answer = soup.select_one('.kno-rdesc span')
                    if answer is not None:
                        return answer.text
                    else:
                        return "Sorry, I couldn't find an answer to your query."
                except:
                    return "Sorry, I couldn't find an answer to your query."
            
# This is the function that will be used to open the browser

    def openBrowser(self):
        webbrowser.open('https://www.google.com/')
        return "Opening Google"

# This is the function that will be used to open the calculator

    def openCalculator(self):
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        return "Opening Calculator"

# This is the function that will be used to open the camera

    def openCamera(self):
        subprocess.Popen('C:\\Windows\\System32\\Camera.exe')
        return "Opening Camera"



# This is the function that will be used to open the clock

    def openClock(self):
            subprocess.Popen('C:\\Windows\\System32\\cmd.exe /c start shell:Appsfolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App')
            return "Opening Clock"

# This is the function that will be used to open the control panel

    def openControlPanel(self):
        subprocess.Popen('C:\\Windows\\System32\\control.exe')
        return "Opening Control Panel"


# This is the function that will be used to open the file explorer

    def openFileExplorer(self):

        subprocess.Popen('C:\\Windows\\explorer.exe')
        return "Opening File Explorer"


# This is the function that will be used to open the mail

    def openMail(self):

        subprocess.Popen('C:\\Windows\\System32\\cmd.exe /c start shell:Appsfolder\microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.mail')
        return "Opening Mail"


# This is the function that will be used to open the maps

    def openMaps(self):

        subprocess.Popen('C:\\Windows\\System32\\cmd.exe /c start shell:Appsfolder\Microsoft.WindowsMaps_8wekyb3d8bbwe!App')
        return "Opening Maps"


# This is the function that will be used to open the music player

    def openMusicPlayer(self):

        subprocess.Popen('C:\\Windows\\System32\\cmd.exe /c start shell:Appsfolder\Microsoft.ZuneMusic_8wekyb3d8bbwe!Microsoft.ZuneMusic')
        return "Opening Music Player"


# This is the function that will be used to open the notepad

    def openNotepad(self):
    
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
        return "Opening Notepad"


# This is the function that will be used to open the settings

    def openSettings(self):

        subprocess.Popen('C:\\Windows\\System32\\cmd.exe /c start shell:Appsfolder\windows.immersivecontrolpanel_cw5n1h2txyewy!microsoft.windows.immersivecontrolpanel')
        return "Opening Settings"


# This is the function that will be used to open the store

    def openStore(self):

        subprocess.Popen('C:\\Windows\\System32\\cmd.exe /c start shell:Appsfolder\Microsoft.WindowsStore_8wekyb3d8bbwe!App')
        return "Opening Store"



# This is the function that will be used to tell you the weather
    def weather(self):
        # Replace YOUR_API_KEY with your actual API key from OpenWeatherMap
        api_key = "Bd5e378503939ddaee76f12ad7a97608"

        # Replace CITY_NAME with the name of the city you want to get weather details for

        city_name = input("Enter the name of the city: ")

        # Make a GET request to the OpenWeatherMap API to get the weather details of the    city
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")

        # Extract the weather details from the response
        weather_data = response.json()
        weather_description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]

        # Print the weather details
        return f"The weather in {city_name} is {weather_description}. The temperature is {temperature} Kelvin and the humidity is {humidity}%."

        


# This is the function that will be used to tell you the time

    def time(self):

        current_date = datetime.datetime.now().strftime("%m/%d/%Y")
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        current_day = datetime.datetime.now().strftime("%A")
        return f'Today is {current_date} and the current date is {current_day}and the current time is {current_time}'

    def bot_normal_reply(self,query):
        print(query_reply(query))
        return query_reply(query)


    
# This is the main function that will be used to run the bot
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)
mic = sr.Microphone()

RAMBOT = RAMBOT(mic,engine)
user = RAMBOT
user.wishme()
# The main function , Also sepererate the user reply and bot reply
while True:
    
    
    query = user.takeCommand().lower()
    if 'open' in query:
        if 'browser' in query:
            print("RAMBOT: ",end="")
            print(user.openBrowser())
            user.speak("Opening Browser")
        elif 'calculator' in query:
            print("RAMBOT: ",end="")
            print(user.openCalculator())
            user.speak("Opening Calculator")
        elif 'camera' in query:
            print("RAMBOT: ",end="")
            print(user.openCamera())
            user.speak("Opening Camera")
        elif 'calendar' in query:
            print(user.openCalendar())
            user.speak("Opening Calendar")
        elif 'clock' in query:
            print("RAMBOT: ",end="")
            print(user.openClock())
            user.speak("Opening Clock")
        elif 'control panel' in query:
            print("RAMBOT: ",end="")
            print(user.openControlPanel())
            user.speak("Opening Control Panel")

        elif 'file explorer' in query:
            print("RAMBOT: ",end="")
            print(user.openFileExplorer())
            user.speak("Opening File Explorer")
        elif 'mail' in query:
            print("RAMBOT: ",end="")
            print(user.openMail())
            user.speak("Opening Mail")
        elif 'maps' in query:
            print("RAMBOT: ",end="")
            print(user.openMaps())
            user.speak("Opening Maps")
        elif 'music player' in query:
            print("RAMBOT: ",end="")
            print(user.openMusicPlayer())
            user.speak("Opening Music Player")
        elif 'notepad' in query:
            print("RAMBOT: ",end="")
            print(user.openNotepad())
            user.speak("Opening Notepad")
        elif 'settings' in query:
            print("RAMBOT: ",end="")
            print(user.openSettings())
            user.speak("Opening Settings")
        elif 'store' in query:
            print("RAMBOT: ",end="")
            print(user.openStore())
            user.speak("Opening Store")
        else:
            print("RAMBOT: ",end="")
            print("Sorry, I couldn't find that application.")
            user.speak("Sorry, I couldn't find that application.")
    elif 'weather' in query:
        print("RAMBOT: ",end="")
        print(user.weather())
        user.speak(user.weather())


    elif "exit" in query or "bye" in query or "sleep" in query:
        print("RAMBOT: ",end="")
        print("Goodbye!")
        user.speak("Goodbye!")
        break
    elif 'time' in query:
        print("RAMBOT: ",end="")
        print(user.time())
        user.speak(user.time())
    elif 'search' in query:
        query = query.replace("search", "")
        print("RAMBOT: ",end="")
        print(user.results(query))
        user.speak(user.results(query))
    else:
        print("RAMBOT: ",end="")
        user.bot_normal_reply(query)
        user.speak(user.bot_normal_reply(query))



        