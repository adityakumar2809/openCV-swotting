import cv2
import numpy as np
import matplotlib.pyplot as plt


image_index = 0


def getImage():
    img = cv2.imread('images/image2.jfif')
    return img


def showImage(img):
    global image_index
    cv2.imshow(f'Image#{image_index}', img)
    image_index += 1


def getMask(img):
    mask = np.zeros(
        shape=img.shape[:2],
        dtype='uint8'
    )
    return mask


def getCircleMask(img, mask):
    circle_mask = cv2.circle(
        img=mask,
        center=(img.shape[1]//2, img.shape[0]//2),
        radius=70,
        color=255,
        thickness=-1
    )
    return circle_mask


def getMaskedImage(img, mask):
    masked_image = cv2.bitwise_and(
        src1=img,
        src2=img,
        mask=mask
    )
    return masked_image


def convertBGRToGrayscale(img):
    gray_image = cv2.cvtColor(
        src=img,
        code=cv2.COLOR_BGR2GRAY
    )
    return gray_image


def calculateGrayHistogram(img):
    gray_histogram = cv2.calcHist(
        images=[img],
        channels=[0],
        mask=None,
        histSize=[256],
        ranges=[0, 256]
    )
    return gray_histogram


def calculateGrayMaskedHistogram(img, mask):
    gray_histogram = cv2.calcHist(
        images=[img],
        channels=[0],
        mask=mask,
        histSize=[256],
        ranges=[0, 256]
    )
    return gray_histogram


def showGrayHistogram(gray_histogram):
    plt.figure()
    plt.title('Grayscale Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')
    plt.plot(gray_histogram)
    plt.xlim([0, 256])
    plt.show()


def calculateColorHistogram(img):
    colors = ('b', 'g', 'r')
    color_histogram = []
    for i, color in enumerate(colors):
        color_histogram.append(
            cv2.calcHist(
                images=[img],
                channels=[i],
                mask=None,
                histSize=[256],
                ranges=[0, 256]
            )
        )
    return color_histogram


def main():
    img = getImage()
    showImage(img)

    gray_image = convertBGRToGrayscale(img)
    showImage(gray_image)

    gray_histogram = calculateGrayHistogram(gray_image)
    showGrayHistogram(gray_histogram)

    mask = getMask(gray_image)
    showImage(mask)
    circle_mask = getCircleMask(gray_image, mask)
    showImage(circle_mask)
    masked_image = getMaskedImage(gray_image, circle_mask)
    showImage(masked_image)
    gray_mask_histogram = calculateGrayMaskedHistogram(
        masked_image,
        circle_mask
    )
    showGrayHistogram(gray_mask_histogram)

    color_histogram = calculateColorHistogram(img)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()
