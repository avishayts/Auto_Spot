import cv2

refPt = []
cropping = False


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


path = "test.png"
original_image = cv2.imread(path)
image = cv2.resize(original_image, (700, 700))
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
# from teh image and display it
if len(refPt) == 2:
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    print(roi.shape)
    # cv2.imshow("ROI", roi)
    # cv2.waitKey(0)
# close all open windows
cv2.matchTemplate
cv2.destroyAllWindows()

# def main():

# imgCropped =
# cv2.imshow("pic", resize_image)
# cv2.waitKey(0)


# if __name__ == '__main__':
#     main()
