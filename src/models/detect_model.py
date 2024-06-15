"""
Este Modulo é responsavel pela manipulação do Modelo YOLO para detecção e contagem dos animais:

    - Constraints:
        
    - Funcs:
        - get_model
        - predict
        - track
        
    - Classes:

"""

from cv2 import VideoCapture
from typing import Tuple
from ultralytics import YOLO
from os.path import abspath, dirname, join, basename


def get_model() -> YOLO:
    """
    Retorna o modelo YOLO Responsavel Pelas Detecções dos objetos
    """
    MODEL_PATH = join(dirname(abspath(__file__)), "yolov8n.pt")

    model = YOLO(MODEL_PATH)
    
    return model

def predict(video: str ,model : YOLO = get_model()) -> dict:
    """
    Realiza a extração das métricas em cada frame do vídeo
    """
    
    results = model(video)

    predicts = {}
    
    for id, result in enumerate(results,0):
        dic = {}
        #dic["boxes"] = result.boxes  # Boxes object for bounding box outputs
        dic["confidences"] = [conf.item() for conf in result.boxes.conf] #obtenho o percentual de confiação sobre a detecção
        dic["class_ids"] = [cls.item() for cls in result.boxes.cls] # Obtenho o ID do item detectado (vulgo classe)
        dic["class_names"] = [result.names[key] for key in dic["class_ids"]] #obtenho o nome de todas as classes que o modelo detectou
        dic["counting_class"] = {nome: dic["class_names"].count(nome) for nome in set(dic["class_names"])}
        
        predicts[id] = dic
    
    return predicts

def track(video: str | object, model: YOLO = get_model()) -> Tuple[list,list]:
    """
    Realiza a marcação das classes no vídeo e retorna uma lista com os resultados e outra com os frames para plot
    
    Return:
    Tuple(results, frames)
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

        ret, frame = cap.read()
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


    

