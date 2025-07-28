# 🎥 Motion Detection Security Camera using Python & OpenCV

This project is a simple yet powerful **motion detection security system** built using **Python** and **OpenCV**, designed to work with **macOS**. It captures live webcam feed, detects motion in real-time, and plays a custom alert sound when movement is detected.

---

## 🛠 Features

- ✅ Real-time video feed from your laptop’s camera  
- ✅ Motion detection using frame differencing and contour detection  
- ✅ Alert sound plays upon detecting movement (macOS `afplay` support)  
- ✅ Cooldown system to prevent repeated alerts  
- ✅ Cross-platform logic with minimal setup

---

## 🎬 Demo

Click the image below to watch the full demo on YouTube:

[![Motion Detection Demo](https://img.youtube.com/vi/LNJoPAhTtmU/0.jpg)](https://www.youtube.com/watch?v=LNJoPAhTtmU)

---

## 📁 Project Structure

```bash
.
├── Audio/
│   └── alert.wav         # Custom audio file played when motion is detected
├── motion_detector.py    # Main Python script
└── README.md             # Documentation
```

⸻

🚀 How It Works
1. Capture Frames: Continuously grabs two frames from the webcam.
2.	Detect Motion: Finds differences using image subtraction, then converts to grayscale, applies blur, and thresholds.
3.	Highlight Movement: Uses contour detection to draw boxes around moving objects.
4.	Play Alert: Plays a sound using afplay when motion is detected, with a cooldown to reduce noise.

⸻

🎧 Sound Configuration (macOS Only)

Place your .wav file inside the Audio/ directory and ensure the path in the script matches:

subprocess.Popen(['afplay', './Audio/alert.wav'])


⸻

⏬ Requirements
	•	Python 3.10+ or 3.13 (both compatible)
	•	OpenCV

📦 Install Dependencies
```
pip install opencv-python
```

⸻

▶️ Run the Program
```
python motion_detector.py
```
```
Press q to exit the video feed.
```
⸻

💻 Platform
- ✅ Tested on macOS Sonoma
- ❗ Will need modification for Windows/Linux (e.g., use playsound or winsound instead of afplay)

⸻


📜 License

This project is open-source and free to use under the MIT License.

⸻

🙌 Credits

Developed by Abdullah Nazmus-Sakib

⸻

📩 Feedback or Suggestions?

Feel free to open an issue or drop a message!

---
