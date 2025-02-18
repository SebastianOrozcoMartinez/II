# 📡 II – NFC Attendance System

This project uses a **Raspberry Pi Zero** with an **NFC MODULE V3** to read the UIDs from **PICC cards**. It then updates an `.xlsx` file to track student attendance. 📋✅

## 🚀 Installation

Follow these steps to set up the project:

### 1️⃣ Download the source code  
Clone the repository or download it manually:

```sh
git clone https://github.com/SebastianOrozcoMartinez/II.git
cd II
```

### 2️⃣ Install dependencies  
Run the following command to install the required Python libraries:

```sh
pip install openpyxl adafruit-circuitpython-pn532
```

### 3️⃣ Configure students  
Before running the program, you need to set up the students in `ii.xlsx`:

- Open **`ii.xlsx`** in Excel or any spreadsheet editor.
- Enter **each student's name**, **classroom**, and **UID**.
- Ensure that each **classroom name matches** the corresponding sheet name in the `.xlsx` file.

## 📖 Usage

Run the script to start reading NFC cards and updating attendance records:

```sh
python main.py
```

When a student scans their card, their attendance will be marked automatically.

## 🛠️ Requirements

- Raspberry Pi Zero
- NFC MODULE V3
- Python 3.x
- PICC-compatible NFC cards

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for more details.
