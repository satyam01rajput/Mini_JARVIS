
# Shifra - Desktop Voice Assistant (with Web Integration) 🎙️💻

Shifra is a smart voice assistant built using **Flask (Python)** and **Vanilla JavaScript**. It responds to voice commands to open apps like **Calculator**, **Notepad**, **Chrome**, and also performs web searches or opens sites like **YouTube**, **Google**, **Facebook**, and more.

## 🚀 Features

- ✅ Web-based voice recognition using JavaScript.
- ✅ Real-time speech synthesis (Shifra speaks back).
- ✅ Integration with Python (Flask) for system-level commands.
- ✅ Opens desktop applications like Calculator, Notepad, Chrome, File Explorer, etc.
- ✅ Can also open websites via voice commands.
- ✅ Works seamlessly with a browser UI.

---

## 🛠️ Technologies Used

- **Frontend:** HTML, CSS, JavaScript (Web Speech API)
- **Backend:** Python, Flask, pyttsx3, SpeechRecognition
- **Others:** OS module, threading for async execution

---

## 📂 Project Structure

```bash


project/
│
├── templates/
│   └── index.html       # Frontend page
├── static/
        css
│   └── script.js        # JavaScript logic
├── app.py               # Python backend using Flask
└── README.md            # You're here!
⚙️ How to Run the App
🔧 Prerequisites
Python 3.x

Pip installed

Working Microphone

A modern browser (Chrome recommended)

📦 Required Libraries
Install all the dependencies:


pip install Flask pyttsx3 SpeechRecognition
(Optional for speech in Windows):
pip install pyaudio


If you face issues installing pyaudio, use:

pip install pipwin
pipwin install pyaudio


▶️ Run the Flask App
python app.py
It will start running on: http://127.0.0.1:5000/

Open it in your browser and click the mic button to start talking to Shifra!

🎤 Sample Commands You Can Say
🌐 Web-Based Commands:
"Open YouTube"

"Open Google"

"What's the time?"

"What's the date?"

💻 System-Level Commands:
"Open calculator"

"Open notepad"

"Open chrome"

"Open file manager"

"Open drive c"

"Open whatsapp"

"Open command prompt"

"Open control panel"

"Shutdown" / "Restart"

📌 Note
If the browser says “Sorry, I didn’t catch that,” and the assistant doesn't respond, refresh the page (or use auto-refresh feature in the future).

Voice command processing is split: Basic commands are handled in JavaScript, while system-level commands go to Flask for execution.

🙌 Author
Satyam Rajput
🔗 GitHub | 🔗 Portfolio | 📧 Available for collaborations and internships!

💡 Future Improvements
Add login/authentication for personal usage.

Add dark mode and better UI styling.

Use hotword detection like "Hey Shifra".

Add AI-based replies using GPT APIs.

Feel free to star 🌟 the repo if you liked it!

yaml


---

Let me know if you want a Hindi version, logo badge, screenshots section, or a GitHub actions dep