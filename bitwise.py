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
        thickness=3
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


def main():
    blank = getBlank()
    showImage(blank)

    rectangle = drawRectangle(blank.copy())
    showImage(rectangle)

    circle = drawCircle(blank.copy())
    showImage(circle)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()
