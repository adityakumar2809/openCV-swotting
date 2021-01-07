import cv2


def readImage():
    image = cv2.imread('images/image1.jfif')
    cv2.imshow('Screen', image)
    cv2.waitKey(0)


def main():
    readImage()


if __name__ == "__main__":
    main()
