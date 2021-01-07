import cv2
import numpy as np


def createBlankImage(size=(500, 500, 3)):
    """Create a blank canvas image"""
    return np.zeros(size, dtype='uint8')


def paintImage(color=(0, 255, 0)):
    blank_image = createBlankImage()
    blank_image[:] = color
    cv2.imshow('PaintedScreen', blank_image)
    cv2.waitKey(0)


def main():
    paintImage()


if __name__ == "__main__":
    main()
