# Simple script to record 10min long videos from a Raspberry Pi

import cv2 as cv
import time
from datetime import datetime

if __name__ == "__main__":
    capture = cv.VideoCapture(1)

    capture.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
    capture.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
    capture.set(cv.CAP_PROP_FPS, 30)

    while True:
        start_time = time.time()

        result = cv.VideoWriter(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.mp4", cv.VideoWriter_fourcc(*'avc1'), 30, (1280, 720))

        while True:
            ret, frame = capture.read()

            if not ret:
                break

            if cv.waitKey(1) & 0xFF == ord('s'):
                break

            result.write(frame)

            if time.time() - start_time >= 600:
                result.release()
                break
