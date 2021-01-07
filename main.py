import cv2


def readImage():
    image = cv2.imread('images/image1.jfif')
    cv2.imshow('Screen', image)
    cv2.waitKey(0)


def readVideo():
    # VIDEOCAPTURE TAKES EITHER FILEPATH AS ARGUMENT OR AN INTEGER DENOTING
    # CAMERAS WHERE 0 IS USUALLY THE WEBCAM
    capture = cv2.VideoCapture('videos/video1.mov')
    while True:
        isSuccessfullyRead, frame = capture.read()

        if isSuccessfullyRead:
            cv2.imshow('VideoScreen', frame)
        else:
            break

        if cv2.waitKey(20) and 0xFF == ord('d'):
            break

    capture.release()
    cv2.destroyAllWindows()


def main():
    readVideo()
    # readImage()


if __name__ == "__main__":
    main()
