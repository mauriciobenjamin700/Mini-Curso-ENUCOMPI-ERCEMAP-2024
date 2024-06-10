from os.path import abspath, dirname
import sys

from get_video import test_path_video

sys.path.append(dirname(dirname(dirname(abspath(__file__)))))


from src.models.detect_model import get_model, predict

model = get_model()

result = predict(test_path_video("01.mp4"), model)

print(result)

