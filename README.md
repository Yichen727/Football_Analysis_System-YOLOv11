
# Football Analysis Project

This project aims to develop an AI-driven Football Analysis System that utilizes the YOLOv11 object detection model to effectively localize and detect the positions of players, officials, and the ball in real-time during football games. By integrating advanced technology with a user-friendly interface, the system seeks to make football analytics more accessible and widely applicable. Users will gain valuable insights into player movements, positioning, and tactical patterns, enabling a deeper understanding of the game. 

## ❓ How to Run

### Clone the Repository:
Clone the project repository to your local machine:
```bash
git clone https://github.com/mradovic38/football_analysis.git
cd football_analysis
```

### Prerequisites
- Ensure you have **Python 3.8 or later** installed.
- Install the required packages using pip:
```bash
pip install -r requirements.txt
```

#### Install Required Dependencies:
Ensure you have all the necessary dependencies installed. You can use a package manager like pip:
```bash
pip install -r requirements.txt
```

#### Run the Script:
Open a terminal and navigate to the project directory. Execute the [`GUI.py`](GUI.py) script to start the analysis:
```bash
python GUI.py
```

## 📜 Feature Explanations
📂Model: When the user clicks the “Model” button, a file selection dialog appears, allowing them to choose a YOLO-based model file (typically with a .pt extension). It is strongly recommended to select the pre-trained football detection model provided with the system (best.pt). However, the system is very flexible, allowing users to load and use other YOLO models as well. This makes it suitable for a wide range of object detection tasks beyond football.

🎞️Video: By clicking the “Video” button, the user is prompted to select a video file (e.g., .mp4, .avi, .mov, etc.) from their local directory. The system then processes the video frame by frame, displaying both the original footage and the detection results simultaneously within the GUI. This mode is ideal for analyzing recorded matches, offering users the ability to pause, screenshot, and review specific game moments.

📹Camera: Clicking the “Camera” button activates the system’s ability to detect and list available camera devices. The user can then choose from internal or external webcams connected to their machine. Once a camera is selected, the application enters real-time detection mode, capturing live video feed and processing each frame on the fly.  

⏸️Pause:  When the user clicks the "Pause" button, the detection temporarily halts, freezing the current frame. This allows the user to observe and analyze specific moments—such as player positioning or referee actions—without the distraction of ongoing motion. Once paused, the button label switches to “Play”, enabling the user to resume the detection process seamlessly.

📷Screen Shot: By clicking the "Screen Shot" button, the user captures the current detection frame (with bounding boxes) and saves it to a predefined directory. This function is especially useful for recording critical events or incidents during a match for later analysis or reporting.

🛑Stop: When the user clicks the "Stop" button, the detection process ends, and the video playback or camera feed is terminated. This action resets the system state, allowing the user to load a new model or input source without restarting the application.

⏹Exit: By clicking the "Exit" button, the application closes safely. This action ensures that all associated resources, such as the camera stream, loaded model, and memory are properly released, preventing system errors or crashes during future use.



