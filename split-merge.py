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


def splitColors(img):
    b, g, r = cv2.split(
        m=img
    )
    return b, g, r


def main():
    img = getImage()

    b, g, r = splitColors(img)
    showImage(b)
    showImage(g)
    showImage(r)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()
