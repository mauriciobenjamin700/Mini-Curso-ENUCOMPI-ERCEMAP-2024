from ultralytics import YOLO
import cv2
from os.path import dirname, abspath, join
import sys

ROOT = dirname(dirname(dirname(abspath(__file__))))
VIDEO_PATH = join(ROOT, "videos", "01.mp4")

sys.path.insert(0, ROOT)

from src.models.detect_model import get_model

model = get_model()

cap = cv2.VideoCapture(VIDEO_PATH)

def validate_capture(cap: cv2.VideoCapture) -> bool:
    if not cap.isOpened():
        return False

    ret, _ = cap.read()
    if not ret:
        return False
    
    return True 

if validate_capture(cap):

    ret, frame = cap.read()
    while ret:
        ret, frame = cap.read()  # Leia frame por frame do vídeo
        if not ret:
            break

        results = model.track(frame, persist=True)  # Detecte e rastreie objetos
        
        frame_plot = results[0].plot()  # Obtenha o resultado da detecção e rastreamento

        cv2.imshow("Frame", frame_plot)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
else:
    print("Failed to create window")
