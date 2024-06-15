import threading

import cv2

from ultralytics import YOLO

from ultralytics import YOLO
from os.path import dirname, abspath, join
import sys

ROOT = dirname(dirname(dirname(abspath(__file__))))
VIDEO_PATH = join(ROOT, "videos", "01.mp4")

sys.path.insert(0, ROOT)

from src.models.detect_model import get_model

model = get_model()


def run_tracker_in_thread(filename, model, file_index):
    """
    Runs a video file or webcam stream concurrently with the YOLOv8 model using threading.

    This function captures video frames from a given file or camera source and utilizes the YOLOv8 model for object
    tracking. The function runs in its own thread for concurrent processing.

    Args:
        filename (str): The path to the video file or the identifier for the webcam/external camera source.
        model (obj): The YOLOv8 model object.
        file_index (int): An index to uniquely identify the file being processed, used for display purposes.

    Note:
        Press 'q' to quit the video display window.
    """
    video = cv2.VideoCapture(filename)  # Read the video file

    while True:
        ret, frame = video.read()  # Read the video frames

        # Exit the loop if no more frames in either video
        if not ret:
            break

        # Track objects in frames if available
        results = model.track(frame, persist=True)
        res_plotted = results[0].plot()
        cv2.imshow(f"Tracking_Stream_{file_index}", res_plotted)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    # Release video sources
    video.release()


# Load the models
model1 = get_model()



# Create the tracker threads
tracker_thread1 = threading.Thread(target=run_tracker_in_thread, args=(VIDEO_PATH, model1, 1), daemon=True)

# Start the tracker threads
tracker_thread1.start()

# Wait for the tracker threads to finish
tracker_thread1.join()

# Clean up and close windows
cv2.destroyAllWindows()