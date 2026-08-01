import cv2

class ObstacleDetector:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)

    def detect(self):
        while True:
            ret, frame = self.camera.read()

            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            edges = cv2.Canny(gray, 100, 200)

            cv2.imshow("Obstacle Detection", edges)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    detector = ObstacleDetector()
    detector.detect()
