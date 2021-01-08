import cv2
import numpy as np


def getImage():
    img = cv2.imread('images/image4.jfif')
    return img


def translateImage(x, y):
    img = getImage()
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    translated_image = cv2.warpAffine(
        src=img,
        M=transMat,
        dsize=dimensions
    )
    return translated_image

    # -x --> Left Translation
    # -y --> Up Translation
    # x --> Right Translation
    # y --> Down Translation


def main():
    img = translateImage(20, 50)
    cv2.imshow('Result', img)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
