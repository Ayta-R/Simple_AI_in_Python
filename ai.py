import speech_recognition as sr
import os
import sys
import webbrowser


def talk(words):
    print(words)
    os.system('say ' + words)


talk('Hi, ask me something')


def command():
    r = sr.Recognizer()

    with sr.Microphone() as sourse:
        print('Speak')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(sourse, duration=1)
        audio = r.listen(sourse)

    try:
        task = r.recognize_google(audio, language='ru-RU').lower()
        print('You said:' + task)
    except sr.UnknownValueError:
        talk('I didn\'t understand you, try to say it again')
        task = command()

    return task


def makeSometing(task):
    if 'open websitre' in task:
        talk('I\'m already opening it')
        url = 'http://www.google.com'
        webbrowser.open(url)
    elif 'name' in task:
        talk('My name is Marusya')
        sys.exit()
    elif 'stop' in task:
        talk('Ok')
        sys.exit()



while True:
    makeSometing(command())
