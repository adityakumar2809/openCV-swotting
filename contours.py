import cv2
import numpy as np


def getImage():
    img = cv2.imread('images/image4.jfif')
    return img


def convertToGrayscale(img):
    return cv2.cvtColor(
        src=img,
        code=cv2.COLOR_BGR2GRAY
    )


def main():
    img = getImage()
    cv2.imshow('Initial', img)

    gray_img = convertToGrayscale(img)
    cv2.imshow('Grayscale', gray_img)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()
