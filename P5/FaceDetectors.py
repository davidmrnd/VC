import cv2
from imutils import face_utils
import numpy as np

#MTCNN
from mtcnn.mtcnn import MTCNN

class FaceDetector:
    def __init__(self):

        self.FaceDetectors = 'MTCNN'
        faceProto = "opencv_face_detector.pbtxt"
        faceModel = "opencv_face_detector_uint8.pb"
        #MTCNN face detcetor
        self.detectormtcnn = MTCNN()

    def getLargestMTCNNBB(self, objects):
        if len(objects) < 1:
            return -1
        elif len(objects) == 1:
            return 0
        else:
            areas = [ (det['box'][2]*det['box'][3]) for det in objects ]
            return np.argmax(areas)

    def DetectLargestFaceEyesMTCNN(self, img):

        results = self.detectormtcnn.detect_faces(img)

        if not results is None:
            index = self.getLargestMTCNNBB(results)

            if len(results) < 1:
                return None

            # laergest face
            face_info = results[index]

            #print(face_info)

            [x, y, w, h] = face_info['box']
            le = face_info['keypoints']['left_eye']
            re = face_info['keypoints']['right_eye']

            return [x,y,w,h], [le[0], le[1], re[0], re[1]], [face_info['keypoints']['left_eye'], face_info['keypoints']['right_eye'],
                    face_info['keypoints']['nose'], face_info['keypoints']['mouth_left'],
                    face_info['keypoints']['mouth_right']]
        else:
            return None


    def SingleFaceEyesDetection(self, img,facedet,eyesdet):

        if facedet == 'MTCNN':
            values = self.DetectLargestFaceEyesMTCNN(img)

            if values is not None:
                face, eyes, shape = values

                return face, eyes, shape
            else:
                return None

