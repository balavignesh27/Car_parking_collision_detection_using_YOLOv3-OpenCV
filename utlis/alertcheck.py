import cv2
from playsound import playsound


def drawBoxToSafeLine(img,p1,p2,Line_Position2,Orientation):
    """ Method Name: drawBoxToSafeLine
        Description: This method creates the alert sound and displays a Alert message when the distance reaches zero or
                    below based on the orientation given
        Output: Returns a dummy values """
    
    if Orientation == "bt":
        bounding_mid = (int((p1[0]+p2[0])/2), int(p1[1]))
        if bounding_mid:
            cv2.line(img=img, pt1=bounding_mid, pt2=(bounding_mid[0],Line_Position2), color=(0,0,255), thickness=1, lineType=8, shift=0)
            distance_from_line = bounding_mid[1] - Line_Position2
            cv2.putText(img, "d : " + str(distance_from_line) + " cm",
                        (bounding_mid[0] + 10, bounding_mid[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 0, 255), 2)

    elif Orientation == "tb":
        bounding_mid = (int((p1[0]+p2[0])/2), int(p2[1]))
        if bounding_mid:
            cv2.line(img=img, pt1=bounding_mid, pt2=(bounding_mid[0],Line_Position2), color=(255, 0, 0), thickness=1, lineType=8, shift=0)
            distance_from_line = Line_Position2 - bounding_mid[1]
            cv2.putText(img, "d : " + str(distance_from_line) + " cm",
                        (bounding_mid[0] + 10, bounding_mid[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 0, 255), 2)

    elif Orientation == "lr":
        bounding_mid = (int(p2[0]), int((p1[1]+p2[1])/2))
        if bounding_mid:
            cv2.line(img=img, pt1=bounding_mid, pt2=(Line_Position2,bounding_mid[1]), color=(255, 0, 0), thickness=1, lineType=8, shift=0)
            distance_from_line = Line_Position2 - bounding_mid[0]
            cv2.putText(img, "d : "+str(distance_from_line/100)+" m", (bounding_mid[0]+10,bounding_mid[1]),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 0, 255), 2)

    elif Orientation == "rl":
        bounding_mid = (int(p1[0]), int((p1[1]+p2[1])/2))
        if bounding_mid:
            cv2.line(img=img, pt1=bounding_mid, pt2=(Line_Position2,bounding_mid[1]), color=(255, 0, 0), thickness=1, lineType=8, shift=0)
            distance_from_line = bounding_mid[0] - Line_Position2
            cv2.putText(img, "d : "+str(distance_from_line)+" cm", (bounding_mid[0]+10,bounding_mid[1]),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 0, 255), 2)

    # Generate the alert when the distance is zero or below from the object to the Blue/Safe line
    if distance_from_line <= 0:
        posi = int(img.shape[1]/2)
        cv2.putText(img, "ALERT", (posi, 70),cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 2)
        playsound("utlis/alert.wav")
        cv2.rectangle(img, (posi-20,40), (posi+85,80), (0,0,255), thickness=3, lineType=8, shift=0)
        return 1

    else:
        return 0
    
   


