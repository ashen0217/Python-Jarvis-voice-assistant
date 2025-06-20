import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, there was a problem with the speech service.")
            return ""

if __name__ == "__main__":
    speak("How can I help you?")
    while True:
        command = listen()
        if "hello" in command:
            speak("Hello! How can I assist you?")
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I can't do that yet.")
