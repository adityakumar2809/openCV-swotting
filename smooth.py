import cv2


image_index = 0


def getImage():
    img = cv2.imread('images/image2.jfif')
    return img


def showImage(img):
    global image_index
    cv2.imshow(f'Image#{image_index}', img)
    image_index += 1


def blurUsingAveraging(img):
    average_blur_image = cv2.blur(
        src=img,
        ksize=(3, 3)
    )
    return average_blur_image


def blurUsingGaussianMethod(img):
    gaussian_blur_image = cv2.GaussianBlur(
        src=img,
        ksize=(3, 3),
        sigmaX=0
    )
    return gaussian_blur_image


def blurUsingMedian(img):
    median_blur_image = cv2.medianBlur(
        src=img,
        ksize=3
    )
    return median_blur_image


def blurUsingBilateralMethod(img):
    bilateral_blur_image = cv2.bilateralFilter(
        src=img,
        d=3,
        sigmaColor=15,
        sigmaSpace=15
    )
    return bilateral_blur_image


def main():
    img = getImage()
    showImage(img)

    average_blur_image = blurUsingAveraging(img)
    showImage(average_blur_image)

    gaussian_blur_image = blurUsingGaussianMethod(img)
    showImage(gaussian_blur_image)

    median_blur_image = blurUsingMedian(img)
    showImage(median_blur_image)

    bilateral_blur_image = blurUsingBilateralMethod(img)
    showImage(bilateral_blur_image)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()
