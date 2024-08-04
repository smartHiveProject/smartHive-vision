import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, )

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
print(cap.get(cv2.CAP_PROP_FPS))
frames = 0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(f"help.avi", fourcc, 15, (1280, 720))

while True:
    ret, fram = cap.read()
    frames += 1
    out.write(fram)
