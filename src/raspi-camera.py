# Simple script to record 10min long videos from a Raspberry Pi

import time
import logging
import cv2 as cv
from datetime import datetime

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO, filename="raspi-camera.log", format="%(asctime)s - %(levelname)s - %(message)s")

    try:
        capture = cv.VideoCapture(0)

        capture.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
        capture.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
        capture.set(cv.CAP_PROP_FPS, 30)

        logger.info("Camera initialized")

        while True:
            start_time = time.time()
            result = cv.VideoWriter(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.mp4", cv.VideoWriter_fourcc(*'avc1'), 30, (1280, 720))
            logger.info("Recording started")

            while True:
                ret, frame = capture.read()

                if not ret:
                    break

                if cv.waitKey(1) & 0xFF == ord('s'):
                    break

                result.write(frame)

                if time.time() - start_time >= 600:
                    result.release()
                    logger.info("Recording completed")
                    break

    except Exception as e:
        logger.error(e, exc_info=True)
