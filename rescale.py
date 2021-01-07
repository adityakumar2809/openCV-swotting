import cv2


def changeResolution(capture, width, height):
    """Used for configuring capture object; Works for Live Videos only"""
    capture.set(3, width)
    capture.set(4, height)
    return capture


def resizeFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


def main():
    pass


if __name__ == "__main__":
    main()
