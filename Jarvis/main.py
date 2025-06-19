import speech_recognition as sr
import pyttsx3

# Initialize recognizer and engine
r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print("Say that again please...")
        return "None"

if __name__ == "__main__":
    speak("Hello, I am Jarvis. How can I help you?")
    while True:
        query = listen().lower()

        if query == "hello":
            speak("Hello to you too!")
        elif query == "what's your name":
            speak("My name is Jarvis.")
        elif query == "exit":
            speak("Goodbye!")
            break
        elif query != "None":
            speak("I heard you, but I don't know what to do with that yet.")
