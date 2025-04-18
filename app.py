from flask import Flask, render_template
import speech_recognition as sr
import pyttsx3
import os
import threading

app = Flask(__name__)

# Thread-safe speak function
def speak(text):
    print("Jarvis:", text)
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

        # 🗂 Folder shortcuts
        folder_paths = {
            "movies": "D:\\Movies",
            "downloads": "C:\\Users\\Satyam Rajput\\Downloads",
            "documents": "C:\\Users\\Satyam Rajput\\Documents",
            "pictures": "C:\\Users\\Satyam Rajput\\Pictures",
            "music": "C:\\Users\\Satyam Rajput\\Music",
            "desktop": "C:\\Users\\Satyam Rajput\\Desktop"
        }

        for folder_name, path in folder_paths.items():
            if folder_name in command:
                speak(f"Opening {folder_name} folder.")
                os.system(f'start "" "{path}"')
                return

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

        elif "camera" in command:
            speak("Opening Camera.")
            os.system("start microsoft.windows.camera:")

        elif "command prompt" in command or "cmd" in command:
            speak("Opening Command Prompt.")
            os.system("start cmd")

        elif "powershell" in command:
            speak("Opening PowerShell.")
            os.system("start powershell")

        elif "control panel" in command:
            speak("Opening Control Panel.")
            os.system("control")

        elif "task manager" in command:
            speak("Opening Task Manager.")
            os.system("taskmgr")

        elif "paint" in command:
            speak("Opening Paint.")
            os.system("mspaint")

        elif "word" in command:
            speak("Opening Microsoft Word.")
            os.system("start winword")

        elif "excel" in command:
            speak("Opening Microsoft Excel.")
            os.system("start excel")

        elif "powerpoint" in command:
            speak("Opening Microsoft PowerPoint.")
            os.system("start powerpnt")

        elif "whatsapp" in command:
            speak("Opening WhatsApp.")
            os.system("start whatsapp")

        elif "music" in command:
            speak("Opening Music.")
            os.system("start mswindowsmusic:")

        elif "photos" in command:
            speak("Opening Photos.")
            os.system("start ms-photos:")

        elif "restart" in command:
            speak("Restarting the system.")
            os.system("shutdown /r /t 0")

        elif "shutdown" in command:
            speak("Shutting down the system.")
            os.system("shutdown /s /t 0")

        elif "sleep" in command:
            speak("Putting system to sleep.")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

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
