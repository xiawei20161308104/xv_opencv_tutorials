import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
# 定义编码方式创建VideoWriter对象
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('../imgs/output_video.avi', fourcc, 20.0, (640, 480))

# 当cap打开状态执行
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # 写入文件
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
