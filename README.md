# Garage Gate ANPR

![tap image](https://github.com/AhmedMostafa3m/garage-gate-anpr/blob/5cf15d812d24d267ca93d2b6311554ee4f561819/static/Raspberry_pi_Servo_Wiring_Diagram.png)

This repository contains the code and resources for the Garage Gate Automatic Number Plate Recognition (ANPR) system.
```
garage-system/
├── app/
│   ├── anpr.py           # License plate recognition logic
│   ├── controller.py     # Gate control logic with Raspberry Pi GPIO
│   ├── database.py       # Handles the SQLite database for authorized plates
│   ├── main.py           # Entry point of the application
│   ├── config.py         # Configuration file with settings for GPIO, etc.
│   └── utils/            # Helper utilities (e.g., image preprocessing)
├── static/
│   ├── wiring-diagram.png # Hardware wiring diagram
├── requirements.txt      # Python dependencies.
├── README.md             # Installation and usage documentation
└── .gitignore            # Prevent sensitive or unnecessary files from being tracked.
```
# 🚗 Garage Access Control System

A Raspberry Pi-based automatic gate system using license plate recognition (ANPR).

## 🧱 Project Structure
See the `/app` directory for core components:
- `anpr.py`: Detects license plates using OpenCV.
- `controller.py`: Controls the servo motor for the gate.
- `database.py`: Stores authorized license plates (SQLite).
- `main.py`: Entry point — integrates all modules.
- `utils/`: Image preprocessing helpers.

Key Features

✅ OpenCV Haar Cascade detects license plate regions.

✅ EasyOCR reads plate text automatically.

✅ Text cleaning removes noise and formats plates (e.g. ABC1234).

✅ Returns both the annotated image and recognized plate numbers for easy use in main.py.

✅ Runs standalone for quick testing with any image.

✅ Automatic OCR integration
* Uses LicensePlateRecognizer.recognize_plate() which returns both the annotated image and detected plate texts.\n
✅ Multi-plate handling\n
* If multiple plates are detected (e.g., nearby cars), each one is checked against the database.\n
* The gate opens immediately once one plate matches an authorized entry.
✅ Console logging\n
* Clear feedback at every stage of the process for easier debugging and monitoring.\n

## ⚙️ Setup
```bash
git clone https://github.com/yourusername/garage-system.git
cd garage-system
pip install -r requirements.txt

▶️ Run
```
python app/main.py
```
🧩 Hardware

See static/wiring-diagram.png for servo and GPIO connections.

