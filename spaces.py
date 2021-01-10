import cv2


def getImage():
    img = cv2.imread('images/image2.jfif')
    return img


def showImage(img):
    cv2.imshow('Image', img)


def convertBGRToGrayscale(img):
    gray_image = cv2.cvtColor(
        src=img,
        code=cv2.COLOR_BGR2GRAY
    )
    return gray_image


def main():
    img = getImage()
    showImage(img)

    gray_image = convertBGRToGrayscale(img)
    showImage(gray_image)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()
