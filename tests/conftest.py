from json import load
from pytest import fixture


from src.models.main import get_model

@fixture
def get_yolo_model():
    return get_model()


@fixture
def mock_predict():
    with open('tests/test.json', 'r') as f:
        data = load(f)

    return data