import cv2
import mediapipe as mp
import numpy as np
from tensorflow.keras.models import load_model
from utils.emotion_utils import get_emotion_label, update_stress_log

model = load_model("models/emotion_model.h5")
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

mp_face_detection = mp.solutions.face_detection
face_detector = mp_face_detection.FaceDetection()

def start_detection():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detector.process(rgb_frame)

        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                h, w, _ = frame.shape
                x, y, w_box, h_box = int(bboxC.xmin * w), int(bboxC.ymin * h), \
                                     int(bboxC.width * w), int(bboxC.height * h)

                face = frame[y:y+h_box, x:x+w_box]
                if face.size == 0:
                    continue
                face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                face_resized = cv2.resize(face_gray, (48, 48))
                face_input = face_resized.reshape(1, 48, 48, 1) / 255.0

                pred = model.predict(face_input)
                emotion = emotion_labels[np.argmax(pred)]
                update_stress_log(emotion)

                cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                cv2.rectangle(frame, (x, y), (x + w_box, y + h_box), (0, 255, 0), 2)

        cv2.imshow("Stress Detector", frame)
        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
