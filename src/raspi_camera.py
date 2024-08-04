# Script to record 10min long videos from a Raspberry Pi

import time
import queue
import logging
import threading
import cv2 as cv
import numpy as np
from datetime import datetime


def capture_frames(frame_queue_arg):
    capture = cv.VideoCapture(0)

    capture.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
    capture.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
    capture.set(cv.CAP_PROP_FPS, 24)

    time_end = time.time() + 600

    while time.time() <= time_end:
        ret, frame = capture.read()

        if not ret:
            logger.warn("Failed to capture frame")
            pass

        if not cv.waitKey(1):
            pass

        frame_bytes = frame.tobytes()
        frame_queue.put(frame_bytes)

    capture.release()


def write_frames(frame_queue_arg):
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.avi", fourcc, 24, (1280, 720))

    while not frame_queue.empty():
        frame_bytes = frame_queue.get()
        out.write(np.frombuffer(frame_bytes, dtype=np.uint8).reshape(720, 1280, 3))

    out.release()


if __name__ == "__main__":
    frame_queue = queue.Queue()

    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO, filename="raspi-camera.log", format="%(asctime)s - %(levelname)s - %(message)s")

    logger.info("Initial startup")

    try:
        while True:
            capturing_thread = threading.Thread(target=capture_frames, args=(frame_queue,))
            capturing_thread.start()

            writing_thread = threading.Thread(target=write_frames, args=(frame_queue,))
            writing_thread.start()

            logger.info("Recording started")

            capturing_thread.join()
            logger.info("Recording completed")
            writing_thread.join()
            logger.info("Writing completed")

            time.sleep(1)

    except Exception as e:
        logger.error(e, exc_info=True)
