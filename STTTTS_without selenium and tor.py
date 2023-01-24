import openai
import pyttsx3
import speech_recognition as sr
import time
import winsound
from gtts import gTTS
import pygame
import os
import requests
import subprocess
from googletrans import Translator
import json
import wave
from playsound import playsound
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


#chrome_options = Options()
#chrome_options.add_argument('--log-level=3')
#chrome_options.headless = True
#PathofDriver = "Driver\\chromedriver.exe"
#driver = webdriver.Chrome(PathofDriver,options=chrome_options)
#driver.maximize_window()

#Website = f'https://ttsmp3.com/text-to-speech/British%20English/'




current_time = time.strftime("%I:%M:%S")
openai.api_key = "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"
translator = Translator()
engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)


def Speak_ge(Text):
    driver.get(Website)
    ButtonSelection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/form/select'))
    ButtonSelection.select_by_visible_text('German / Vicki')
    print("")
    print(f" AI : {Text}.")
    print("")
    Data = str(Text)
    xpathtec = '/html/body/div[4]/div[2]/form/textarea'
    driver.find_element(by=By.XPATH, value=xpathtec).send_keys(Data)
    driver.find_element(by=By.XPATH, value='//*[@id="vorlesenbutton"]').click()
    driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/form/textarea').clear()
    #sleep(2)
    


def start_program(program_name):
  os.system("start " + program_name)
  print("Das Programm wurde gestartet.")


def stop_program(program_name):
  os.system("taskkill /im " + program_name + " /f")
  print("Das Programm wurde beendet.")



def armode():
    while True:
        conversation = ""
        user_name = "Mohamad"
        bot_name = "ليلى"
        with mic as source:
            print("\n" + current_time + " تكلم مع الذكاء الاصطناعي...")
            r.adjust_for_ambient_noise(source, duration=0.2 )
            audio = r.listen(source, phrase_time_limit=5)
        print("....\n")
        try:
            user_input = r.recognize_google(audio, language= "ar-XA-Wavenet-C")
            print(" : " + user_input)
        except Exception as e :
            continue
        if user_input == "توقف":
            winsound.Beep(frequency=500, duration=500)
            break
        elif user_input == "غير اللغه الى الانجليزيه":
            aimode()
        elif user_input == "غير اللغه الالمانيه":
            kimode()  
        else:
            

            prompt = user_name + ": " + user_input + "\n" + bot_name+ ": "
            conversation += prompt
            response = openai.Completion.create( model="text-davinci-003",prompt=conversation,temperature=0.9,max_tokens=300,top_p=1,frequency_penalty=0.0,presence_penalty=0.6)
            response_str = response["choices"][0]["text"].replace("\n", "")
            response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]
            conversation += response_str + "\n"
            print("KI: " + response_str)
            myobj = gTTS(text=response_str, lang='ar', slow=False)
            myobj.save("ar.mp3")
            pygame.mixer.init()
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.load("ar.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
            pygame.mixer.music.stop()
            pygame.quit()


























def kimode():
    while True:
        conversation= "" 
        user_name = "Mohamad"
        bot_name = "Layla"
        with mic as source:
            winsound.Beep(frequency=1000, duration=100)
            print("\n" + current_time + " KI Wartt auf Frage...")
            r.adjust_for_ambient_noise(source, duration=0.2 )
            audio = r.listen(source, phrase_time_limit=5)
        print("....\n")
        try:
            user_input = r.recognize_google(audio, language= "de")
            print(" : " + user_input)
        except Exception as e :
            continue
        if user_input == "ausschalten":
            winsound.Beep(frequency=500, duration=500)
            break
        elif user_input == "wechsle zu Englisch":
            aimode()
        elif user_input == "wechsle zu Arabisch":
            armode()
        else:
            

            prompt = user_name + ": " + user_input + "\n" + bot_name+ ": "
            conversation += prompt
            response = openai.Completion.create( model="text-davinci-003",prompt=conversation,temperature=0.5,max_tokens=300,top_p=1,frequency_penalty=0.0,presence_penalty=0.6)
            response_str = response["choices"][0]["text"].replace("\n", "")
            response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]
            with open('conversation.txt', 'a', encoding='utf-8') as file:
                file.write(prompt + response_str + "."  + "\n")
            
            print("KI: " + response_str)
            #Speak_ge(response_str)
            engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0")
            engine.say(response_str)
            engine.runAndWait()




def aimode():
    engine.setProperty('voice', "com.apple.speech.synthesis.voice.alex")
            
    engine.say("Ich höre")
    while True:
        
        conversation = ""
        user_name = "Mohamad"
        bot_name = "Habibi"
        with mic as source:
            print("\n" + current_time + " AI listening...")
            r.adjust_for_ambient_noise(source, duration=0.2 )
            audio = r.listen(source)
        print("....\n")
        try:
            user_input = r.recognize_google(audio, language= "en")
            print(" : " + user_input)
        except Exception as e :
            continue
        
        if user_input == "turn off":
            winsound.Beep(frequency=500, duration=500)
            break
        elif user_input == "switch to German":
            kimode()
        elif user_input == "switch to Arabic":
            armode()
        else:

            prompt = user_name + ": " + user_input + "\n" + bot_name+ ": "
            conversation += prompt
            response = openai.Completion.create( model="text-davinci-003",prompt=conversation,temperature=0.9,max_tokens=300,top_p=1,frequency_penalty=0.0,presence_penalty=0.6)
            response_str = response["choices"][0]["text"].replace("\n", "")
            response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]

            conversation += response_str + "\n"
            print("AI: " + response_str)
            engine.say(response_str)
            engine.runAndWait()
            
def sd():
    os.system("shutdown /s /t 1")




#pygame.mixer.init()
#pygame.mixer.music.load("Startup_Sound.mp3")
#pygame.mixer.music.play()
#while pygame.mixer.music.get_busy():
#    continue
#pygame.mixer.music.stop()
#pygame.quit()
while True:
    try:
        response = requests.get("https://www.google.com")
        if response.status_code == 200:
            print("*")
        else:
            print("Internet connection is not working.")
    except requests.ConnectionError:
        print("Internet connection is not working.")
    with mic as source:
        print("\n" + current_time + " Warten auf Ruf ...")
        r.adjust_for_ambient_noise(source, duration=0.2 )
        audio = r.listen(source)

    print("....\n")


    try:
        user_input = r.recognize_google(audio, language= "en")
        print("user input : " + user_input)

    except Exception as e :
        print(e)
        continue

    if user_input == "German":
        winsound.Beep(frequency=1000, duration=100)
        kimode()
        
    elif user_input == "English" :
        winsound.Beep(frequency=1000, duration=100)
        winsound.Beep(frequency=1000, duration=100)
        aimode()
    elif user_input == "Arabic" :
        winsound.Beep(frequency=1000, duration=100)
        winsound.Beep(frequency=1000, duration=10)
        winsound.Beep(frequency=500, duration=1050)
        armode()
        
    elif "open" in user_input:
      program_name = user_input.split("open")[-1]
      start_program(program_name)


    elif "close" in user_input:
      program_name = user_input.split("close")[-1]
      stop_program(program_name)

    elif user_input == "sleep" :
        winsound.Beep(frequency=500, duration=500)
        winsound.Beep(frequency=500, duration=500)
        break
    elif user_input == "shut down now" :
        pygame.mixer.init()
        pygame.mixer.music.load("Shutdown_Sound.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.mixer.music.stop()
        pygame.quit()
        sd()
    
        
    
    else:
        continue
