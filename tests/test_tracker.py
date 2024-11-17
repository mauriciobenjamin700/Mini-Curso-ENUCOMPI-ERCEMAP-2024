from json import load

from src.models.main import is_same_animal


def test_same_animal(mock_predict):

    
    data = mock_predict

    for frame in data:
        tracks = data[frame]['tracks']

        if tracks:

            for track in range(0, len(tracks)-1):
                track1 = tracks[track]
                track2 = tracks[track+1]

                assert is_same_animal(track1, track2) == True