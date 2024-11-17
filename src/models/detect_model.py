from pickle import FALSE
import numpy as np
from os.path import abspath, dirname, join
from ultralytics import YOLO
from ultralytics.engine.results import Results

from src.models.configs import MAX_DISTANCE


def get_model() -> YOLO:
    """
    Retorna o modelo YOLO Responsavel Pelas Detecções dos objetos
    """
    MODEL_PATH = join(dirname(abspath(__file__)), "yolov8n.pt")

    model = YOLO(MODEL_PATH)
    
    return model


def box_distance(box1, box2):
    """
    Calcula a distância euclidiana entre os centros de duas caixas delimitadoras.
    
    Args:
        box1, box2: Listas ou tuplas no formato [x, y, w, h]
        
    Return:
        float: Distância euclidiana
    """
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2
    
    center1 = (x1 + w1 / 2, y1 + h1 / 2)
    center2 = (x2 + w2 / 2, y2 + h2 / 2)
    
    return np.linalg.norm(np.array(center1) - np.array(center2))

class Tracker:
    """
    Classe para rastrear objetos detectados em diferentes frames de um vídeo.

    Args:
        max_distance (int): Distância máxima para considerar que uma nova detecção corresponde a um objeto rastreado anteriormente.

    Attributes:
        max_distance (int): Distância máxima para correspondência de detecções.
        tracks (list): Lista de trilhas, onde cada trilha é uma lista de tuplas (classe, caixa delimitadora).
    """

    def __init__(self, max_distance=MAX_DISTANCE):
        """
        Inicializa um novo objeto Tracker.

        Args:
            max_distance (int): Distância máxima para considerar que uma nova detecção corresponde a um objeto rastreado anteriormente.
        """
        self.max_distance = max_distance
        self.tracks = []

    def update(self, boxes, class_ids):
        """
        Atualiza as trilhas com novas caixas delimitadoras e classes.

        Args:
            boxes (list): Lista de novas caixas delimitadoras no formato [x, y, w, h].
            class_ids (list): Lista de IDs das classes correspondentes às caixas delimitadoras.
        """
        new_tracks = []
        for box, class_id in zip(boxes, class_ids):
            matched = False
            for track in self.tracks:
                if track[-1][0] == class_id and box_distance(box, track[-1][1]) < self.max_distance:
                    track.append((class_id, box))
                    new_tracks.append(track)
                    matched = True
                    break
            if not matched:
                new_tracks.append([(class_id, box)])
        self.tracks = new_tracks

    def get_tracks(self):
        """
        Retorna as trilhas atuais.

        Returns:
            list: Lista de trilhas, onde cada trilha é uma lista de tuplas (classe, caixa delimitadora).
        """
        return self.tracks



def features(result: Results, tracker: Tracker = Tracker()) -> dict:
    """
    Extrai as características de interesse de um objeto results
    
    Args:
        result (Results): Objeto results gerado pela yolo após um processo
        
    Return:
        dict {
            confidences,
            class_ids,
            class_names,
            counting_class,
            tracks
        }
    """
    if isinstance(result, list):
        raise ValueError("Results must be a Results object")
    
    dic = {}
    dic["boxes"] = result.boxes.xywh.tolist()  # Boxes object for bounding box outputs
    dic["confidences"] = [conf.item() for conf in result.boxes.conf] #obtenho o percentual de confiação sobre a detecção
    dic["class_ids"] = [cls.item() for cls in result.boxes.cls] # Obtenho o ID do item detectado (vulgo classe)
    dic["class_names"] = [result.names[key] for key in dic["class_ids"]] #obtenho o nome de todas as classes que o modelo detectou
    #dic["counting_class"] = {nome: dic["class_names"].count(nome) for nome in set(dic["class_names"])}
    
    tracker.update(dic["boxes"], dic["class_names"])
    dic["tracks"] = tracker.get_tracks()
    
    return dic

def is_same_animal(box1: list[float, float, float, float], box2: list[float, float, float, float], max_distance=MAX_DISTANCE) -> bool:
    """
    Verifica se dois rastros pertencem ao mesmo animal com base na distância entre as caixas delimitadoras.

    a função retorna True se a distância entre as caixas delimitadoras for menor ou igual a max_distance, indicando que elas pertencem ao mesmo animal. Caso contrário, retorna False, indicando que as caixas estão muito distantes para serem consideradas do mesmo animal.

    Args:
        track1, track2: Listas de caixas delimitadoras no formato [x, y, w, h].
        max_distance (int): Distância máxima para considerar que as caixas delimitadoras pertencem ao mesmo animal.

    Return:
        bool: True se for o mesmo animal, False caso contrário.
    """
    return box_distance(box1, box2) <= max_distance