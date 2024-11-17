from src.controllers.apply import count_unique_animals, predict



def test_predict_video3(get_yolo_model):
    model = get_yolo_model
    feat = predict("videos/03.mp4", model)
    
    for frame_features in feat.values():
        assert "boxes" in frame_features
        assert "confidences" in frame_features
        assert "class_ids" in frame_features
        assert "class_names" in frame_features

    assert count_unique_animals(feat) == {'cat': 1, 'dog': 1}