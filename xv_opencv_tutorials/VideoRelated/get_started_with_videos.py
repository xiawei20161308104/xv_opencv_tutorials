import cv2 as cv

# 创建VideoCapture对象，用创建的对象去做之后的操作
cap2 = cv.VideoCapture(0)

while True:
    # 获取设备参数，cv.CAP_PROP_FRAME_WIDTH,CAP_PROP_FRAME_HEIGHT是cv2提供的参数选项
    width, height = cap2.get(cv.CAP_PROP_FRAME_WIDTH), cap2.get(cv.CAP_PROP_FRAME_HEIGHT)
    # 我这里是1280.0 720.0
    print(width, height)

    # 以原分辨率的两倍来捕获
    cap2.set(cv.CAP_PROP_FRAME_WIDTH, width * 2)
    cap2.set(cv.CAP_PROP_FRAME_HEIGHT, height * 2)
    _, frame2 = cap2.read()

    gray_double = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)
    # 展示
    cv.imshow('doubel read', gray_double)
    # q退出获取视频流
    if cv.waitKey(1) == ord('q'):
        break
# 释放资源
cap2.release()
cv.destroyAllWindows()
