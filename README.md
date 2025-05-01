
# Football Analysis Project

This project aims to develop an AI-driven Football Analysis System that utilizes the YOLOv11 object detection model to effectively localize and detect the positions of players, officials, and the ball in real-time during football games. By integrating advanced technology with a user-friendly interface, the system seeks to make football analytics more accessible and widely applicable. Users will gain valuable insights into player movements, positioning, and tactical patterns, enabling a deeper understanding of the game. 

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
📂 Model
Clicking the “Model” button opens a file selection dialog for choosing a YOLO-based model file . It is recommended to use the provided football detection model (best.pt) for optimal performance. However, the system is designed to be flexible and supports loading other YOLO models, making it adaptable for various object detection tasks beyond football.

🎞️ Video
Clicking the “Video” button prompts the user to select a local video file (e.g., .mp4, .avi, .mov). The system then processes the video frame by frame, displaying both the original footage and the detection results within the interface. This mode is ideal for analyzing recorded matches, with features to pause playback, take screenshots, and closely review key moments.

📹 Camera
Clicking the “Camera” button detects and lists all available camera devices (internal or external). Upon selection, the system enters real-time detection mode, capturing and processing the live feed frame by frame. This is useful for live analysis during training sessions or broadcasts.

⏸️ Pause / Play
Clicking “Pause” temporarily halts detection and freezes the current frame, allowing users to closely examine specific events such as player formations or referee decisions. The button toggles to “Play”, which resumes the detection seamlessly.

📷 Screen Shot
Clicking “Screen Shot” captures the current frame with detection results (including bounding boxes) and saves it to a predefined directory. This feature is useful for documenting important events or preparing reports.

🛑 Stop
Clicking “Stop” ends the detection process and stops the video playback or camera stream. The system is then reset, allowing the user to load a new model or input source without restarting the application.

⏹ Exit
Clicking “Exit” safely closes the application. This ensures that all resources—including camera streams, loaded models, and memory—are properly released, preventing crashes or errors in future sessions.


