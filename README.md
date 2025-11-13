# Garage Gate ANPR

This repository contains the code and resources for the Garage Gate Automatic Number Plate Recognition (ANPR) system.

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

