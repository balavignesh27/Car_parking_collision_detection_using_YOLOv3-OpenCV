import cv2
import numpy as np
from utlis import alertcheck

confThreshold = 0.5  # To draw the bbox when the confidence is more than 50%
nmsThreshold = 0.3  # To avoid overlapping of bbox on same object. Lower it is better the result
a=b=0

def findObjects(outputs, img, classNames, Line_Position2, Orientation):
    """ Method Name: findObjects
        Description: This method creates the boundary box on the image
        Output: Passes the position of the bbox to trigger the alarm when the object reaches the Blue/Safe Line
                and returns a dummy value """

    hT, wT, cT = img.shape
    bbox = []
    classIds = []
    conf_values = []

    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                w, h = int(det[2] * wT), int(det[3] * hT)
                x, y = int((det[0] * wT) - w / 2), int((det[1] * hT) - h / 2)
                bbox.append([x, y, w, h])
                classIds.append(classId)
                conf_values.append(float(confidence))
    # print((bbox))
    indices = cv2.dnn.NMSBoxes(bbox, conf_values, confThreshold, nmsThreshold)

    for i in indices:
        i = i[0]
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]

        p1 = (int(x), int(y))
        p2 = (int(x+w), int(y+h))

        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
        cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(conf_values[i] * 100)}%',
                    (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255, 2))

        # Passes the position of the bbox to trigger the alarm when the object reaches the Blue/Safe Line
        a = alertcheck.drawBoxToSafeLine(img, p1, p2, Line_Position2, Orientation)
        return a

def draw_text_on_image(fps, image_np):
    cv2.putText(image_np, fps, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)



def distance_to_camera(knownWidth, focalLength, pixelWidth):
    return (knownWidth * focalLength) / pixelWidth