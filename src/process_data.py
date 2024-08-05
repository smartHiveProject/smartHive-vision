import os
import sys
import argparse
import cv2 as cv


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process video to extract frames", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", "--file", help="Source file", type=str, required=True)
    parser.add_argument("-i", "--frame_interval", help="Interval at which to extract frames", type=int, default=6)
    parser.add_argument("-c", "--count", help="Filename start", type=int, default=0)

    args = parser.parse_args()
    capture = cv.VideoCapture(args.file)

    os.makedirs("data", exist_ok=True)

    if not capture.isOpened():
        print(f"Error opening video file {args.file}")
        sys.exit(-1)

    frame_count = 0
    frame_number = 0

    while True:
        ret, frame = capture.read()

        if not ret:
            break

        if not frame_count % args.frame_interval:
            cv.imwrite(f"data/{args.count + int(frame_count/args.frame_interval)}.jpg", frame)

        frame_count += 1
        frame_number += 1

    capture.release()
    print(f"Saved {frame_count} frames")
