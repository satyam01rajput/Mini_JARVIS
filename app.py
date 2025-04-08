from flask import Flask, render_template
import speech_recognition as sr
import pyttsx3
import os
import threading

app = Flask(__name__)

# Thread-safe speak function
def speak(text):
    print("Shifra:", text)
    local_engine = pyttsx3.init()
    local_engine.setProperty('rate', 150)
    local_engine.say(text)
    local_engine.runAndWait()

# Listening and command execution
def listen_and_execute():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening now...")
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language='en-in')
        command = command.lower()
        print(f"You said: {command}")

        if "calculator" in command:
            speak("Opening calculator.")
            os.system("calc")

        elif "notepad" in command:
            speak("Opening notepad.")
            os.system("notepad")

        elif "chrome" in command:
            speak("Opening Chrome.")
            os.system("start chrome")

        elif "youtube" in command:
            speak("Opening YouTube.")
            os.system("start https://youtube.com")

        elif "file manager" in command or "this pc" in command:
            speak("Opening File Manager.")
            os.system("explorer")

        elif "drive c" in command:
            speak("Opening Local Disk C.")
            os.system("start C:\\")

        elif "drive d" in command:
            speak("Opening Local Disk D.")
            os.system("start D:\\")

        elif "settings" in command:
            speak("Opening Settings.")
            os.system("start ms-settings:")

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            return

        else:
            speak("Searching on Google.")
            os.system(f"start https://www.google.com/search?q={command}")

    except Exception as e:
        speak("Sorry, I didn't catch that.")
        print("Error:", e)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/listen', methods=['POST'])
def listen():
    threading.Thread(target=listen_and_execute).start()
    return "Listening..."

# Main entry
if __name__ == '__main__':
    app.run(debug=True)
