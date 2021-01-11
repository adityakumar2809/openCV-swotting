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


def performEdgeCascade():
    img = cv2.imread('images/image2.jfif')
    img = cv2.Canny(
        image=img,
        threshold1=125,
        threshold2=175
    )
    # PASS IN BLURRED IMAGES TO REDUCE THE EDGES IN THE FINAL OUTPUT
    cv2.imshow('EdgeCascadeImage', img)
    cv2.waitKey(0)


def dilateImage():
    img = cv2.imread('images/image2.jfif')
    img = cv2.Canny(
        image=img,
        threshold1=125,
        threshold2=175
    )
    cv2.imshow('EdgeCascadeImage', img)
    img = cv2.dilate(
        src=img,
        kernel=(7, 7),
        iterations=5
    )
    cv2.imshow('DilatedImage', img)
    cv2.waitKey(0)


def erodeImage():
    img = cv2.imread('images/image2.jfif')
    img = cv2.Canny(
        image=img,
        threshold1=125,
        threshold2=175
    )
    cv2.imshow('EdgeCascadeImage', img)

    img = cv2.dilate(
        src=img,
        kernel=(7, 7),
        iterations=5
    )
    cv2.imshow('DilatedImage', img)

    img = cv2.erode(
        src=img,
        kernel=(7, 7),
        iterations=5
    )
    cv2.imshow('ErodedImage', img)
    cv2.waitKey(0)


def cropImage():
    img = cv2.imread('images/image2.jfif')
    img = img[50:200, 120:250]
    cv2.imshow('CroppedImage', img)
    cv2.waitKey(0)


def main():
    cropImage()
    # erodeImage()
    # dilateImage()
    # performEdgeCascade()
    # blurImage()
    # convertToGrayScale()


if __name__ == "__main__":
    main()
