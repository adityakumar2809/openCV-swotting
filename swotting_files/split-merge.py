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


def getTwoDimBlank(img):
    blank = np.zeros(
        shape=img.shape[:2],
        dtype='uint8'
    )
    return blank


def splitColors(img):
    b, g, r = cv2.split(
        m=img
    )
    return b, g, r


def mergeColors(b, g, r):
    merged_img = cv2.merge(
        mv=[b, g, r]
    )
    return merged_img


def main():
    img = getImage()
    showImage(img)

    b, g, r = splitColors(img)
    showImage(b)
    showImage(g)
    showImage(r)

    merged_image = mergeColors(b, g, r)
    showImage(merged_image)

    blank = getTwoDimBlank(img)
    blue_image = mergeColors(b, blank, blank)
    green_image = mergeColors(blank, g, blank)
    red_image = mergeColors(blank, blank, r)
    showImage(blue_image)
    showImage(green_image)
    showImage(red_image)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()
