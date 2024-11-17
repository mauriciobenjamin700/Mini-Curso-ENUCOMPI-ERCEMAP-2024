from src.controllers.apply import predict
from src.controllers.save import to_json



def test_features(get_yolo_model):
    model = get_yolo_model
    feat = predict("videos/02.mp4", model)
    
    for frame_features in feat.values():
        assert "boxes" in frame_features
        assert "confidences" in frame_features
        assert "class_ids" in frame_features
        assert "class_names" in frame_features

    to_json(feat, "tests/test.json")