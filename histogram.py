import cv2
import numpy as np


image_index = 0


def getImage():
    img = cv2.imread('images/image2.jfif')
    return img


def showImage(img):
    global image_index
    cv2.imshow(f'Image#{image_index}', img)
    image_index += 1


def convertBGRToGrayscale(img):
    gray_image = cv2.cvtColor(
        src=img,
        code=cv2.COLOR_BGR2GRAY
    )
    return gray_image


def calculateGrayHistogram(img):
    gray_histogram = cv2.calcHist(
        images=[img],
        channels=[0],
        mask=None,
        histSize=[256],
        ranges=[0, 256]
    )


def main():
    img = getImage()
    showImage(img)

    gray_image = convertBGRToGrayscale(img)
    showImage(gray_image)

    gray_histogram = calculateGrayHistogram(gray_image)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()
