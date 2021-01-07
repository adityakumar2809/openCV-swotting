import cv2


def convertToGrayScale():
    img = cv2.imread('images/image2.jfif')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale', img)
    cv2.waitKey(0)


def main():
    convertToGrayScale()


if __name__ == "__main__":
    main()
