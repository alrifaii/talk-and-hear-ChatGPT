# Talk-and-Hear-ChatGPT
This Programm is able to recognize your Speech and answear with a natural Voice.

This code uses the Selenium web driver and the OpenAI API to create a text-to-speech program that allows a user to ask a question using their voice and receive an answer from the OpenAI API in speech.

The Selenium web driver is used to control a Chrome browser that opens a specific website and interacts with the website's elements. The Chrome browser is also set to run in headless mode and uses a proxy server.

The OpenAI API is used to generate the response to the user's question. The code also uses the SpeechRecognition library to recognize the user's voice and the Winsound library to make a beep sound when it's listening.

The code also includes a function called "Sprachmodus" that begins the voice recognition process and continues to listen for user input until the program is closed. This function also writes the conversation to a file called conversation.txt and timestamps each line.
