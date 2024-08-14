# Import necessary libraries
import sys
import argparse
import cv2 as cv
import numpy as np

from ultralytics import YOLO
from collections import defaultdict


def process_image(image_name, export_name, model):
    image = cv.imread(image_name)
    results = model(image)

    annotated_image = results[0].plot()

    cv.imwrite(export_name, annotated_image)


def process_video(video_name, export_name, model):
    capture = cv.VideoCapture(video_name)
    output = cv.VideoWriter(export_name, cv.VideoWriter_fourcc(*"mp4v"), 30, (640, 640))

    if not capture.isOpened():
        print("Could not open video file")
        sys.exit(-1)

    while True:
        ret, frame = capture.read()

        if not ret:
            break

        results = model.track(cv.resize(frame, (640, 640)), persist=True)
        annotated_frame = results[0].plot()
        output.write(annotated_frame)

    capture.release()
    output.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run model on video or image", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-t", "--type", help="video or image", type=str, required=True)
    parser.add_argument("-f", "--file", help="Source file", type=str, required=True)
    parser.add_argument("-e", "--export", help="Filename to export as", type=str, required=True)
    parser.add_argument("-m", "--model", help="Model to use", type=str, default="YOLOv10-Bee.pt")

    args = parser.parse_args()

    if args.type == "video":
        process_video(args.file, args.export, args.model)
    elif args.type == "image":
        process_image(args.file, args.export, args.model)
    else:
        print("Invalid type. Please choose either video or image")
        sys.exit(-1)
