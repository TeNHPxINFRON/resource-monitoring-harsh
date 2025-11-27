# Resource Monitoring Project

This project reads building details and their meter readings, then calculates
the total consumption and monthly usage. It also creates a simple bar chart
dashboard and a summary report.

## How to Run

1. Install requirements:
   pip install -r requirements.txt

2. Run main script:
   python src/main.py

3. Check the "outputs" folder for:
   - summary.csv
   - dashboard.png
   - report.md

## Files
- building.py: Building class
- meter.py: MeterReading class
- main.py: Main logic
- building_data.csv: Building info
- meter_readings.csv: Consumption data
