# II – NFC Attendance System

This project uses a **Raspberry Pi Zero** with an **NFC MODULE V3** to read the UIDs from **PICC cards**. It then updates an `.xlsx` file to track student attendance. 

## Installation

Follow these steps to set up the project:

### Download the source code  
Clone the repository or download it manually:

```sh
git clone https://github.com/SebastianOrozcoMartinez/II.git
cd II
```

### Install dependencies  
Run the following command to install the required Python libraries:

```sh
pip install openpyxl adafruit-circuitpython-pn532
```
 
Before running the program, you need to set up the students in `ii.xlsx`:

- Open **`ii.xlsx`** in Excel
- Enter **each student's name**, **classroom**, and **UID**.
- Make sure that each **classroom name matches** the corresponding sheet name in the `.xlsx` file.

## Requirements

- Raspberry Pi Zero
- NFC MODULE V3
- Python 3.x
- PICC-compatible NFC cards