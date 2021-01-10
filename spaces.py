import cv2
import matplotlib.pyplot as plt


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


def displayImageUsingRGBFormat(img):
    plt.imshow(img)
    plt.show()


def convertBGRToRGB(img):
    rgb_image = cv2.cvtColor(
        src=img,
        code=cv2.COLOR_BGR2RGB
    )
    return rgb_image


def convertHSVToBGR(img):
    bgr_image = cv2.cvtColor(
        src=img,
        code=cv2.COLOR_HSV2BGR
    )
    return bgr_image


def convertLABToBGR(img):
    bgr_image = cv2.cvtColor(
        src=img,
        code=cv2.COLOR_LAB2BGR
    )
    return bgr_image


def main():
    img = getImage()
    showImage(img)

    gray_image = convertBGRToGrayscale(img)
    showImage(gray_image)

    hsv_image = convertBGRToHSV(img)
    showImage(hsv_image)

    lab_image = convertBGRToLAB(img)
    showImage(lab_image)

    displayImageUsingRGBFormat(img)

    rgb_image = convertBGRToRGB(img)
    displayImageUsingRGBFormat(rgb_image)

    bgr_image = convertHSVToBGR(hsv_image)
    showImage(bgr_image)

    bgr_image = convertLABToBGR(lab_image)
    showImage(bgr_image)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()
