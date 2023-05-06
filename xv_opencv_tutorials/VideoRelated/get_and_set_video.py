import cv2 as cv

# 创建VideoCapture对象，用创建的对象去做之后的操作
cap = cv.VideoCapture(0)
# 检测有无摄像头正常使用
# 这是一个必要的验证，当cap为空的时候，后续调用会报错。
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# 获取视频流是一个连续的循环过程,一直在获取,不是说获取到一帧就可以了
while True:
    # 通过创建的VideoCapture对象逐帧获取视频,会返回两个参数,ret返回true和false代表是否正常获取到帧,以及视频是否结束
    # frame代表获取到的帧
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("不能正常读取视频帧")
        break
    # 将获取到的视频帧,也就是一幅幅图像,转为灰度图
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 展示
    cv.imshow('frame', gray)
    # q退出获取视频流
    if cv.waitKey(1) == ord('q'):
        break
# 释放资源
cap.release()
cv.destroyAllWindows()