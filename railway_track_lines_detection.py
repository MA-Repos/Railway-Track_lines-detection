import cv2
import numpy as np


def canny_edges(image):
    ex , threshold = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    kernel = np.ones((2, 3), np.uint8)
    opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel, iterations=2)
    edges = cv2.Canny(opening, 3, 3)
    # print(edged)
    return edges

def track_lines_detection():
    image_orignal = cv2.imread('railway_track.jpg')
    image = cv2.cvtColor(image_orignal, cv2.COLOR_BGR2GRAY)
    canny = canny_edges(image)

    # HoughLines
    result = cv2.HoughLinesP(canny, 1, np.pi / 180, 100, 50, minLineLength=180, maxLineGap=200)
    lines = result[:, 0, :][:]
 
    num_of_lines = 0
    for x1, y1, x2, y2 in lines:
        num_of_lines = num_of_lines + 1
        cv2.line(image_orignal, (x1, y1), (x2, y2), (0, 0, 255), 5, cv2.LINE_AA)
        print('Line %s  (x1=%s, y1=%s) ==> (x2=%s, y2=%s) ' % (num_of_lines, x1, y1, x2, y2))
    
    cv2.imwrite("detected_lines.jpg", image_orignal) 
    cv2.imshow('Detected Lines Image', image_orignal)
    cv2.waitKey()

track_lines_detection()