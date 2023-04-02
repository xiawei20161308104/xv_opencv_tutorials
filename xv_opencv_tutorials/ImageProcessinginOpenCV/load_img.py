import cv2 as cv
import  sys
# 创建窗口
# 参数一winname：string类型的窗口名称，参数二flags：窗口类型，使用规定好的类型，默认WINDOW_AUTOSIZE
cv.namedWindow('img IMREAD_GRAYSCALE', cv.WINDOW_NORMAL)
cv.namedWindow('img1 original', cv.WINDOW_NORMAL)
cv.namedWindow('img2 original had alpha', cv.WINDOW_NORMAL)

# 读取图像
# 参数一filename：string类型的图片路径，参数二flags：读取方式，比如读取哪个通道，哪些保留哪些丢弃等。使用规定好的类型。
# 以灰度图形式读取
img = cv.imread("../imgs/opencv.png", cv.IMREAD_GRAYSCALE)
# 因为imread读取不到的时候不会报错，所有这里需要判空
if img is None:
    sys.exit("Could not read the image.")
print("灰度图大小为：", img.shape)
# 以默认形式读取原图，没有透明度通道
img1 = cv.imread("../imgs/opencv.png")
print("默认方式读取大小为：", img1.shape)
# 以IMREAD_UNCHANGED形式读取原图，有透明度通道
img2 = cv.imread("../imgs/opencv.png", cv.IMREAD_UNCHANGED)
print("不忽略透明度通道大小为：", img2.shape)
# 展示图像
# 参数一winname：string类型的窗口名称，参数二mat：图像。配合cv.namedWindow使用。
cv.imshow('img IMREAD_GRAYSCALE', img)
cv.imshow('img1 original', img1)
cv.imshow('img2 original had alpha', img2)
# waitKey（0）将无限显示窗口，直到按下任何键为止,适用于想显示图像的时候。
# waitKey（25）将显示一帧并等待大约25ms的按键，适用于逐帧显示视频的时候。
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("../imgs/opencv1.png", img)
cv.destroyAllWindows()
