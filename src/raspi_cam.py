# Simple script to record 10min long videos from a Raspberry Pi

import time
import logging
import cv2 as cv
from datetime import datetime

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO, filename="raspi_camera.log", format="%(asctime)s - %(levelname)s - %(message)s")

    logger.info("Initial startup")

    while True:
        try:
            while True:
                capture = cv.VideoCapture(0)

                capture.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
                capture.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
                capture.set(cv.CAP_PROP_FPS, 30)

                result = cv.VideoWriter(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.avi", cv.VideoWriter_fourcc(*'XVID'), 30, (1280, 720))
                logger.info("Recording started")

                end_time = time.time() + 600

                while time.time() <= end_time:
                    ret, frame = capture.read()

                    if not ret:
                        logger.warn("Failed to capture frame")
                        continue

                    if not cv.waitKey(1):
                        pass

                    result.write(frame)

                result.release()
                capture.release()
                logger.info("Recording completed")
                time.sleep(10)

        except Exception as e:
            logger.error(e, exc_info=True)
            continue
