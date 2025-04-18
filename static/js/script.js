let btn = document.querySelector("#btn");
let content = document.querySelector("#content");
let voice = document.querySelector("#voice");

// Speak Function
function speak(text) {
    let speech = new SpeechSynthesisUtterance(text);
    speech.rate = 1;
    speech.pitch = 1;
    speech.volume = 1;
    speech.lang = "en-US";
    window.speechSynthesis.speak(speech);
}

// Greeting Function
function wishMe() {
    let hour = new Date().getHours();
    if (hour < 12) speak("Good Morning Sir");
    else if (hour < 16) speak("Good Afternoon Sir");
    else speak("Good Evening Sir");
}

// Voice Recognition Setup
let speechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
let recognition = new speechRecognition();

recognition.onresult = (event) => {
    let transcript = event.results[event.resultIndex][0].transcript;
    content.innerText = transcript;
    takeCommand(transcript.toLowerCase());
};

btn.addEventListener("click", () => {
    recognition.start();
    voice.style.display = "block";
    btn.style.display = "none";
});

// Command Handling Function
function takeCommand(message) {
    voice.style.display = "none";
    btn.style.display = "flex";

    // Web & Basic Commands (Client-side)
    if (message.includes("hello") || message.includes("hey")) {
        speak("Hello Sir, what can I help you with?");
    } else if (message.includes("who are you")) {
        speak("I am Shifra, your voice assistant.");
    } else if (message.includes("open youtube")) {
        speak("Opening YouTube...");
        window.open("https://youtube.com", "_blank");
    } else if (message.includes("open google")) {
        speak("Opening Google...");
        window.open("https://google.com", "_blank");
    } else if (message.includes("open facebook")) {
        speak("Opening Facebook...");
        window.open("https://facebook.com", "_blank");
    } else if (message.includes("open instagram")) {
        speak("Opening Instagram...");
        window.open("https://instagram.com", "_blank");
    } else if (message.includes("open whatsapp")) {
        speak("Opening WhatsApp Web...");
        window.open("https://web.whatsapp.com", "_blank");
    } else if (message.includes("time")) {
        let time = new Date().toLocaleTimeString();
        speak("Current time is " + time);
    } else if (message.includes("date")) {
        let date = new Date().toLocaleDateString();
        speak("Today's date is " + date);

    // Unknown / System-level commands — hand over to Python
    } else {
        speak("Let me handle that.");
        fetch('/listen', { method: 'POST' })
            .then(res => console.log("Voice command forwarded to backend."))
            .catch(err => console.error("Backend error:", err));
    }
}
