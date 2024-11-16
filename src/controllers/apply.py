"""
Funções para inferir o modelo a detectar em videos

- predict: Realiza a extração das métricas em cada frame do vídeo
- track: Realiza a marcação das classes no vídeo e retorna uma lista com os resultados e outra com os frames para plot
"""
from cv2 import VideoCapture
from ultralytics import YOLO


from src.models.detect_model import (
    features, 
    get_model
)


def predict(video: str ,model: YOLO = get_model()) -> dict:
    """
    Realiza a extração das métricas em cada frame do vídeo
    
    - Args:
        - video (str): Caminho para o vídeo que será processado
        - model (YOLO): Modelo YOLO responsavel pelo processamento.
        
    - Return:
        - dict{
            - confidences,
            - class_ids,
            - class_names,
            - counting_class}
    """
    
    results = model(video)

    predicts = {}
    
    for id, result in enumerate(results,0): 
        predicts[id] = features(result)
    
    return predicts

def track(video: str | VideoCapture, model: YOLO = get_model()) -> tuple[list,list]:
    """
    Realiza a marcação das classes no vídeo e retorna uma lista com os resultados e outra com os frames para plot
    
    - Args:
        - video: str or VideoCapture
        - model: YOLO
    
    - Return:
        - tuple(results, frames)
    """

    if isinstance(video, str):
        cap = VideoCapture(video)

    def validate_capture(cap: VideoCapture) -> bool:
        if not cap.isOpened():
            return False

        ret, _ = cap.read()
        if not ret:
            return False
        
        return True 

    if validate_capture(cap):
        
        results = []
        frames = []

        ret = True
        while ret:
            ret, frame = cap.read()  # Leia frame por frame do vídeo
            if not ret:
                break
            
            result = model.track(frame, persist=True)
            results.append(result)  # Detecte e rastreie objetos
            frames.append(result[0].plot())  # Obtenha o resultado da detecção e rastreamento


        cap.release()
        
        return (results, frames)
        
    else:
        return ([], [])