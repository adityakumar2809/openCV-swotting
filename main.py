import cv2

def main():
    image = cv2.imread('images/image1.jfif')
    cv2.imshow('Cat', image)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()