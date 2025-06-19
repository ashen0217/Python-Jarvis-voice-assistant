import core.speech as speech
import core.ai as ai
import core.tts as tts

def main():
    while True:
        text = speech.recognize_speech()
        if text:
            response = ai.get_ai_response(text)
            tts.speak(response)

if __name__ == "__main__":
    main()
