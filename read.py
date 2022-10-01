import cv2 as cv

## read image
img=cv.imread('images/tree-img.jpg')

cv.imshow('tree',img)

cv.waitKey(0)

## Read videos

capture = cv.VideoCapture('videos\dog-video.mp4')

while True:
    isTrue,frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
