from ultralytics import YOLO
import cv2
from os.path import dirname, abspath, join
import sys

ROOT = dirname(dirname(dirname(abspath(__file__))))
VIDEO_PATH = join(ROOT, "videos", "01.mp4")

sys.path.insert(0, ROOT)

from src.models.detect_model import get_model, track
from src.controllers.frames import plot

model = get_model()


frames, plots = track(VIDEO_PATH, model)

plot(plots)