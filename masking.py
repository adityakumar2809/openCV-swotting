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


def getMask(img):
    mask = np.zeros(
        shape=img.shape[:2],
        dtype='uint8'
    )
    return mask


def getCircleMask(img, mask):
    circle_mask = cv2.circle(
        img=mask,
        center=(img.shape[1]//2, img.shape[0]//2),
        radius=70,
        color=255,
        thickness=-1
    )
    return circle_mask


def main():
    img = getImage()
    showImage(img)

    mask = getMask(img)
    showImage(mask)

    circle_mask = getCircleMask(img, mask)
    showImage(circle_mask)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()
