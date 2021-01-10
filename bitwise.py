import cv2
import numpy as np


image_index = 0


def showImage(img):
    global image_index
    cv2.imshow(f'Image#{image_index}', img)
    image_index += 1


def getBlank(shape=(400, 400)):
    blank = np.zeros(
        shape=shape,
        dtype='uint8'
    )
    return blank


def drawRectangle(img):
    rectangle = cv2.rectangle(
        img=img,
        pt1=(30, 30),
        pt2=(370, 370),
        color=255,
        thickness=-1
    )
    return rectangle


def drawCircle(img):
    circle = cv2.circle(
        img=img,
        center=(200, 200),
        radius=200,
        color=255,
        thickness=-1
    )
    return circle


def bitwiseAnd(img1, img2):
    bitwise_and_image = cv2.bitwise_and(
        src1=img1,
        src2=img2
    )
    return bitwise_and_image


def bitwiseOr(img1, img2):
    bitwise_or_image = cv2.bitwise_or(
        src1=img1,
        src2=img2
    )
    return bitwise_or_image


def bitwiseXor(img1, img2):
    bitwise_xor_image = cv2.bitwise_xor(
        src1=img1,
        src2=img2
    )
    return bitwise_xor_image


def main():
    blank = getBlank()
    showImage(blank)

    rectangle = drawRectangle(blank.copy())
    showImage(rectangle)

    circle = drawCircle(blank.copy())
    showImage(circle)

    bitwise_and_image = bitwiseAnd(rectangle, circle)
    showImage(bitwise_and_image)

    bitwise_or_image = bitwiseOr(rectangle, circle)
    showImage(bitwise_or_image)

    bitwise_xor_image = bitwiseXor(rectangle, circle)
    showImage(bitwise_xor_image)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()
