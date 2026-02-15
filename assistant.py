import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        print("Sorry, I did not understand.")
        return ""

def run_assistant():
    speak("Hello! I am your voice assistant.")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello Raj! How can I help you?")

        elif "time" in command:
            time = datetime.datetime.now().strftime("%H:%M")
            speak("The time is " + time)

        elif "date" in command:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + date)

        elif "search" in command:
            speak("What should I search?")
            query = listen()
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak("Here are the search results.")

        elif "wikipedia" in command:
            speak("What topic?")
            topic = listen()
            try:
                summary = wikipedia.summary(topic, sentences=2)
                speak(summary)
            except:
                speak("Sorry, I couldn't find information.")

        elif "bye" in command:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("Please say a valid command.")

run_assistant()
