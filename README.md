# 🚦 Intelligent Traffic System for Urban Conditions

Real-time vehicle tracking and congestion analysis using **YOLOv8 + DeepSORT**, built with Python and OpenCV.

---

## 🎯 Features

- ✅ Real-time vehicle detection (car, bus, truck, bike)
- ✅ Object tracking with unique IDs using DeepSORT
- ✅ Congestion level estimation (Low / Medium / High)
- ✅ CSV logging for traffic data
- ✅ Modular and ready for live camera feeds

---

## 🧠 Tech Stack

- **Language**: Python 3.10  
- **Detection**: YOLOv8 (`ultralytics`)  
- **Tracking**: DeepSORT (`deep-sort-realtime`)  
- **Video Processing**: OpenCV  
- **IDE**: PyCharm

---

## 📂 Project Structure

INTELLIGENT_TRAFFIC_SYSTEM/

│

├── data/ # Video input folder

├── output/ # Output logs and results

├── models/ # (Optional: custom models)

├── main.py # Main code (detection + tracking)

├── requirements.txt # All dependencies

└── README.md

---

## 🚀 Run the Project

1. Clone the repo:

   git clone https://github.com/MaazHussain2711/INTELLIGENT_TRAFFIC_SYSTEM.git

   cd INTELLIGENT_TRAFFIC_SYSTEM

3. Create virtual environment:

python -m venv .venv

.venv\Scripts\activate  # Windows

3. Install requirements:
pip install -r requirements.txt

Add your video to data/ folder and run:

python main.py

---

## 📊 Output

- Real-time vehicle tracking with ID overlay

- Congestion level displayed on frame

- Logs stored in output/traffic_log.csv

---

## 👨‍💻 Author
Maaz Hussain
GitHub

---

## 🏁 Future Goals

- Smart traffic signal control

- GPS-based traffic clustering

- Web dashboard with live stats
