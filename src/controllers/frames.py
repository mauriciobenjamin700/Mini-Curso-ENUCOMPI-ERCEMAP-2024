"""
Este Modulo é responsavel pela manipulação dos resultados provindos do Modelo YOLO para detecção e contagem dos animais:

    - Constraints:
        
    - Funcs:
        - plot
        - generate_video
        -get_video_settings
        
        
    - Classes:

    
"""

from cv2 import (
    VideoCapture, 
    VideoWriter
)
from cv2 import (
    CAP_PROP_FRAME_HEIGHT, 
    CAP_PROP_FRAME_WIDTH, 
    CAP_PROP_FPS, 
    VideoWriter_fourcc
)
from os.path import exists
from src.models.detect_model import get_model
from ultralytics import YOLO
from ultralytics.engine.results import Results


def plot(plots: list) -> None:
    """
    Apresenta na tela todos os plots recebidos de track
    """
    from cv2 import destroyAllWindows, imshow, waitKey
    
    for frame_plot in plots:
        imshow("Frame", frame_plot)
        if waitKey(25) & 0xFF == ord('q'):
            break
        
        destroyAllWindows()
        

def get_video_settings(video: str | VideoCapture) -> dict:
    """
    Obtem as configurações do vídeo e as retorna em formato de dicionário
    
    Args:
        Vídeo: str or VideoCapture: Video que será análisado
    
    Return
        dict{
            fourcc: int,
            fps: float,
            frameSize: Size: tuple
            is_color: bool
        }
    """
    if isinstance(video, str):
        video = VideoCapture(video)
        
     # Coletando um frame para avaliar se o vídeo é ou não colorido
    ret, frame = video.read()
    if not ret:
        raise ValueError("Não foi possível ler o vídeo.")

    video.release()
    
    settings = {
        "fourcc": VideoWriter_fourcc(*'mp4v'),
        "fps": int(video.get(CAP_PROP_FPS)),
        "frameSize": (int(video.get(CAP_PROP_FRAME_WIDTH)), int(video.get(CAP_PROP_FRAME_HEIGHT))),
        "is_color": len(frame.shape) == 3 and frame.shape[2] == 3
    }

    return settings

def video2frames(video: str | VideoCapture) -> list:
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
        
        frames = []

        ret = True
        while ret:
            ret, frame = cap.read()  # Leia frame por frame do vídeo
            if not ret:
                break
            
            
            frames.append(frame)  # Obtenha o resultado da detecção e rastreamento


        cap.release()
        
    return frames
    
    
def save_video(output: str, frames, settings: dict) -> None:
    video = VideoWriter(
        filename=output,
        fourcc=settings["fourcc"],
        fps=settings["fps"],
        frameSize=settings["frameSize"],
        isColor=settings["is_color"]
    )
    
    if len(frames) == 0:
        print("Lista de frames está vazia. Não há nada para salvar.")
        return
    else:
        print(len(frames), " Frames Salvos")
    
    for frame in frames:
        video.write(frame)
    
    video.release()
    print(f"Vídeo salvo em: {output}")
    """   
    video = VideoWriter(
        filename=output,
        fourcc=settings["fourcc"],
        fps=settings["fps"],
        frameSize=settings["frameSize"],
        isColor=True 
    )
    
    for frame in frames:
        video.write(frame)
        
    video.release()
    """
    
def generate_video(file_name: str, frames, settings: dict):
    """
    Gera um vídeo novo com as anotações feitas pelo modelo yolo
    
    Args:
        video: str: Caminho para salvar o vídeo
        frames: list: Lista com os frames que serão salvos no vídeo
    
    Return:
        None
    """
    
    if exists(file_name):
        save_video(f"{file_name}_new.mp4",frames, settings)
    else:
        save_video(f"{file_name}_new.mp4",frames, settings)


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


def track_one_frame(frame, model: YOLO = get_model()) -> list[Results]:
    return model.track(frame, persist=True)