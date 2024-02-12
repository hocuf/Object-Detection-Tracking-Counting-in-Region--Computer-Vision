# Object Detection, Tracking, Counting in Region Project

In this repo I would like to share with you a project that I have been working on and adding to and subtracting from. This project is a system that uses Python, OpenCV and Ultralytics' big YOLOv8 model to perform real-time object detection, tracking, counting and performance analysis in a specific region, graphing it instantly and saving all the information and states instantly in a csv file. The unique value of the project is the object detection, tracking, counting and component logic that makes coding more readable and cleaner.

It works with a customized component that manually visualizes and instantly graphs the performance of the bounding box, score and ID information for each object detected in a given area. This provides immediate feedback on the tracked objects. you can see it in the test video below. if you want to try it, you can use it by changing the object name in the class_id part of the code and manually entering the zone points.



https://github.com/hocuf/Object-Detection-Tracking-Counting-in-Region--Computer-Vision/assets/92105996/604a5016-dece-46d1-9f33-9ae568612cfe




## Key Features

- **Real-Time Detection & Tracking**: Utilizes the YOLOv8 model for instantaneous object detection and tracking.
- **Region-Based Counting**: Performs object counting within a user-defined region, catering to specific analytical needs.
- **Visual Feedback**: Annotates detected objects with bounding boxes, class IDs, and confidence scores.
- **Data Logging**: Compiles all detections into a CSV file for subsequent analysis and reporting.
- **Performance Metrics**: Offers insights into the system's performance, including FPS and processing times.
- **Temporal Visualization**: Graphically represents the object count over time, facilitating trend observation and analysis.

## Getting Started

To set up the system, clone the repository and install the necessary dependencies:

### Prerequisites

- Python 3.6 or later
- OpenCV library
- Ultralytics YOLOv8 model

### Installation - Useage

* Clone the repository:
   ```sh
   git clone https://github.com/hocuf/Object-Detection-Tracking-Counting-in-Region--Computer-Vision.git
* To run the main script and start processing your video feed:
   ```sh
   python main.py


## Videos
Source: [pixabay](https://pixabay.com/)

