import speech_recognition as sr
import pyttsx3
from datetime import datetime
import os
import requests
import json

def get_temperature():
    url = "https://api.tomorrow.io/v4/timelines"
    querystring = {
        "location": "LATITUDE AQUI, LONGITUDE AQUI",
        "fields":["temperature", "cloudCover"],
        "units":"metric",
        "timesteps":"1d",
        "apikey":"sua chave"}
    try:
        response = requests.request("GET", url, params=querystring)

        if response.status_code == 200:
            print(response.json)
            t = response.json()['data']['timelines'][0]['intervals'][0]['values']['temperature']
            speak(f"A temperatura é {t}C")
            return response.json()
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ouvindo")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Analisando")
        query = r.recognize_google(audio, language ='pt-br')
        speak("Você disse: " + query)

    except Exception as e:
        print(e)
        speak("Não entendi")
        return "None"
    return query


while True:
    command = takeCommand()

    print(command)
    if 'hora' in command:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        speak("Agora é " + current_time)
    if 'temperatura' in command:
        get_temperature()
    if 'fechar' in command:
        exit()