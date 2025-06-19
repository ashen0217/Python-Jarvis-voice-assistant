import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def main():
    while True:
        query = listen().lower()

        if query == "none":
            continue

        elif "hello" in query:
            speak("Hello! How can I help you?")

        elif "exit" in query:
            speak("Goodbye!")
            break

        elif "open website" in query:
            speak("Which website do you want me to open?")
            website = listen().lower()
            if website != "none":
                speak(f"Opening {website}")
                webbrowser.open(website)

        elif "what is the time" in query:
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            speak(f"The time is {current_time}")

if __name__ == "__main__":
    main()
