# import external libraries

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests

# speech recognition & pyttsx3 (python text to speech version 3)

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
print('Hey I am Tessa\nHow can I help you?')
engine.say('Hey I am Tessa')
engine.say('How can I help you?')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening ......')
            talk("listening now")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        pass
    return command


def run_tessa():
    command = take_command()
    if 'hi' in command or 'hello' in command:
        print("What can I do for you?")
        talk("What can I do for you?")

    # pywhatkit
    # youtube and google search

    elif 'play' in command:
        song = command.replace('play', '')
        print('playing' + song)
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'search' in command:
        term = command.replace('search', '')
        print('searching' + term)
        talk('searching' + term)
        pywhatkit.search(term)

    # date-time

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
    elif 'date' in command:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        print('Today is ' + date)
        talk('Today is ' + date)

    # wikipedia

    elif 'wikipedia' in command:
        topic = command.replace('wikipedia', '')
        info = wikipedia.summary(topic, 2)
        print(info)
        talk(info)

    # pyjokes

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    # weather

    elif 'current weather in ' in command:
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=62b743472ce5e32f9fb2a3b2b63856c8&q='
        city = command.replace('current weather in ', '')
        url = api_address + city
        json_data = requests.get(url).json()
        weather = json_data['weather'][0]['description']
        temp_k = json_data['main']['temp']
        temp_c = int(temp_k - 273.15)
        print(str(temp_c) + '°C, with ' + weather)
        talk(str(temp_c) + 'degree celsius, with ' + weather)

    # about me

    elif 'who are you' in command or 'what can you do' in command:
        talk('I am Tessa your personal assistant. I am programmed to perform minor tasks like,'
             ' play songs in youtube, search in google chrome, tell date and time, search in wikipedia, '
             'tell current weather in different places and you can ask me to tell a joke too')

    # creators

    elif 'who made you' in command or 'who created you' in command or 'who discovered you' in command:
        print("I was built by Anusha, Sandra and Sneha.")
        talk("I was built by Anusha, Sandra and Sneha.")

    elif 'bye' in command:
        print("Thank you.\nAssistance accomplished!\nHuzzah!")
        talk("Thank you. Assistance accomplished. Huzzah")
        exit()

    else:
        print("Please say the command again!")
        talk("Please say the command again")


while True:
    try:
        run_tessa()
    except UnboundLocalError:
        print("No command detected!\nTessa has stopped working!")
        talk("No command detected. Tessa has stopped working")
        exit()
