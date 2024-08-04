# Simple script to record 10min long videos from a Raspberry Pi

import time
import logging
import cv2 as cv
from datetime import datetime

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO, filename="raspi-camera.log", format="%(asctime)s - %(levelname)s - %(message)s")

    logger.info("Initial startup")

    try:
        while True:
            capture = cv.VideoCapture(0)

            capture.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
            capture.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
            capture.set(cv.CAP_PROP_FPS, 30)

            result = cv.VideoWriter(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.mp4", cv.VideoWriter_fourcc(*'avc1'), 30, (1280, 720))
            logger.info("Recording started")

            start_time = time.time()

            while True:
                ret, frame = capture.read()

                if not ret:
                    logger.warn("Failed to capture frame")
                    pass

                if not cv.waitKey(1):
                    pass

                result.write(frame)

                if time.time() - start_time >= 600:
                    result.release()
                    capture.release()
                    logger.info("Recording completed")
                    time.sleep(30)
                    break

    except Exception as e:
        logger.error(e, exc_info=True)
