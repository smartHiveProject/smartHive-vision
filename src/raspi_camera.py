# Script to record 10min long videos from a Raspberry Pi

import time
import queue
import logging
import threading
import cv2 as cv
import numpy as np
from datetime import datetime


def capture_frames():
    capture = cv.VideoCapture(0)

    capture.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
    capture.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
    capture.set(cv.CAP_PROP_FPS, 24)

    time_end = time.time() + 600

    try:
        while time.time() <= time_end:
            ret, frame = capture.read()

            if not ret:
                logger.warning("Failed to capture frame")
                pass

            if not cv.waitKey(1):
                pass

            frame_bytes = frame.tobytes()
            frame_queue.put(frame_bytes)

    except Exception as e:
        logger.error(e, exc_info=True)

    capture.release()
    logger.info("Recording completed")


def write_frames():
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.avi", fourcc, 24, (1280, 720))

    try:
        while not frame_queue.empty() or capturing_thread.is_alive:
            frame_bytes = frame_queue.get()
            out.write(np.frombuffer(frame_bytes, dtype=np.uint8).reshape(720, 1280, 3))

    except Exception as e:
        logger.error(e, exc_info=True)

    out.release()
    logger.info("Writing completed")


if __name__ == "__main__":
    frame_queue = queue.Queue()

    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO, filename="raspi-camera.log", format="%(asctime)s - %(levelname)s - %(message)s")

    logger.info("Initial startup")

    try:
        while True:
            capturing_thread = threading.Thread(target=capture_frames)
            capturing_thread.start()

            writing_thread = threading.Thread(target=write_frames)
            writing_thread.start()

            logger.info("Recording started")

            capturing_thread.join()
            writing_thread.join()

            frame_queue.queue.clear()

            time.sleep(1)

    except Exception as e:
        logger.error(e, exc_info=True)
