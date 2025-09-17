<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d00df609-a633-4c72-b18f-c4f09d5f9d4d" />

# Face Mesh Module (OpenCV + MediaPipe)

This project is a simple **Face Mesh detector** using [MediaPipe](https://developers.google.com/mediapipe) and [OpenCV](https://opencv.org/).  
It captures real-time video from your webcam, detects up to **2 faces**, and draws the full **468-point face mesh** on the frame.  
Each landmark’s pixel coordinates are also printed in the console.

---

## 📌 Features
- Real-time face mesh detection (468 landmarks per face).
- Supports multiple faces (default: 2).
- Draws tessellation mesh with adjustable drawing specifications.
- Prints landmark coordinates `(id, x, y)` in pixels.
- Displays FPS counter on screen.

---

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/karmat-1/Face-Mesh.git
   cd FaceMeshModule
   ```
2. Install Dependencies
   ```bash
   pip install opencv-python mediapipe
   ```
3. Usage
   ```py
   from FaceMeshModule import run_face_mesh

   run_face_mesh()
   ```
