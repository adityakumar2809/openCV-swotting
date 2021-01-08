import cv2
import numpy as np


def getImage():
    img = cv2.imread('images/image4.jfif')
    return img


def main():
    img = getImage()
    cv2.imshow('Result', img)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
