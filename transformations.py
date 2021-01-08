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


def rotateImage(angle, rotation_point=None):
    img = getImage()
    (height, width) = img.shape[:2]

    if rotation_point is None:
        rotation_point = (width//2, height//2)

    rotation_matrix = cv2.getRotationMatrix2D(
        center=rotation_point,
        angle=angle,
        scale=1.0
    )
    dimensions = (width, height)
    rotated_image = cv2.warpAffine(
        src=img,
        M=rotation_matrix,
        dsize=dimensions
    )
    return rotated_image


def main():
    img = rotateImage(45)
    # img = translateImage(20, 50)
    cv2.imshow('Result', img)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
