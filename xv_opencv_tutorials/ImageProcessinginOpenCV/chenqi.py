import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def main():
    # imgcopy[threshold == 2] = 100  # 连通域/背景（蓝）
    # img2 = cv.cvtColor(imgcopy, code=cv.COLOR_HSV2BGR)
    # cv.namedWindow("img2", cv.WINDOW_FREERATIO)
    # cv.imshow('img2', img2)

    img = cv.imread("../imgs/star.png")
    imgcopy = img.copy()
    cv.namedWindow("img", cv.WINDOW_FREERATIO)
    cv.imshow('img', img)
    img = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
    threshold = cv.threshold(img, 150, 255,
                             cv.THRESH_BINARY_INV)[1]

    cv.namedWindow("threshold", cv.WINDOW_FREERATIO)
    cv.imshow('threshold', threshold)
    cv.namedWindow("threshold", cv.WINDOW_FREERATIO)
    cv.imshow('threshold', threshold)
    kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(3, 3))
    close_img = cv.morphologyEx(threshold, op=cv.MORPH_CLOSE, kernel=kernel, iterations=2)
    cv.namedWindow("close_img", cv.WINDOW_FREERATIO)
    cv.imshow('close_img', close_img)

    imgcopy[close_img == 0] = imgcopy[close_img == 0]-70
    cv.namedWindow("imgcopy", cv.WINDOW_FREERATIO)
    cv.imshow('imgcopy', imgcopy)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
