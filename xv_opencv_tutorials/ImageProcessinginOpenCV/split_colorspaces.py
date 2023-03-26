import cv2 as cv


def main():
    # 读取图像
    src = cv.imread("../imgs/opencv.png")
    # 转换HSV空间
    hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
    # 分离通道
    h, s, v = cv.split(hsv)
    cv.namedWindow("v", cv.WINDOW_NORMAL)
    cv.imshow("v", v)
    # 减小亮度
    v1 = v - 30
    cv.namedWindow("v1", cv.WINDOW_NORMAL)
    cv.imshow("v1", v1)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
