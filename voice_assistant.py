import pyttsx3
import time

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 160)
        self.engine.setProperty("volume", 1.0)

    def speak(self, message):
        print(f"[VOICE]: {message}")
        self.engine.say(message)
        self.engine.runAndWait()

    def obstacle_warning(self):
        self.speak("Warning! Obstacle detected ahead.")

    def guide_left(self):
        self.speak("Please move left.")

    def guide_right(self):
        self.speak("Please move right.")

    def safe_path(self):
        self.speak("Path is clear. You can move forward.")

if __name__ == "__main__":
    assistant = VoiceAssistant()

    assistant.safe_path()
    time.sleep(2)

    assistant.obstacle_warning()
    time.sleep(2)

    assistant.guide_left()
    time.sleep(2)

    assistant.guide_right()
