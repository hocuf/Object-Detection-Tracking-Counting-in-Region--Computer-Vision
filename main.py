"""
OBJECT DETECTION-TRACKING-COUNTING PROJECT ARCHITECTURE

- Import libraries
- Get the capture (real time or video)
- Return and run the capture
- Finish it or keep going

- Creating component as function or file
    - Process the capture in loop
        - Object detection and tracking
            - Load YOLO and run it
            - Get results
                - Access to data
                - Process to data
            - Show results
        - Finish it or keep going
        - Object counting in region
        - Finish it or keep going
        - Display performance metric
        - Finish it or keep going

"""


# - Import libraries
import cv2
from object_function import detect_track_count_on_region
from performance import PerformanceMonitor

from ultralytics import YOLO
model = YOLO('yolov8l.pt')

# * DUPLICATE IS ABOUT ENVIRONMENT ERROR
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"







# Choose it class id
"""
0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 
6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 
11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 
16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 
21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 
26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 
31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 
36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 40: 'wine glass', 
41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 
46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 
51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 
56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 
61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote',
66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 
71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 
76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'}
"""


class_id = 'person'
# region coordinates
left_upper = (400,300)
left_down = (1000,700)
right_down = (1240,700)
right_upper = (490,270)


# - Get the capture (real time or video)
video_path = 'data/test_video1.mp4'
cap = cv2.VideoCapture(video_path)

# Define performance metric to use
performance_monitor = PerformanceMonitor()


frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, (frame_width, frame_height))



#- Return the capture in loop
while cap.isOpened():
    ret, frame = cap.read()
    if ret:

        # Performance first metric
        performance_monitor.start_frame()
        # - Process capture in loop
        # verbose=False : Not extra info
        results = model(frame, verbose=False)
        # Just get labels name
        labels = results[0].names
        # Check it out - print(labels)
        # Check it out - print(results)

        # Created function that access and process capture data as component
        detect_track_count_on_region(frame,results,labels, class_id,left_upper, left_down, right_upper, right_down )

        # Performance final metric
        performance_monitor.end_frame()
        out.write(frame)
        cv2.imshow('Window', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# - Finish it
cap.release()
out.release()
cv2.destroyAllWindows()
performance_monitor.summarize()
