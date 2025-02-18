# II

This project uses a Raspberry Pi Zero with an NFC MODULE V3 to get the UIDs from the PICCs. It then edits an `.xlsx` file for the attendance of students.

## Installation

First, download the source code, then install the following packages:

```sh
pip install openpyxl adafruit-circuitpython-pn532
```

Then, you need to configure the students. For this, you need to open `ii.xlsx` and write the name of every student. Then, you'll write their classrooms and UIDs. Make sure that the name of the classroom is the same as the classroom's unique page on the `.xlsx` file.