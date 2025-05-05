
# Football Analysis System based on YOLOv11 with GUI

This project develops an AI-driven Football Analysis System using the YOLOv11 model to detect players, referee, and the ball in real time. With an integrated graphical user interface(GUI), it makes football analytics more accessible and practical.

## 📁 Dataset
The self-annotated dataset used for training and evaluation is available for download via Google Drive:

🔗 https://drive.google.com/drive/folders/1ibCxaK_JHJPj_oyBDrQcdeggLVoGwqdX?usp=drive_link

This dataset includes 4,000+ labeled images covering players, referees, and footballs, annotated for optimal training of YOLO-based object detection models.

## ❓ How to Run

### Clone the Repository:
Clone the project repository to your local machine:
```bash
git clone https://github.com/Yichen727/football_analyze_yolov11.git
cd football_analyze_yolov11
```

### Prerequisites
- Ensure you have **Python 3.8 or later** installed.
link: https://www.python.org/downloads/release/python-380/

- Ensure you have all the necessary dependencies installed:
```bash
pip install -r requirements.txt
```

#### Run the Script:
Open a terminal and navigate to the project directory. Execute the [`GUI.py`](GUI.py) script to start the analysis:
```bash
python GUI.py
```

## 📜 Feature Explanations
📂 Model:
Clicking the “Model” button opens a file selection dialog for choosing a YOLO-based model file . It is recommended to use the provided football detection model (yolov11_football.pt) for optimal performance.

🎞️ Video:
Clicking the “Video” button prompts the user to select a local video file. The system then processes the video frame by frame, displaying both the original footage and the detection results within the interface.

📹 Camera:
Clicking the “Camera” button detects and lists all available camera devices (internal or external). Upon selection, the system enters real-time detection mode, capturing and processing the live feed frame by frame.

⏸️ Pause / Play:
Clicking “Pause” temporarily halts detection and freezes the current frame, allowing users to closely examine specific events. The button toggles to “Play”, which resumes the detection seamlessly.

📷 Screen Shot:
Clicking “Screen Shot” captures the current frame with detection results (including bounding boxes) and saves it to a predefined directory. 

🛑 Stop:
Clicking “Stop” ends the detection process and stops the video playback or camera stream. The system is then reset, allowing the user to load a new model or input source without restarting the application.

⏹ Exit:
Clicking “Exit” safely closes the application. 


