from gtts import *                    # importing gtts(Google Text To Speech)
import os                             # Importing the os built-in module for accessing the terminal

while True:                           # A 'while True' statement to allow multiple inputs

    inp = input("What shall i say: ") # Asking the user what they want the computer to say

    tts = gTTS(text=inp, lang="en")   # Setting the text(that had been inputed) and language
    tts.save("audio.mp3")             # Saving the text to an .mp3 file named audio
    os.system("open audio.mp3")       # Automatically opening the audio.mp3 file(works with Mac,not sure abou
                                      # Windows and Linux just change it to the working terminal command
