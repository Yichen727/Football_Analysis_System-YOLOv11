import os
import cv2
import torch
import numpy as np
 
from PySide6.QtGui import QIcon
from PySide6 import QtWidgets, QtCore, QtGui
 
from ultralytics import YOLO
 
 
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.init_gui()
        self.model = None
        self.timer = QtCore.QTimer()
        self.timer1 = QtCore.QTimer()
        self.cap = None
        self.video = None
        self.timer.timeout.connect(self.camera_show)
        self.timer1.timeout.connect(self.video_show)
 
    def init_gui(self):
        self.setFixedSize(960, 440)
        self.setWindowTitle('Football Show')
 
        centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(centralWidget)
 
        mainLayout = QtWidgets.QVBoxLayout(centralWidget)
 
        topLayout = QtWidgets.QHBoxLayout()
        self.oriVideoLabel = QtWidgets.QLabel(self)
        self.detectlabel = QtWidgets.QLabel(self)
        self.oriVideoLabel.setMinimumSize(448, 336)
        self.detectlabel.setMinimumSize(448, 336)
        self.oriVideoLabel.setStyleSheet('border:1px solid #D7E2F9;')
        self.detectlabel.setStyleSheet('border:1px solid #D7E2F9;')
        # 960 540  1920 960
 
        topLayout.addWidget(self.oriVideoLabel)
        topLayout.addWidget(self.detectlabel)
 
        mainLayout.addLayout(topLayout)
 
        # Output Box and Buttons
        groupBox = QtWidgets.QGroupBox(self)
 
        bottomLayout = QtWidgets.QVBoxLayout(groupBox)
 
        mainLayout.addWidget(groupBox)
 
        btnLayout = QtWidgets.QHBoxLayout()
        self.selectModel = QtWidgets.QPushButton('📂Model')
        self.selectModel.setFixedSize(100, 50)
        self.selectModel.clicked.connect(self.load_model)
        self.openVideoBtn = QtWidgets.QPushButton('🎞️Video')
        self.openVideoBtn.setFixedSize(100, 50)
        self.openVideoBtn.clicked.connect(self.start_video)
        self.openVideoBtn.setEnabled(False)
        self.openCamBtn = QtWidgets.QPushButton('📹Camera')
        self.openCamBtn.setFixedSize(100, 50)
        self.openCamBtn.clicked.connect(self.start_camera)
        self.pauseBtn = QtWidgets.QPushButton('⏸️Pause')
        self.pauseBtn.setFixedSize(100, 50)
        self.pauseBtn.clicked.connect(self.pause_resume)
        self.screenshotBtn = QtWidgets.QPushButton('📷Screen Shot')
        self.screenshotBtn.setFixedSize(100, 50)
        self.screenshotBtn.setEnabled(False)
        self.screenshotBtn.clicked.connect(self.save_screenshot)
        self.stopDetectBtn = QtWidgets.QPushButton('🛑Stop')
        self.stopDetectBtn.setFixedSize(100, 50)
        self.stopDetectBtn.setEnabled(False)
        self.stopDetectBtn.clicked.connect(self.stop_detect)
        self.exitBtn = QtWidgets.QPushButton('⏹Exit')
        self.exitBtn.setFixedSize(100, 50)
        self.exitBtn.clicked.connect(self.close)
        btnLayout.addWidget(self.selectModel)
        btnLayout.addWidget(self.openVideoBtn)
        btnLayout.addWidget(self.openCamBtn)
        btnLayout.addWidget(self.pauseBtn)
        btnLayout.addWidget(self.stopDetectBtn)
        btnLayout.addWidget(self.screenshotBtn)
        btnLayout.addWidget(self.exitBtn)
        bottomLayout.addLayout(btnLayout)
 
    def start_camera(self):
        self.timer1.stop()

        available_cameras = []
        for i in range(10): 
            cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
            if cap.isOpened():
                available_cameras.append(f"Camera {i}")
                cap.release()

        if not available_cameras:
            QtWidgets.QMessageBox.warning(self, "Warning", "No available cameras found!")
            return

        cam_index, ok = QtWidgets.QInputDialog.getItem(self, "Select Camera", 
                                                    "Choose a camera:", available_cameras, 0, False)
        
        if not ok:  
            return

        selected_camera = int(cam_index.split()[-1])  
        self.cap = cv2.VideoCapture(selected_camera, cv2.CAP_DSHOW)

        if self.cap.isOpened():
            self.timer.start(50)
            self.screenshotBtn.setEnabled(True)  
            self.stopDetectBtn.setEnabled(True)
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Failed to open the selected camera!")

 
    def camera_show(self):
        ret, frame = self.cap.read()
        if ret:
            if self.model is not None:
                frame = cv2.resize(frame, (448, 352))
                frame1 = self.model(frame, imgsz=[448, 352], device='cuda') if torch.cuda.is_available() \
                    else self.model(frame, imgsz=[448, 352], device='cpu')
                frame1 = cv2.cvtColor(frame1[0].plot(), cv2.COLOR_RGB2BGR)
                frame1 = QtGui.QImage(frame1.data, frame1.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
                self.detectlabel.setPixmap(QtGui.QPixmap.fromImage(frame1))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            self.oriVideoLabel.setPixmap(QtGui.QPixmap.fromImage(frame))
            self.oriVideoLabel.setScaledContents(True)
        else:
            pass
 
    def start_video(self):
        if self.timer.isActive():
            self.timer.stop()
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "Select Video", filter='*.mp4 *.avi *.mov *.mkv')
        if os.path.isfile(fileName):
            self.video = cv2.VideoCapture(fileName)
            fps = self.video.get(cv2.CAP_PROP_FPS)
            self.timer1.start(int(1/fps))
            self.screenshotBtn.setEnabled(True)  # Allow Screen Shot
        else:
            print("Reselect video")
 
    def video_show(self):
        ret, frame = self.video.read()
        if ret:
            if self.model is not None:
                frame = cv2.resize(frame, (448, 352))
                frame1 = self.model(frame, imgsz=[448, 352], device='cuda') if torch.cuda.is_available() \
                    else self.model(frame, imgsz=[448, 352], device='cpu')
                frame1 = cv2.cvtColor(frame1[0].plot(), cv2.COLOR_RGB2BGR)
                frame1 = QtGui.QImage(frame1.data, frame1.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
                self.detectlabel.setPixmap(QtGui.QPixmap.fromImage(frame1))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            self.oriVideoLabel.setPixmap(QtGui.QPixmap.fromImage(frame))
            self.oriVideoLabel.setScaledContents(True)
        else:
            self.timer1.stop()
            img = cv2.cvtColor(np.zeros((500, 500), np.uint8), cv2.COLOR_BGR2RGB)
            img = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888)
            self.oriVideoLabel.setPixmap(QtGui.QPixmap.fromImage(img))
            self.detectlabel.setPixmap(QtGui.QPixmap.fromImage(img))
            self.video.release()
            self.video = None
 
    def load_model(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "Select model weights", filter='*.pt')
        if fileName.endswith('.pt'):
            self.model = YOLO(fileName)
        else:
            print("Reselect model")
 
        self.openVideoBtn.setEnabled(True)
        self.stopDetectBtn.setEnabled(True)

    def pause_resume(self):
        # Camera Mode
        if self.cap is not None:
            if self.timer.isActive():  # Pause Camera
                self.timer.stop()
                self.pauseBtn.setText("▶️ Play")
            else:  
                self.timer.start(50)
                self.pauseBtn.setText("⏸️ Pause")
            return

        # Video Mode
        if self.video is not None:
            if self.timer1.isActive():  # Pause Video
                self.timer1.stop()
                self.pauseBtn.setText("▶️ Play")
            else:  
                fps = self.video.get(cv2.CAP_PROP_FPS) or 25
                self.timer1.start(int(1000 / fps))  # restart timer
                self.pauseBtn.setText("⏸️ Pause")

    def save_screenshot(self):
        if self.detectlabel.pixmap() is None:
            QtWidgets.QMessageBox.warning(self, "Warning! ", "There are currently no detection screen!")
            return

        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save Screenshot", "", "PNG (*.png);;JPEG (*.jpg)"
        )

        if file_path:
            self.detectlabel.pixmap().save(file_path)
            QtWidgets.QMessageBox.information(self, "Successfully! ", "The screenshot has been saved!")


 
    def stop_detect(self):
        if self.timer.isActive():
            self.timer.stop()
        if self.timer1.isActive():
            self.timer1.stop()
        if self.cap is not None:
            self.cap.release()
            self.cap = None
        self.video = None
        self.screenshotBtn.setEnabled(False)  
        img = cv2.cvtColor(np.zeros((500, 500), np.uint8), cv2.COLOR_BGR2RGB)
        img = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888)
        self.oriVideoLabel.setPixmap(QtGui.QPixmap.fromImage(img))
        self.detectlabel.setPixmap(QtGui.QPixmap.fromImage(img))

    
 
    def close(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None
        if self.timer.isActive():
            self.timer.stop()
        exit()
 
 
if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MyWindow()
    window.show()
    app.exec()