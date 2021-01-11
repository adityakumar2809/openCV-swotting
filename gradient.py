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


def getGrayScaleImage(img):
    gray_image = cv2.cvtColor(
        src=img,
        code=cv2.COLOR_BGR2GRAY
    )
    return gray_image


def getLaplacianGradient(img):
    lap = cv2.Laplacian(
        src=img,
        ddepth=cv2.CV_64F
    )
    lap = np.uint8(np.absolute(lap))
    return lap


def main():
    img = getImage()
    showImage(img)

    gray_image = getGrayScaleImage(img)
    showImage(gray_image)

    lap_image = getLaplacianGradient(gray_image)
    showImage(lap_image)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()
