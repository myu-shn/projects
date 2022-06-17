from scipy.spatial import distance as dist
from imutils import face_utils
import cv2
from timebudget import timebudget

class EyeBlink(object):

    def __init__(self, detector_param, predictor_param):
        

        self.EYE_AR_THRESH = 0.23
        self.EYE_AR_CONSEC_FRAMES = 3

        # initialize the frame counters and the total number of blinks
        self.COUNTER = 0
        self.TOTAL = 0

        # initialize the status liveness face biometric and spoofing
        self.status_face_biometric = False

        # grab the indexes of the facial landmarks for the left and
        # right eye, respectively
        (self.lStart, self.lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (self.rStart, self.rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

        self.detector = detector_param
        self.predictor = predictor_param

    def eye_aspect_ratio(self, eye):
        # compute the euclidean distances between the two sets of
        # vertical eye landmarks (x, y)-coordinates
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])

        # compute the euclidean distance between the horizontal
        # eye landmark (x, y)-coordinates
        C = dist.euclidean(eye[0], eye[3])

        # compute the eye aspect ratio
        ear = (A + B) / (2.0 * C)

        # return the eye aspect ratio
        return ear

    def predictEyeblink(self, frames):
        for frame in frames:
            self.status_face_biometric = self.detect_eyeblink(frame)
            
        print(self.TOTAL, "BLINK")
        print("Is Blink : ",self.status_face_biometric)
        return self.status_face_biometric

    def detect_eyeblink(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # detect faces in the grayscale frame
        rects = self.detector(gray, 0)
        
        # loop over the face detections
        for rect in rects:

            shape = self.predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)


            leftEye = shape[self.lStart:self.lEnd]
            rightEye = shape[self.rStart:self.rEnd]
            leftEAR = self.eye_aspect_ratio(leftEye)
            rightEAR = self.eye_aspect_ratio(rightEye)

            # average the eye aspect ratio together for both eyes
            ear = (leftEAR + rightEAR) / 2.0

            if ear < self.EYE_AR_THRESH:
                self.COUNTER += 1 
            else:
                if self.COUNTER >= self.EYE_AR_CONSEC_FRAMES:
                    self.TOTAL += 1
                    
                self.COUNTER = 0
        if self.TOTAL > 0:
            self.status_face_biometric = True

        return self.status_face_biometric
