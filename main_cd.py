import numpy as np
import cv2
import datetime
from utlis import orien_lines
from utlis import detector_utlis


# Initialize the Camera
vid = cv2.VideoCapture("car video.mp4")
vid.set(3, 1080)
vid.set(4, 720)
vid.set(10, 1500)
Orientation = "lr"  # Change this to [bt, tb, lr, rl] when camera orientation changes
Line_Perc1=float(5)  # Vary this % of value for Blue Line position
Line_Perc2=float(20)  # Vary this % of value for Red Line position

# Initialize the YOLOv3
wh = 320  # width and height of the input image since using "YOLOv2-320"
classesFile = 'coco.names'  # Classes present in YOLO
classNames = []
with open(classesFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

modelConfiguration = 'yolo.cfg'
modelWeights = 'yolov3.weights'

start_time = datetime.datetime.now()
num_frame = 0

net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)  # Read the Configuration and weights of YOLOv3 from Darknet
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)  # Using OpenCV
net.setPreferableBackend(cv2.dnn.DNN_TARGET_CPU)  # Using CPU

# Main
if __name__ == "__main__":
    while True:
        _, img = vid.read()  # Read each frame from the video
        img = cv2.resize(img, (640, 480), cv2.INTER_CUBIC)
        img = np.array(img)
        img = img[:, :500, :]
        img = cv2.resize(img, (640, 480), cv2.INTER_CUBIC)

        frame = np.array(img)  # Create a numpy array of the image for future manipulation

        # Get the height(h)-value of the Blue Line to generate alert when the object crosses the Safe line
        Line_Position2 = orien_lines.drawSafeLines(frame, img, Orientation, Line_Perc1, Line_Perc2)

        # Preprocess the image as an input for YOLO-320
        blob = cv2.dnn.blobFromImage(img, 1 / 255, (wh, wh), [0, 0, 0], 1, crop=False)
        net.setInput(blob)
        layerNames = net.getLayerNames()
        # Get the layers based on their index
        outputNames = [layerNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        outputs = net.forward(outputNames)

        # Get the box, classes and scores
        detector_utlis.findObjects(outputs, img, classNames, Line_Position2, Orientation)

        # No of Frames
        num_frame = num_frame + 1
        elapsed_time = (datetime.datetime.now() - start_time).total_seconds()
        fps = num_frame / elapsed_time
        detector_utlis.draw_text_on_image("FPS : " + str("{0:.2f}".format(fps)), img)

        cv2.imshow('Result', img)  # Display the image
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Stop the process when you press the key 'q'
            break