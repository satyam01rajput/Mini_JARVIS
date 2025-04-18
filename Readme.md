
# Jarvis - Desktop Voice Assistant (with Web Integration) 🎙️💻

**Jarvis** is a smart desktop voice assistant built using **Flask (Python)** and **Vanilla JavaScript**. It responds to voice commands to open system apps like **Calculator**, **Notepad**, **Chrome**, and also performs web searches or opens websites like **YouTube**, **Google**, and more — all from a sleek browser interface.

## 🚀 Features

- ✅ Web-based voice recognition using JavaScript.
- ✅ Real-time speech synthesis (Jarvis speaks back to you).
- ✅ Python- and Flask-powered backend for executing system-level commands.
- ✅ Opens popular Windows apps like Calculator, Notepad, Chrome, Word, Excel, PowerPoint, etc.
- ✅ Can also open system folders like Downloads, Documents, Pictures, and more.
- ✅ Executes browser-based searches or directly opens websites.
- ✅ Built-in multi-threading support for smooth, non-blocking responses.
- ✅ Commands to restart, shut down, or put the system to sleep.
- ✅ Fun, interactive, and useful for daily tasks!

---

## 🛠️ Technologies Used

- **Frontend:** HTML, CSS, JavaScript (Web Speech API)
- **Backend:** Python, Flask, pyttsx3, SpeechRecognition
- **Others:** OS module, threading for async operations

---

## 📂 Project Structure

```bash
Jarvis/
│
├── templates/
│   └── index.html       # Main frontend UI
├── static/
│   └── css/             # Styling
│   └── script.js        # JavaScript for voice interaction
├── app.py               # Python backend logic (Flask app)
└── README.md            # You're here!
⚙️ How to Run the App
🔧 Prerequisites
Python 3.x

Pip

Working Microphone

Modern browser (Chrome recommended)

📦 Required Libraries
Install all required packages using:

bash
Copy
Edit
pip install Flask pyttsx3 SpeechRecognition
Optional (for speech support on Windows):

bash
Copy
Edit
pip install pipwin
pipwin install pyaudio
▶️ Run the Flask App
bash
Copy
Edit
python app.py
Open your browser at http://127.0.0.1:5000/, and click the microphone icon to start speaking to Jarvis!

🎤 Sample Voice Commands
🌐 Web-Based Commands:
"Open YouTube"

"Open Google"

"Search for weather today"

💻 System-Level Commands:
"Open calculator"

"Open notepad"

"Open Chrome"

"Open file manager"

"Open drive C"

"Open drive D"

"Open WhatsApp"

"Open command prompt"

"Open PowerShell"

"Open control panel"

"Open task manager"

"Open Microsoft Word"

"Open Microsoft Excel"

"Open PowerPoint"

"Open camera"

"Open settings"

"Open photos"

"Open music"

"Shutdown" / "Restart" / "Sleep"

📌 Notes
If the browser says “Sorry, I didn’t catch that,” try refreshing the page.

Some commands are executed via JavaScript in the browser; others use Flask to run Python code.

The system-level commands require Python and microphone access to work correctly.

🙌 Author
Satyam Rajput

🔗 GitHub | 🔗 Portfolio
📧 Available for collaborations and internships!









💡 Future Improvements
Add user login/authentication

Introduce dark mode and improved UI

Implement hotword detection like “Hey Jarvis”

Add GPT/AI-powered smart responses

Create auto-refresh feature for the page
