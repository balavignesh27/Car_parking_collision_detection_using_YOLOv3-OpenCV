import cv2

# Draw Safe lines
def drawSafeLines(image_np, img, Orientation, Line_Perc1, Line_Perc2):
    """ Method Name: drawSafeLines
        Description: This method creates the Blue/Safe Line and Red/Danger Line based on the orientation given
        Output: Returns the height(h)-value of the Blue Line to generate alert when the object crosses this line """

    cv2.putText(img, "Blue Line : Safety Border Line", (0,160),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1, cv2.LINE_AA)
    cv2.putText(img, 'Red Line : Danger Border Line', (0, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1, cv2.LINE_AA)

    # Use this orientation when your object moves from bottom to top in the frame
    if (Orientation == "bt"):
        Line_Position1 = int(image_np.shape[0] * (Line_Perc1 / 100))

        Line_Position2 = int(image_np.shape[0] * (Line_Perc2 / 100))

        cv2.line(img=img, pt1=(0, Line_Position1), pt2=(image_np.shape[1], Line_Position1), color=(0,0,255),
                 thickness=2, lineType=8, shift=0)

        cv2.line(img=img, pt1=(0, Line_Position2), pt2=(image_np.shape[1], Line_Position2), color=(255,0,0),
                 thickness=2, lineType=8, shift=0)

        return Line_Position2

    # Use this orientation when your object moves from top to bottom in the frame
    elif (Orientation == "tb"):

        Line_Position1 = int(image_np.shape[0] - (image_np.shape[0] * (Line_Perc1 / 100)))

        Line_Position2 = int(image_np.shape[0] - (image_np.shape[0] * (Line_Perc2 / 100)))

        cv2.line(img=img, pt1=(0, Line_Position1), pt2=(image_np.shape[1], Line_Position1), color=(0, 0, 255),
                 thickness=2, lineType=8, shift=0)

        cv2.line(img=img, pt1=(0, Line_Position2), pt2=(image_np.shape[1], Line_Position2), color=(255, 0, 0),
                 thickness=2, lineType=8, shift=0)

        return Line_Position2

    # Use this orientation when your object moves from left to right in the frame
    elif (Orientation == "lr"):

        Line_Position1 = int(image_np.shape[1] - (image_np.shape[1] * (Line_Perc1 / 100)))

        Line_Position2 = int(image_np.shape[1] - (image_np.shape[1] * (Line_Perc2 / 100)))

        cv2.line(img=img, pt1=(Line_Position1, 0), pt2=(Line_Position1, image_np.shape[0]), color=(0, 0, 255),
                 thickness=2, lineType=8, shift=0)

        cv2.line(img=img, pt1=(Line_Position2, 0), pt2=(Line_Position2, image_np.shape[0]), color=(255, 0, 0),
                 thickness=2, lineType=8, shift=0)

        return Line_Position2

    # Use this orientation when your object moves from right to left in the frame
    elif (Orientation == "rl"):

        Line_Position1 = int(image_np.shape[1] * (Line_Perc1 / 100))

        Line_Position2 = int(image_np.shape[1] * (Line_Perc2 / 100))

        cv2.line(img=img, pt1=(Line_Position1, 0), pt2=(Line_Position1, image_np.shape[0]), color=(0, 0, 255),
                 thickness=2, lineType=8, shift=0)

        cv2.line(img=img, pt1=(Line_Position2, 0), pt2=(Line_Position2, image_np.shape[0]), color=(255, 0, 0),
                 thickness=2, lineType=8, shift=0)

        return Line_Position2