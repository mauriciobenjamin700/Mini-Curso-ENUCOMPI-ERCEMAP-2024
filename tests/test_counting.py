from src.controllers.apply import count_unique_animals

def test_counting(mock_predict):

    result = count_unique_animals(mock_predict)

    assert result == {'cat': 1}