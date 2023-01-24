#selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
#speak
import openai
import os
import speech_recognition as sr
import winsound
from datetime import datetime




chrome_options = Options()
chrome_options.add_argument('--proxy-server=socks5://127.0.0.1:9050')
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
driver = webdriver.Chrome("Driver\\chromedriver.exe",options=chrome_options)
driver.maximize_window()
openai.api_key = "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"
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)

user_name = "Mohamad"
bot_name = "Layla"

        
def Speak(Text, Voice):
    
    ButtonSelection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/form/select'))
    ButtonSelection.select_by_visible_text(Voice)
    words = Text.split()
    num_words = len(words)
    print ("num_words: " + str(num_words))
    duration = (num_words / 100)*60  
    print(f"Duration of text-to-speech output: {duration:.2f} sec")
    xpathtec = '/html/body/div[4]/div[2]/form/textarea'
    driver.find_element(by=By.XPATH, value=xpathtec).send_keys(Text)
    driver.find_element(by=By.XPATH, value='//*[@id="vorlesenbutton"]').click()
    driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/form/textarea').clear()
    time.sleep(duration)
    #driver.close()
    print("..finish..")
def askai(frage):
    conversation= "" 
    prompt = user_name + ": " + frage + "\n" + bot_name+ ": "
    conversation += prompt
    response = openai.Completion.create( model="text-davinci-003",prompt=conversation,temperature=0.8,max_tokens=300,top_p=1,frequency_penalty=0.0,presence_penalty=0.6)
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]
    with open('conversation.txt', 'a', encoding='utf-8') as file:
        file.write(prompt + response_str + "."  + "\n")
    print("KI: " + response_str)
    Speak(response_str, 'German / Vicki') 
def Sprachmodus():
    Speak("Sprachmodus an", 'German / Vicki')
    i = 0
    while True:
        winsound.Beep(frequency=500, duration=100)
        with mic as source:
            print("\n" + datetime.now().strftime("%d-%m-%Y %H:%M:%S") + " KI Wartt auf Frage...")
            r.adjust_for_ambient_noise(source, duration=0.2 )
            audio = r.listen(source, phrase_time_limit=5)
        print("....\n")
        try:
            user_input = r.recognize_google(audio, language= "de")
            print(" : " + user_input)
            i = 0
        except Exception as e :
            i = i + 1
            print ("nichts empfangen " + str(i))
            if i == 10:
                Speak("Sprachmodus, aus", 'German / Vicki')
                break
            continue
        if user_input == "Sprachmodus aus":
            winsound.Beep(frequency=500, duration=500)
            Speak("Sprachmodus, aus", 'German / Vicki')
            break
        askai(user_input)




def start_program(program_name):
  os.system("start " + program_name)
  print("Das Programm wurde gestartet.")
def stop_program(program_name):
  os.system("taskkill /im " + program_name + " /f")
  print("Das Programm wurde beendet.")

def sd():
    os.system("shutdown /s /t 1")

driver.get(f'https://ttsmp3.com/text-to-speech/British%20English/')
print("selenium eingehäckt")

while True:
    conversation= "" 
    user_name = "Mohamad"
    bot_name = "Layla"
    with mic as source:
        winsound.Beep(frequency=500, duration=10) # neuer version LED
        print("\n" + datetime.now().strftime("%d-%m-%Y %H:%M:%S") + " KI Wartt auf Frage...")
        r.adjust_for_ambient_noise(source, duration=0.2 )
        audio = r.listen(source, phrase_time_limit=5)
    print("....\n")
    try:
        user_input = r.recognize_google(audio, language= "de")
        print(" : " + user_input)
    except Exception as e :
        continue
    if "Leila" in user_input:
        askai(user_input)

        
    elif "open" in user_input:
      program_name = user_input.split("open")[-1]
      start_program(program_name)


    elif "close" in user_input:
      program_name = user_input.split("close")[-1]
      stop_program(program_name)
      
    elif "Sprachmodus" in user_input:
      Sprachmodus()

    

    elif user_input == "Schlaf" :
        winsound.Beep(frequency=500, duration=500)
        winsound.Beep(frequency=500, duration=500)
        driver.close()
        break
    elif user_input == "herunterfahren" :
        sd()

    else:
        continue