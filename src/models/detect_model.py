"""
Este Modulo é responsavel pela manipulação do Modelo YOLO para detecção e contagem dos animais:

    - Constraints:
        
    - Funcs:
        - get_model
        - predict
        - track
        
    - Classes:

"""
from json import dump, loads
from os.path import abspath, dirname, join
from ultralytics import YOLO
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


def result2json(results: Results | list, output: str = "file.json"):
    """
    Salva os resultados da detecção em um Arquivo JSON
    
    Args:
        results (Results): Objeto results gerado pela yolo após um processo
        output (str, optional): Caminho para salvar o arquivo json. Defaults to "file.json".
        
    Return:
        None
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
    
    



