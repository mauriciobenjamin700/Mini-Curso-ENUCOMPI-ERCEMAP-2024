"""
Este Modulo é responsavel pela manipulação do Modelo YOLO para detecção e contagem dos animais:

    - Constraints:
        
    - Funcs:
        - get_model
        - predict
        
    - Classes:

    
"""

from ultralytics import YOLO
from os.path import dirname, abspath, join



def get_model() -> YOLO:
    """
    Retorna o modelo YOLO Responsavel Pelas Detecções dos objetos
    """
    MODEL_PATH = join(dirname(abspath(__file__)), "yolov8n.pt")

    model = YOLO(MODEL_PATH)
    
    return model

def predict(video_path: str ,model : YOLO = get_model()):
    
    results = model(video_path)

    
    
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