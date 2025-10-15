import speech_recognition as sr

listener = sr.Recognizer()

print("=== Microphone Test Script ===")

# Step 1: List all available microphones
print("\nAvailable Microphones:")
for i, mic_name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{i}: {mic_name}")

# Step 2: Try to use the default microphone
try:
    with sr.Microphone() as source:
        print("\nDefault microphone dpython mic_test.pyetected.")
        print("Adjusting for ambient noise, please wait...")
        listener.adjust_for_ambient_noise(source, duration=2)
        print("Now, please say something:")
        audio = listener.listen(source, timeout=5)
        text = listener.recognize_google(audio)
        print("✅ You said:", text)
except sr.WaitTimeoutError:
    print("❌ No speech detected. Try speaking clearly within 5 seconds.")
except OSError as e:
    print("❌ Mic error:", e)
    print("Make sure your microphone is connected and set as default input.")
except Exception as e:
    print("❌ Unexpected error:", e)

print("\nTest Complete!")
