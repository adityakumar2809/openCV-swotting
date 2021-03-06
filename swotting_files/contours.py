import cv2
import numpy as np


def getBlank(img):
    return np.zeros(
        shape=img.shape,
        dtype='uint8'
    )


def getImage():
    img = cv2.imread('images/image4.jfif')
    return img


def convertToGrayscale(img):
    return cv2.cvtColor(
        src=img,
        code=cv2.COLOR_BGR2GRAY
    )


def getThresholdedImage(img):
    return cv2.threshold(
        src=img,
        thresh=125,
        maxval=255,
        type=cv2.THRESH_BINARY
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


def drawContours(blank_image, contours):
    return cv2.drawContours(
        image=blank_image,
        contours=contours,
        contourIdx=-1,
        color=(0, 0, 255),
        thickness=3
    )


def main():
    img = getImage()
    cv2.imshow('Initial', img)

    gray_img = convertToGrayscale(img)
    cv2.imshow('Grayscale', gray_img)

    ret, thresh_img = getThresholdedImage(gray_img)
    cv2.imshow('Threshold', thresh_img)

    canny_img = getEdges(thresh_img)
    cv2.imshow('Canny', canny_img)

    contours, hierarchies = getContours(canny=canny_img)
    print(f'Found {len(contours)} coutours.')

    blank_image = getBlank(img)
    image_contours = drawContours(blank_image, contours)
    cv2.imshow('Contours', image_contours)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()
