import cv2


image_index = 0


def getImage():
    img = cv2.imread('images/image2.jfif')
    return img


def showImage(img):
    global image_index
    cv2.imshow(f'Image#{image_index}', img)
    image_index += 1


def convertBGRToGrayscale(img):
    gray_image = cv2.cvtColor(
        src=img,
        code=cv2.COLOR_BGR2GRAY
    )
    return gray_image


def convertBGRToHSV(img):
    hsv_image = cv2.cvtColor(
        src=img,
        code=cv2.COLOR_BGR2HSV
    )
    return hsv_image


def convertBGRToLAB(img):
    lab_image = cv2.cvtColor(
        src=img,
        code=cv2.COLOR_BGR2LAB
    )
    return lab_image


def main():
    img = getImage()
    showImage(img)

    gray_image = convertBGRToGrayscale(img)
    showImage(gray_image)

    hsv_image = convertBGRToHSV(img)
    showImage(hsv_image)

    lab_image = convertBGRToLAB(img)
    showImage(lab_image)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()
