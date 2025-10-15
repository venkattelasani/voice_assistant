# Voice Assistant 🤖

A Python-based voice assistant with Telugu language support.

## Features 🎯
- Telugu voice recognition with wake word "venkat"
- English voice commands for YouTube and Google
- Text-to-speech in Telugu
- YouTube video playback
- Google search
- Time telling

## Commands 🗣️
- **"venkat time"** - Get current time
- **"venkat youtube"** - Play YouTube videos
- **"venkat google"** - Search on Google  
- **"venkat stop"** - Exit assistant
Libraries:
pip install speechrecognition  # Voice recognition
pip install pygame            # Audio playback
pip install gtts             # Text-to-speech
pip install pywhatkit        # YouTube & Google integration
pip install pyaudio          # Microphone access
If pyaudio gives errors, use this instead:
pip install pipwin
pipwin install pyaudio



| Library             | Purpose                                 |
| ------------------- | --------------------------------------- |
| `SpeechRecognition` | Convert microphone speech to text       |
| `gTTS`              | Convert text to Telugu voice (`.mp3`)   |
| `pygame`            | Play `.mp3` reliably on Windows         |
| `pywhatkit`         | YouTube search and Google search        |
| `PyAudio`           | Microphone input for speech recognition |
