# Test Report Generator 🔬

A Python command-line application that validates
multi-parameter sensor readings and generates
professional test reports.

## Features
- Multi-parameter testing (Voltage, Current, Temperature)
- Pass/Fail logic with spec limits
- FPY (First Pass Yield) calculation
- Timestamped CSV report — opens in Excel
- Formatted TXT report
- Error handling & input validation
- OOP design — clean & maintainable

## Tech Stack
- Python 3.12+
- OOP — Classes & Inheritance
- File I/O — CSV & TXT
- Error Handling

## How To Run
```bash
cd test_report_generator
python main.py
```

## Spec Limits
| Parameter | LSL | USL |
|-----------|-----|-----|
| Voltage   | 4.5V | 5.5V |
| Current   | 0.8A | 1.2A |
| Temperature | 20°C | 35°C |

## Sample Output

==================================================
       FUNCTIONAL TEST REPORT
==================================================
Date     : 2026-06-06 17:22:24
Product  : BATTERY
Station  : BATT-001
Operator : AMIR ASYRAFF
Spec V   : 4.5V - 5.5V
Spec I   : 0.8A - 1.2A
Spec T   : 20C - 35C
--------------------------------------------------
Unit  Volt    Curr    Temp    Status  Reason
--------------------------------------------------
1     5.0     1.1     28.0    PASS    
2     4.3     1.2     28.0    FAIL    Volt_LOW
3     5.1     0.9     36.0    FAIL    Temp_HIGH
4     5.0     1.3     27.0    FAIL    Curr_HIGH
5     4.5     1.0     25.0    PASS    
--------------------------------------------------
TOTAL    : 5 units
PASS     : 2 units
FAIL     : 3 units
FPY      : 40.0%
--------------------------------------------------
STATISTICS:
Volt Max : 5.1V
Volt Min : 4.3V
Volt Avg : 4.78V
Curr Max : 1.3A
Curr Min : 0.9A
Curr Avg : 1.10A
==================================================

## AUTHOR
MUHAMMAD HAFIZUL BIN AHMAD HUSNI