"""
Este Modulo é responsavel pela manipulação dos resultados provindos do Modelo YOLO para detecção e contagem dos animais:

    - Constraints:
        
    - Funcs:
        - plot
        - generate_video
        
        
    - Classes:

    
"""

from cv2 import VideoCapture, VideoWriter
from cv2 import CAP_PROP_FRAME_HEIGHT, CAP_PROP_FRAME_WIDTH, CAP_PROP_FPS, VideoWriter_fourcc
from os.path import dirname, join, basename

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
    
    Return
        dict{
            fourcc: int,
            fps: float,
            frameSize: Size: tuple
        }
    """
    if isinstance(video, str):
        video = VideoCapture(video)
        

    
    settings = {
        "fourcc": VideoWriter_fourcc(*'mp4v'),
        "fps": int(video.get(CAP_PROP_FPS)),
        "frameSize": (int(video.get(CAP_PROP_FRAME_WIDTH)), int(video.get(CAP_PROP_FRAME_HEIGHT)))
    }

    return settings
    
def save_video(output: str, frames, settings: dict) -> None:
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
    
def generate_video(video: str, frames):
    """
    Gera um vídeo novo com as anotações feitas pelo modelo yolo
    """
    settings = get_video_settings(video)
    
    save_video(join(dirname(video),basename(video)+".mp4"),frames, settings)