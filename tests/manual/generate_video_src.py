from ultralytics import YOLO
import cv2
from os.path import dirname, abspath, join
import sys

ROOT = dirname(dirname(dirname(abspath(__file__))))
print("root is: ", ROOT)
VIDEO_PATH = join(ROOT, "videos", "01.mp4")

sys.path.insert(0, ROOT)

from src.models.detect_model import get_model, track
from src.models.frames import generate_video, get_video_settings

model = get_model()


frames, plots = track(VIDEO_PATH, model)

settings = get_video_settings(VIDEO_PATH)

generate_video(join(ROOT,"teste.mp4"),plots,settings)
print("terminei")