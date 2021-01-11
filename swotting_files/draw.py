import cv2
import numpy as np


def createBlankImage(size=(500, 500, 3)):
    """Create a blank canvas image"""
    return np.zeros(size, dtype='uint8')


def paintImage(color=(0, 255, 0)):
    canvas_full = createBlankImage()
    canvas_partial = createBlankImage()
    canvas_full[:] = color
    canvas_partial[200:300, 300:400] = color
    cv2.imshow('FullPaintedScreen', canvas_full)
    cv2.imshow('PartialPaintedScreen', canvas_partial)
    cv2.waitKey(0)


def drawRectangle():
    canvas = createBlankImage()
    cv2.rectangle(
        img=canvas,
        pt1=(125, 125),
        pt2=(375, 375),
        color=(255, 0, 255),
        thickness=5
    )
    cv2.imshow('RectangleScreen', canvas)
    cv2.rectangle(
        img=canvas,
        pt1=(125, 125),
        pt2=(375, 375),
        color=(255, 0, 255),
        thickness=cv2.FILLED
    )
    cv2.imshow('RectangleFilledScreen', canvas)
    cv2.waitKey(0)


def drawCircle():
    canvas = createBlankImage()
    cv2.circle(
        img=canvas,
        center=(250, 250),
        radius=100,
        color=(255, 0, 255),
        thickness=5
    )
    cv2.imshow('CircleScreen', canvas)
    cv2.waitKey(0)


def drawLine():
    canvas = createBlankImage()
    cv2.line(
        img=canvas,
        pt1=(125, 125),
        pt2=(375, 375),
        color=(0, 0, 255),
        thickness=5
    )
    cv2.imshow('LineScreen', canvas)
    cv2.waitKey(0)


def writeText():
    canvas = createBlankImage()
    cv2.putText(
        img=canvas,
        text='Hello World!',
        org=(100, 100),
        fontFace=cv2.FONT_HERSHEY_COMPLEX,
        fontScale=1.0,
        color=(255, 0, 0),
        thickness=2
    )
    cv2.imshow('TextScreen', canvas)
    cv2.waitKey(0)


def main():
    writeText()
    # drawLine()
    # drawCircle()
    # drawRectangle()
    # paintImage()


if __name__ == "__main__":
    main()
