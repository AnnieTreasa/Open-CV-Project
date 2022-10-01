import cv2 as cv

img = cv.imread('images/tree-img.jpg')
cv.imshow('tree',img)
def rescaleFrame(frame,scale=0.75):
    
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)


    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

cv.imshow('tree',img)
resize_image = rescaleFrame(img)
cv.imshow('Image',resize_image)
cv.imwrite("resized_image.png",resize_image,[cv.IMWRITE_PNG_COMPRESSION,0])
cv.waitKey(0)

