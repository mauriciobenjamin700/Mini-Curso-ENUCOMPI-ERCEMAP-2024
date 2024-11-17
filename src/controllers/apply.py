from cv2 import VideoCapture
from ultralytics import YOLO


from src.models.configs import CONFIANCE, IOU, FRAME_SKIP
from src.models.main import (
    Tracker,
    features, 
    get_model,
    is_same_animal
)
from src.models.classes import animals_list


# https://docs.ultralytics.com/modes/predict/#inference-arguments

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
    
    results = model(video, conf=CONFIANCE, classes=animals_list, iou=IOU, vid_stride=FRAME_SKIP) 

    predicts = {}

    tracker = Tracker()

    if not results:
        raise ValueError("No results found")


    
    frames_result = results
    
    for id, result in enumerate(frames_result,0):
        predicts[id] = features(result, tracker)
        print(f"Frame {id} processed: {predicts[id]}")
    
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
    

def count_unique_animals(results: dict) -> dict[str,int]:
    """
    Retorna a quantidade de animais únicos detectados
    
    - Args:
        - dict: dict
    
    - Return:
        - dict:{"animal": int}
    """
    
    tracked_animals = {}
    animals_quantity = {}

    for frame in results:

        tracks = results[frame]['tracks']
        
        if tracks:
            
            for item in tracks:

                for class_name, box in item:

                    if class_name not in tracked_animals.keys(): # primeira vez que a classe aparece

                        tracked_animals[class_name] = []

                        tracked_animals[class_name].append(box)

                        animals_quantity[class_name] = 1

                    else: # Se a classe já existe, precisa-se checar se não é um animal já contado
                        
                        same_animal = False

                        if box not in tracked_animals[class_name]: # Se a caixa não foi contada

                            for tracked_box in tracked_animals[class_name]: # percorre todas as caixas já contadas daquela classe de animal

                                if is_same_animal(box, tracked_box): # Se a caixa é proxima a alguma caixa já contada
                                        
                                        same_animal = True
    
                                        break
                                
                            if not same_animal: # Se a caixa não é proxima a nenhuma caixa já contada

                                tracked_animals[class_name].append(box) # Salva a caixa de um novo animal
                                
                                animals_quantity[class_name] += 1  # Adiciona mais um animal da mesma classe
                            
                            else: # Apenas adiciona a box na lista para comparações futuras

                                tracked_animals[class_name].append(box)




    return animals_quantity

    
    