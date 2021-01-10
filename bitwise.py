import cv2
import numpy as np


def getBlank(shape=(400, 400)):
    blank = np.zeros(
        shape=shape,
        dtype='uint8'
    )
    return blank


def main():
    blank = getBlank()


if __name__ == "__main__":
    main()
