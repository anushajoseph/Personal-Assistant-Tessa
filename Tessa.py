import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

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


def run_tessa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'what is the time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
    elif 'what is the date' in command:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        print('Current date is ' + date)
        talk('Current date is ' + date)
    else:
        talk('Please say the command again')


while True:
    try:
        run_tessa()
    except UnboundLocalError:
        print("No command detected! Tessa has stopped working ")
        exit()
