import speech_recognition as sr
import winsound
import pyglet
import webbrowser
from playsound import playsound
from gtts import gTTS # google text to speech
import random
from time import ctime
import time
import os

# Creating a user class
class user:
    name = ''
    def setName(self, name):
        self.name = name

# A methods that looks up a specific word in an array of words
def word_exists(terms, audio_data):
    for term in terms:
        if term in audio_data:
            return True

# Intializing the recognizer
recognizer = sr.Recognizer()

# Convert audio into text format
def convert_audio():
    with sr.Microphone() as audio_input:
        print("Say something")
        audio = recognizer.listen(audio_input)
        voice_data = ''
        try:
            voice_data = recognizer.recognize_google(audio) # converting audio to text
        except sr.UnknownValueError:
            say('Sorry, I did not understand that')
        except sr.RequestError:
            say('Sorry, the service is unavailable at the moment')
        #print(f"{voice_data.lower()}") # printing what the user has said
        return voice_data.lower()

# convert a string into an audio
def say(audio_string):
    text_to_speech = gTTS(text=audio_string, lang='en')
    random_number = random.randint(1,5000000)
    audio_file = 'audio' + str(random_number) + '.mp3' # creating an mp3 file for the audio file
    text_to_speech.save(audio_file)
    playsound(audio_file)
    print(f"Khadra: {audio_string}")
    os.remove(audio_file)

# recognizing audio
def respond(sound_text):
    # greeting
    if word_exists(['hey', 'hi', 'hello'], sound_text):
        greetings = [f"hey, how can I help you? {user_object.name}", f"hey, what's up? {user_object.name}", f"hey, what is going on? {user_object.name}", f"hello {user_object.name}"]
        greeting = greetings[random.randint(0, len(greetings)-1)]
        say(greeting)

    # name
    if word_exists(['what is your name', 'tell me your name', 'who are you'], sound_text):
        if user_object.name:
            say("my name is Khadra")
        else:
            say("my name is Khadra, what is your name?")
    
    if word_exists(['my name is'], sound_text):
        user_name = sound_text.split("is")[-1].strip()
        say(f"okay, I will remember that {user_name}")
        user_object.setName(user_name)

    if word_exists(['how are you', 'how are you doing'], sound_text):
        say(f"I am doing good, thanks for asking {user_object.name}")

    # tell the time
    if word_exists(['what is the time', 'tell me the time', 'what time is it'], sound_text):
        time = ctime().split(" ")[3].split(":")
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f"{hours} {minutes}"
        say(time)

    # search google
    if word_exists(['search for'], sound_text):
        search_item = sound_text.split("for")[-1]
        url = f"https://google.com/search?q={search_item}"
        webbrowser.get().open(url)
        say(f"Here is what I found for {search_item} on google")

    if word_exists(['exit', 'quit', 'goodby'], sound_text):
        say(f"see you next time {user_object.name}")
        exit()
        

time.sleep(1)    

user_object = user()

def main():
    while(1):
        sound_text = convert_audio()
        respond(sound_text)
if __name__ == "__main__":
    main()