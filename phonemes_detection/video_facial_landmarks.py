# import the necessary packages
from imutils.video import VideoStream
from imutils import face_utils
import datetime
import argparse
import imutils
import time
import dlib
import cv2
import numpy as np
import math

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-r", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])
# face_aligner = openface.AlignDlib(args["shape_predictor"])

# initialize the video stream and allow the cammera sensor to warmup
print("[INFO] camera sensor warming up...")
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)

phonemes = []

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream, resize it to
	# have a maximum width of 400 pixels, and convert it to
	# grayscale
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    if frame.any():
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        clahe_image = clahe.apply(gray)

        detections = detector(frame, 1) #Detect the faces in the image

        for k,d in enumerate(detections): #For each detected face
            shape = predictor(frame, d) #Get coordinates
            vec = np.empty([68, 2], dtype = int)
            c = []
            for i in range(1,68): #There are 68 landmark points on each face
                cv2.circle(frame, (shape.part(i).x, shape.part(i).y), 1, (0,0,255), thickness=1)
                c.append([shape.part(i).x, shape.part(i).y])

            #Mouth coordinates
            # m_60,m_61,m_62,m_63,m_64,m_65,m_66,m_67 = 0,0,0,0,0,0,0,0
            m_48 = c[47]
            m_49 = c[48]
            m_50 = c[49]
            m_51 = c[50]
            m_52 = c[51]
            m_53 = c[52]
            m_54 = c[53]
            m_55 = c[54]
            m_56 = c[55]
            m_57 = c[56]
            m_58 = c[57]
            m_59 = c[58]
            m_60 = c[59]
            m_61 = c[60]
            m_62 = c[61]
            m_63 = c[62]
            m_64 = c[63]
            m_65 = c[64]
            m_66 = c[65]
            m_67 = c[66]


            mouth_vertical = math.sqrt((m_62[0] - m_66[0])**2 + (m_62[1] - m_66[1])**2);

            mouth_horizontal = math.sqrt((m_60[0] - m_64[0])**2 + (m_60[1] - m_64[1])**2);

            b_2 = [(m_62[0] + m_66[0]) / 2, (m_62[1] + m_66[1]) / 2]

            o = [(m_60[0] + m_48[0]) / 2, (m_60[1] + m_48[1]) / 2]

            a_2 = m_62

            print('vertical - %d, horizontal - %d' % (mouth_vertical, mouth_horizontal))
            #prints mouth distance

            cv2.line(frame, (b_2[0], b_2[1]), (o[0], o[1]), (0, 255, 0), 1)

            cv2.line(frame, (a_2[0], a_2[1]), (o[0], o[1]), (255, 0, 0), 1)

            a = np.array([(a_2[0] - o[0]), (a_2[1] - o[1])])
            b = np.array([(b_2[0] - o[0]), (b_2[1] - o[1])])

            arc = np.dot(a, b) / ((np.linalg.norm(a) * np.linalg.norm(b)))
            if arc > 1:
                arc = 1
            elif arc < 0:
                arc = 0
                
            angle = np.arccos(arc)

            print('angle - %f,' % (angle))
            #prints angle between center, corner of mouth (m_60) and m_62. 

            # classificator of phoneme
            # if ()

	# show the frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
