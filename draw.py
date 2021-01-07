import cv2
import numpy as np


def createBlankImage(size=(500, 500, 3)):
    """Create a blank canvas image"""
    return np.zeros(size, dtype='uint8')


def paintImage(color=(0, 255, 0)):
    blank_image_full = createBlankImage()
    blank_image_partial = createBlankImage()
    blank_image_full[:] = color
    blank_image_partial[200:300, 300:400] = color
    cv2.imshow('FullPaintedScreen', blank_image_full)
    cv2.imshow('PartialPaintedScreen', blank_image_partial)
    cv2.waitKey(0)


def main():
    paintImage()


if __name__ == "__main__":
    main()
