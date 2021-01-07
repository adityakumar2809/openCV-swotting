import cv2


def convertToGrayScale():
    img = cv2.imread('images/image2.jfif')
    img = cv2.cvtColor(
        src=img,
        code=cv2.COLOR_BGR2GRAY
    )
    cv2.imshow('Grayscale', img)
    cv2.waitKey(0)


def blurImage():
    img = cv2.imread('images/image2.jfif')
    img = cv2.GaussianBlur(
        src=img,
        ksize=(3, 3),
        sigmaX=cv2.BORDER_DEFAULT
    )
    # KSIZE MUST BE COMPOSED OF ODD NUMBERS
    cv2.imshow('BlurImage', img)
    cv2.waitKey(0)


def main():
    blurImage()
    # convertToGrayScale()


if __name__ == "__main__":
    main()
