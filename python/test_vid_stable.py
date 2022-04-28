import os
from turtle import width
import cv2
from cv2 import Mat
from cv2 import vconcat
import numpy as np
from vidstab import VidStab, layer_overlay, download_ostrich_video

# Download test video to stabilize
if not os.path.isfile("ostrich.mp4"):
    download_ostrich_video("ostrich.mp4")

stabilizer = VidStab()
vidcap = cv2.VideoCapture("ostrich.mp4")

object_bounding_box = None
while True:
    
    grabbed_frame, frame = vidcap.read()
    stabilized_frame = stabilizer.stabilize_frame(input_frame=frame, border_size=50)
    if stabilized_frame is None:
        break
    # Display stabilized output
    cv2.imshow('stabilized_frame', stabilized_frame)
    cv2.imshow('original frame', frame)

    key = cv2.waitKey(5)

  
    if key == 27:
        break

vidcap.release()
cv2.destroyAllWindows()