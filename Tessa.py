
#import external libraries

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests



#speech recognition & pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say('Hey I am Tessa')
engine.say('How can I help you')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening ......')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Tessa' in command:
                command = command.replace('Tessa', '')
                print(command)
    except:
        pass
    return command

#pywhatkit

def run_tessa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        print('playing' + song)
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'search' in command:
        term = command.replace('search', '')
        print('searching' + term)
        talk('searching' + term)
        pywhatkit.search(term)

#date-time

    elif 'what is the time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
    elif 'what is the date' in command:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        print('Today is ' + date)
        talk('Today is ' + date)

#wikipedia

    elif 'wiki ' in command:
        topic = command.replace('wiki ', '')
        info = wikipedia.summary(topic, 2)
        print(info)
        talk(info)

#pyjokes

    elif 'tell me a joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

#weather

    elif 'current weather in ' in command:
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=62b743472ce5e32f9fb2a3b2b63856c8&q='
        city = command.replace('current weather in ', '')
        url = api_address + city
        json_data = requests.get(url).json()
        weather = json_data['weather'][0]['description']
        temp_k = json_data['main']['temp']
        temp_c = int(temp_k - 273.15)
        talk(temp_c)
        talk('degree celsius , with')
        talk(weather)

    else:
        talk('Please say the command again')


while True:
    try:
        run_tessa()
    except UnboundLocalError:
        print("No command detected!\nTessa has stopped working ")
        exit()
