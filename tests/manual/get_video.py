from os.path import abspath, dirname, join
    
VIDEOS_PATH = join(dirname(dirname(dirname(abspath(__file__)))), "videos")

def test_path_video(name: str) -> str:
    return join(VIDEOS_PATH, name)

# C:\Users\mauri\Documents\GitHub\UFPI\Mini-Curso-ENUCOMPI-ERCEMAP-2024\videos\01.mp4

if __name__ == "__main__":
    print(test_path_video("01.mp4"))