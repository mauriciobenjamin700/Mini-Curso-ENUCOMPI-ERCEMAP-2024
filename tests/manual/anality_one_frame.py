from ultralytics import YOLO
from os.path import dirname, abspath, join
import sys

ROOT = dirname(dirname(dirname(abspath(__file__))))
VIDEO_PATH = join(ROOT, "videos", "01.mp4")

sys.path.insert(0, ROOT)
from src.models.detect_model import get_model, track_one_frame, features, take_one_frame, describe_results, result2json

model = get_model()

frame = take_one_frame(VIDEO_PATH)

result = track_one_frame(frame, model)

result2json(result,"teste1.json")


#print(result[0].tojson())
#print(type(result[0].tojson()))

describe_results(result)

