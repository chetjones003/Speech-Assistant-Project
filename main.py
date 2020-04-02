from gtts import gTTS
import os
import playsound
import random
import speech_recognition as sr
import time
from time import ctime
import webbrowser

# initialize a recognizer
r = sr.Recognizer()

# listen for audio and convert it to text


def record_audio(ask=False):
    # Microphone as source
    with sr.Microphone() as source:
        if ask:
            assistant_speak(ask)
        # listen for the audio from source
        audio = r.listen(source)
        voice_data = ''
        try:
            # covert audio to tex
            voice_data = r.recognize_google(audio)
        # recognizer doesn't understand what was said
        except sr.UnknownValueError:
            assistant_speak('Sorry, I did not get that.')
        # recognizer is not connected
        except sr.RequestError:
            assistant_speak('My speech service is down at the moment.')
        return voice_data


# get string and make a audio file to be played
def assistant_speak(audio_string):
    # text to speech voice
    tts = gTTS(text=audio_string, lang='en')
    random_int = random.randint(1, 10000000)
    audio_file = 'audio-' + str(random_int) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


# reponses to user input
def respond(voice_data):
    # Name
    if 'what is your name' in voice_data:
        assistant_speak('My name is Assistant')

    # Time
    if 'what time is it' in voice_data:
        assistant_speak(ctime())

    # Google Search
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        assistant_speak('Here is what I found for the search of' + search)

    # Google Location
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/map/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        assistant_speak('Here is what I found for the search of' + location)

    # Exit
    if 'exit' in voice_data:
        exit()


time.sleep(1)
assistant_speak('How can I help you')
while 1:
    voice_data = record_audio()
    resond(voice_data)
