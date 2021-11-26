import cv2
import numpy as np
import math
refPt = []
cropping = False


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv2.warpAffine(img, rotMat, dimensions)


def resize(img, scalar):
    (height, width) = img.shape[:2]
    print(height, width)
    return cv2.resize(img, (math.floor(width*scalar), math.floor(height*scalar)), interpolation=cv2.INTER_CUBIC)


def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False
        # draw a rectangle around the region of interest
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)

# def detect_apprarances


path = "test2.jpg"
# original_image = cv2.imread(path)
# image = cv2.resize(original_image, (700, 700))
image = cv2.imread(path)
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)
while True:
    # display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF
    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        image = clone.copy()
    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break
# if there are two reference points, then crop the region of interest
# from the image and display it
roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
# rotated = rotate(roi, -25, None)
# cv2.imshow("Rotated", rotated)
# cv2.waitKey(0)
resized = resize(roi, 1.4)
cv2.imshow("Resized", resized)
cv2.waitKey(0)
if len(refPt) == 2:
    h, w = roi.shape[:2]
    res = cv2.matchTemplate(clone, roi, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):  # Switch collumns and rows
        cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    cv2.imshow("result", image)
    cv2.waitKey(0)
# close all open windows
cv2.destroyAllWindows()


# def main():

# imgCropped =
# cv2.imshow("pic", resize_image)
# cv2.waitKey(0)


# if __name__ == '__main__':
#     main()
