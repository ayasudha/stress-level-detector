import time

stress_emotions = ['Angry', 'Fear', 'Sad']

def get_emotion_label(index):
    labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
    return labels[index]

def update_stress_log(emotion):
    with open("logs.txt", "a") as log:
        stress_score = 1 if emotion in stress_emotions else 0
        log.write(f"{int(time.time())},{emotion},{stress_score}\n")
