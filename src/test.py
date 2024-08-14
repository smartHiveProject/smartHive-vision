from ultralytics import YOLO
import cv2 as cv

model = YOLO("YOLOv10-Bee.pt")

results = model("111_jpg.rf.652858cc2b3bad85bfc635f81e5bbfa4.jpg")

annotated_frame = results[0].plot()
cv.imwrite("tracked.jpg", annotated_frame)
