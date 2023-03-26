import cv2 as cv
import numpy as np


def main():
    # flags = [i for i in dir(cv) if i.startswith('COLOR_')]
    # print( flags )
    src = cv.imread("../imgs/opencv.png")
    cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
    cv.imshow("input", src)

    hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    cv.imwrite('hsv.png', hsv)
    cv.imshow("hsv", hsv)
    cv.imshow("gray", gray)

    # 分离通道
    h, s, v = cv.split(hsv)
    b, g, r = cv.split(src)
    cv.namedWindow("h", cv.WINDOW_NORMAL)
    cv.imshow("h", h)
    cv.namedWindow("s", cv.WINDOW_NORMAL)
    cv.imshow("s", s)
    cv.namedWindow("v", cv.WINDOW_NORMAL)
    cv.imshow("v", v)

    cv.namedWindow("b", cv.WINDOW_NORMAL)
    cv.imshow("b", b)
    cv.namedWindow("g", cv.WINDOW_NORMAL)
    cv.imshow("g", g)
    cv.namedWindow("r", cv.WINDOW_NORMAL)
    cv.imshow("r", r)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
