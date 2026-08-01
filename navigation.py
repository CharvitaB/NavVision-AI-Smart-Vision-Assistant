from voice_assistant import VoiceAssistant

class NavigationSystem:
    def __init__(self):
        self.voice = VoiceAssistant()

    def navigate(self, obstacle=False, direction="forward"):
        if obstacle:
            self.voice.obstacle_warning()

            if direction == "left":
                self.voice.guide_left()

            elif direction == "right":
                self.voice.guide_right()

            else:
                self.voice.speak("Please stop and scan the surroundings.")

        else:
            self.voice.safe_path()

if __name__ == "__main__":
    navigator = NavigationSystem()

    print("=== Mevice Navigation Demo ===")

    navigator.navigate(obstacle=False)

    navigator.navigate(obstacle=True, direction="left")

    navigator.navigate(obstacle=True, direction="right")

    navigator.navigate(obstacle=True)
