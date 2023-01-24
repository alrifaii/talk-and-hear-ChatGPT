# Talk-and-Hear-ChatGPT

This Programm is able to recognize your Speech and answers with a natural Voice.
----
It utilizes the Selenium web driver and OpenAI API to create a text-to-speech program that allows the user to ask a question using their voice and receive an answer from the OpenAI API in speech. Selenium is used to control a Chrome browser that opens a specific website and interacts with the website's elements. The Chrome browser is set to run in headless mode and uses a proxy server. The OpenAI API is used to generate the response to the user's question. The code also uses the SpeechRecognition library to recognize the user's voice and the Winsound library to make a beep sound when it's listening.

#### Selenium
The Selenium web driver is used to control a Chrome browser that opens a specific website and interacts with the website's elements. The Chrome browser is also set to run in headless mode and uses a proxy server.

#### OpenAI API
The OpenAI API is used to generate the response to the user's question. The code also uses the SpeechRecognition library to recognize the user's voice and the Winsound library to make a beep sound when it's listening.


The code also includes a function called "Sprachmodus" that begins the voice recognition process and continues to listen for user input until the program is closed. This function also writes the conversation to a file called conversation.txt and timestamps each line.

## There are TWO Ways:

### STTTTSv2.py

This code uses a proxy server to change the IP address when interacting with the ttsmp3.com website. This is done to bypass any usage limitations that the website may have in place. The website, ttsmp3.com, provides text-to-speech conversion services and allows users to convert written text into spoken words by using artificial voices. However, there is a limitation of 3000 words per day. If this limit is reached, you can start TorProxy.py. As the website's terms of service do not prohibit the use of Tor proxy, it is likely to be legal.

### STTTTS_without selenium and tor.py

This code has the same function as STTTTSv2.py, however, it uses the computer's built-in text-to-speech system instead of ttsmp3.com. It doesn't require to use a proxy or the selenium web driver
