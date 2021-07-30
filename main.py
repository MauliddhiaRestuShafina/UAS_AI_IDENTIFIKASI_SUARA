import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Silahkan Masukkan Suara anda...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        command = "please try again later"
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'project' in command:
        url = 'https://id.wikipedia.org/wiki/Jasa_boga'
        webbrowser.open(url)
        talk('Done!')
    elif 'are you single' in command:
        talk('Yaa, saya tidak berpacaran dengan mu')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'introduce yourself' in command:
        talk("Okay,Let me start by The time I was born,,")
        talk("I was a dream of a boy dreaming to make a perfect virtual assistant")
        talk("He soon established the company named ROGER industries")
        talk("Slowly,I came to life")
        talk("I started learning various things like calculations,General knowldge etc etc")
        talk("Now I am capable of doing various things like Beatboxing,opening applications,Cracking jokes,Playing music etc.")
        talk("Okay,thats a wrap I wont say more ")
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
