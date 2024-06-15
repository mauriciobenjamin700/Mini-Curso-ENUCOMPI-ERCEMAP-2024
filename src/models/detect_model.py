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
from json import dump, loads
from typing import List, Tuple
from ultralytics import YOLO
from os.path import abspath, dirname, join

from ultralytics.engine.results import Results


def get_model() -> YOLO:
    """
    Retorna o modelo YOLO Responsavel Pelas Detecções dos objetos
    """
    MODEL_PATH = join(dirname(abspath(__file__)), "yolov8n.pt")

    model = YOLO(MODEL_PATH)
    
    return model

def features(result: Results) -> dict:
    """
    Extrai as caractéristicas de interesse de um objeto results
    
    Args:
        result (Results): Objeto results gerado pela yolo após um processo
        
    Return:
        dict {
            confidences,
            class_ids,
            class_names,
            counting_class
        }
    """
    
    if isinstance(result, list):
        result = result[0]
    
    dic = {}
    #dic["boxes"] = result.boxes  # Boxes object for bounding box outputs
    dic["confidences"] = [conf.item() for conf in result.boxes.conf] #obtenho o percentual de confiação sobre a detecção
    dic["class_ids"] = [cls.item() for cls in result.boxes.cls] # Obtenho o ID do item detectado (vulgo classe)
    dic["class_names"] = [result.names[key] for key in dic["class_ids"]] #obtenho o nome de todas as classes que o modelo detectou
    dic["counting_class"] = {nome: dic["class_names"].count(nome) for nome in set(dic["class_names"])}
    return dic

def describe_results(result: Results):
    
    dic = features(result)
    
    for key, value in dic.items():
        print(f"\n\n{key}: {value}\n")

def result2json(results: Results | list, output: str = "file.json"):
    """
    
    """

    if isinstance(results, list):
        if len(results) == 1: # Caso seja uma lista com um único item
            results = results[0]
            json_object = loads(results.tojson())
        else: # caso seja uma lista com vários itens
            data = []
            for result in results: # para cada item, acessa o objeto
                data.append(result[0].tojson())
                
            json_object = [loads(json_str) for json_str in data]
    
    with open(output, "w", encoding='utf-8') as json_file:
        dump(json_object, json_file, ensure_ascii=False, indent=4)
    
def predict(video: str ,model : YOLO = get_model()) -> dict:
    """
    Realiza a extração das métricas em cada frame do vídeo
    
    Args:
        video (str): Caminho para o vídeo que será processado
        model (YOLO): Modelo YOLO responsavel pelo processamento.
        
    Return:
        dict {
            confidences,
            class_ids,
            class_names,
            counting_class
        }
    """
    
    results = model(video)

    predicts = {}
    
    for id, result in enumerate(results,0): 
        predicts[id] = features(result)
    
    return predicts

def track(video: str | VideoCapture, model: YOLO = get_model()) -> Tuple[list,list]:
    """
    Realiza a marcação das classes no vídeo e retorna uma lista com os resultados e outra com os frames para plot
    
    Args:
        video: str or VideoCapture
        model: YOLO
    
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
    
    
def take_one_frame(video: str | VideoCapture):
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
        ret, frame = cap.read()
        
        if ret:
            return frame
    
    return None


def track_one_frame(frame, model: YOLO = get_model()) -> List[Results]:
    return model.track(frame, persist=True)


