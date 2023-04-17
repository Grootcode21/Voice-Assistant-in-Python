# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:28:27 2022

GROOTBOT

@author: ALIENWARE
"""
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import os
import yfinance as yf
import pyjokes
import wikipedia


# listen to microphone & return audio as text using google
def transform():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        said = r.listen(source)
        try:
            print('I am listening')
            q = r.recognize_google(said, language= "en")
            return q
        except sr.UnknownValueError():
            print("Sorry I did not understand")
            return " I am waiting"
        except sr.RequestError(): 
            print('Sorry the service is down')
            return " I am waiting"
        except:
            return "I am waiting"
    

transform()
  

def speaking(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

import pywintypes
import pythoncom

# speaking('hello world')
speaking("Hello World") 

engine = pyttsx3.init()
for voice in engine.getProperty('voices'):
    print(voice)
     
id = ''
engine.setProperty('voice', id)
engine.say('Buen dia.como estas')
engine.runAndWait()       


#return weekday name
def query_day():
    day = datetime.date.today()
    #print(day)
    weekday = day.weekday()
    print(weekday)
    mapping = {
        0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'
        }
    try:
        speaking(f'Today is {mapping[weekday]}')
    except:
        pass

query_day()

#returns the time
def query_time():
    #time = datetime.datetime.now()
    #print(time)
    time = datetime.datetime.now().strftime("%I:%M:%S")
    #speaking(time[1])
    #speaking(f'{time[0:2]} o'clock and {time[3:5]} minutes')
    speaking(time)
    

query_time()


#Intro greeting at startup
def whatsup():
    speaking('''Hi, my name is Groot. I am your personal assistant.
             How may I help you?
             ''')


whatsup()


# heart of our VA. Take queries and returns answers
def querying():
    whatsup()
    start =  True
    while(start):
        q = transform().lower()
        
        if 'start youtube' in q:
            speaking('starting youtube. Just a sec.')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'start webbrowser' in q:
            speaking('opening browser')
            webbrowser.open('https://www.google.com')
            continue
        elif 'What day is it?' in q:
            query_day()
            continue
        elif 'what time is it?' in q:
            query_time()
            continue
        elif 'shut down' in q:
            speaking('I am shutting down')
            break
        elif 'from wikipedia' in q:
            speaking('Checking wikipedia')
            q = q.replace('wikipedia', "")
            result = wikipedia.summary(q, sentences=2)
            speaking('found on wikipedia')
            speaking(result)
            
        elif 'your name' in q:
            speaking('I am Groot. Your Voice Assistant')
            
        elif 'search web' in q:
            pywhatkit.search(q)
            speaking('that is what I found')
            continue
        elif 'play' in q:
            speaking(f'playing {q}')
            pywhatkit.playonyt(q)
            continue
        elif 'joke' in q:
            speaking(pyjokes.get_joke())
            continue
        elif 'stock price' in q:
            search = q.split("of")[-1].strip()
            lookup = {'apple': 'AAPL',
                      'amazon':'AMZN',
                      'google':'GOOGL'}
            try:
                stock = lookup[search]
                stock = yf.Ticker(stock)
                currentprice = stock.info["regularMarketPrice"]
                speaking(f'found it, the price for {search} is {currentprice}')
                continue
            except:
                speaking(f'sorry I have no data for {search}')
                continue
            
                    
        
        
querying()

