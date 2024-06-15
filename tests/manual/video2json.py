from ultralytics import YOLO
from os.path import dirname, abspath, join
import sys

ROOT = dirname(dirname(dirname(abspath(__file__))))
VIDEO_PATH = join(ROOT, "videos", "01.mp4")

sys.path.insert(0, ROOT)
from src.models.detect_model import get_model, track, result2json

model = get_model()

results, _ = track(VIDEO_PATH, model)

result2json(results,"teste3.json")

