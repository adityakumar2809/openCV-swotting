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


def getEdges(img):
    canny = cv2.Canny(
        image=img,
        threshold1=125,
        threshold2=175
    )
    return canny


def getContours(canny):
    contours, hierarchies = cv2.findContours(
        image=canny,
        mode=cv2.RETR_LIST,
        method=cv2.CHAIN_APPROX_NONE
    )
    return contours, hierarchies


def main():
    img = getImage()
    cv2.imshow('Initial', img)

    gray_img = convertToGrayscale(img)
    cv2.imshow('Grayscale', gray_img)

    canny_img = getEdges(img)
    cv2.imshow('Canny', canny_img)

    contours, hierarchies = getContours(canny=canny_img)
    print(f'Found {len(contours)} coutours.')

    cv2.waitKey(0)


if __name__ == "__main__":
    main()
