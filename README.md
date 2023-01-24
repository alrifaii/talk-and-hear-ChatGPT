#Talk-and-Hear-ChatGPT

#####This Programm is able to recognize your Speech and answear with a natural Voice.
----
This code uses the Selenium web driver and the OpenAI API to create a text-to-speech program that allows a user to ask a question using their voice and receive an answer from the OpenAI API in speech.

####Selenium
The Selenium web driver is used to control a Chrome browser that opens a specific website and interacts with the website's elements. The Chrome browser is also set to run in headless mode and uses a proxy server.

####OpenAI API
The OpenAI API is used to generate the response to the user's question. The code also uses the SpeechRecognition library to recognize the user's voice and the Winsound library to make a beep sound when it's listening.


The code also includes a function called "Sprachmodus" that begins the voice recognition process and continues to listen for user input until the program is closed. This function also writes the conversation to a file called conversation.txt and timestamps each line.

##There are TWO Ways:

###STTTTSv2.py

This Code is using a proxy server to change the IP address when interacting with the ttsmp3.com website. This is done to bypass any usage limitations that the website may have in place.

ttsmp3.com is a website that provides text-to-speech conversion services. It allows users to convert written text into spoken words by using artificial voices. It provides users the ability to convert any written text into spoken words with natural sounding voices. This can be useful for creating audio versions of written content, such as e-books, articles, and more. They also provide the ability to change the voice gender and language, allowing users to convert text into speech in multiple languages.

However there is a limitation of 3000 Words/day. This could be enough for some useres, so you have to start a Tor Proxy befor you start the Programm. If you reatch the limitation just start Torkill.py and start TorProxy.py again.

As the website's terms of service do not prohibit the use of Tor proxy, it is likely to be legal. However, there is also an alternative version available:

###STTTTS_without selenium and tor.py

This Code have the same function as STTTTSv2.py, however it uses instate of the ttsmp3 the computer's built-in text-to-speech system.
