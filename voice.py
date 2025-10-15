import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import time
import datetime as dt
import pywhatkit as pk

# Initialize pygame mixer
pygame.mixer.init()

listener = sr.Recognizer()
va_name = "venkat"

# Speak function (Telugu voice output) - FIXED
def speak(cmd):
    try:
        filename = f"audio_{int(time.time())}.mp3"
        tts = gTTS(cmd, lang='te')
        tts.save(filename)
        
        # Use pygame instead of playsound
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        
        # Wait for playback to finish
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
            
    except Exception as e:
        print(f"Audio error: {e}")
    finally:
        # Clean up
        try:
            pygame.mixer.music.stop()
            if os.path.exists(filename):
                os.remove(filename)
        except:
            pass

# Take voice command - YOUR ORIGINAL CODE
def take_cmd(check):
    command = ""
    try:
        with sr.Microphone() as source:
            # Improved ambient noise adjustment and listening
            listener.adjust_for_ambient_noise(source, duration=1.0)
            print("Listening...")
            audio = listener.listen(source, timeout=10, phrase_time_limit=8)  # Increased timeout
            if check:
                command = listener.recognize_google(audio, language="te").lower()
                if va_name in command:
                    command = command.replace(va_name, "").strip()
            else:
                command = listener.recognize_google(audio, language="en-US").lower()
    except sr.WaitTimeoutError:
        print("No speech detected. Please try again...")
    except sr.UnknownValueError:
        print("Could not understand audio. Please repeat...")
    except Exception as e:
        print(f"Check your mic or input: {e}")
    return command

# Greeting message
speak(f"Hello, how can I help you, {va_name}")

# Main loop - YOUR ORIGINAL CODE
while True:
    final_cmd = take_cmd(True)
    print(f"DEBUG: Heard this after removing '{va_name}': '{final_cmd}'")  # Debug line added
    if final_cmd == "":
        continue

    # Stop command - FIXED WITH ALL TELUGU VARIATIONS
    if "stop" in final_cmd or "exit" in final_cmd or "ఎగ్జిట్" in final_cmd or "స్టాప్" in final_cmd:
        speak("Stopping the assistant. Goodbye!")
        break

    # Tell time - FIXED WITH TELUGU VARIATIONS
    if "time" in final_cmd or "టైం" in final_cmd or "టైమా" in final_cmd:
        current_time = dt.datetime.now().strftime("%I:%M %p")
        speak(current_time)

    # Play YouTube video - FIXED WITH TELUGU VARIATIONS
    elif "youtube" in final_cmd or "google" in final_cmd:
        speak("Mahesh hit songs")
        video_cmd = take_cmd(False)
        if video_cmd:
            pk.playonyt(video_cmd)
            speak("Enjoy. Call again if you need to.")
        break

    # Google search - FIXED WITH TELUGU VARIATIONS
    elif "google" in final_cmd:
        speak("Search with SQL")
        search_cmd = take_cmd(False)
        if search_cmd:
            pk.search(search_cmd)