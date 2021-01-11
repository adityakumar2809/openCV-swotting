import cv2


image_index = 0


def getImage():
    img = cv2.imread('images/image2.jfif')
    return img


def showImage(img):
    global image_index
    cv2.imshow(f'Image#{image_index}', img)
    image_index += 1


def getGrayScaleImage(img):
    gray_image = cv2.cvtColor(
        src=img,
        code=cv2.COLOR_BGR2GRAY
    )
    return gray_image


def getSimpleThreshold(img, threshold_value):
    threshold, threshold_image = cv2.threshold(
        src=img,
        thresh=threshold_value,
        maxval=255,
        type=cv2.THRESH_BINARY
    )
    return threshold, threshold_image


def getSimpleInverseThreshold(img, threshold_value):
    threshold, inverse_threshold_image = cv2.threshold(
        src=img,
        thresh=threshold_value,
        maxval=255,
        type=cv2.THRESH_BINARY_INV
    )
    return threshold, inverse_threshold_image


def getAdaptiveThreshold(img):
    adaptive_threshold_image = cv2.adaptiveThreshold(
        src=img,
        maxValue=255,
        adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
        thresholdType=cv2.THRESH_BINARY,
        blockSize=11,
        C=3
    )
    return adaptive_threshold_image


def getInverseAdaptiveThreshold(img):
    inverse_adaptive_threshold_image = cv2.adaptiveThreshold(
        src=img,
        maxValue=255,
        adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
        thresholdType=cv2.THRESH_BINARY_INV,
        blockSize=11,
        C=3
    )
    return inverse_adaptive_threshold_image


def main():
    img = getImage()
    showImage(img)

    gray_image = getGrayScaleImage(img)
    showImage(gray_image)

    simple_threshold, simple_threshold_image = getSimpleThreshold(
        gray_image,
        150
    )
    showImage(simple_threshold_image)

    simple_inverse_threshold, simple_inverse_threshold_image =\
        getSimpleInverseThreshold(
            gray_image,
            150
        )
    showImage(simple_inverse_threshold_image)

    adaptive_threshold_image = getAdaptiveThreshold(gray_image)
    showImage(adaptive_threshold_image)

    inverse_adaptive_threshold_image = getInverseAdaptiveThreshold(gray_image)
    showImage(inverse_adaptive_threshold_image)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()
