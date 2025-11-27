import pandas as pd
import matplotlib.pyplot as plt
from building import Building
from meter import MeterReading

def load_buildings(path):
    df = pd.read_csv(path)
    buildings = {}

    for _, row in df.iterrows():
        b = Building(row['building_id'], row['name'], row['address'])
        buildings[row['building_id']] = b
    return buildings

def load_readings(path, buildings):
    df = pd.read_csv(path)

    for _, row in df.iterrows():
        r = MeterReading(row['building_id'], row['date'], row['consumption'])
        if row['building_id'] in buildings:
            buildings[row['building_id']].add_reading(r)

def generate_summary(buildings):
    rows = []
    for bid, b in buildings.items():
        rows.append(b.summary())
    summary_df = pd.DataFrame(rows)
    summary_df.to_csv("outputs/summary.csv", index=False)
    return summary_df

def generate_dashboard(summary_df):
    plt.figure(figsize=(8,5))
    plt.bar(summary_df['building'], summary_df['total_consumption'])
    plt.title("Total Consumption by Building")
    plt.xlabel("Building")
    plt.ylabel("Consumption")
    plt.tight_layout()
    plt.savefig("outputs/dashboard.png")
    plt.close()

def generate_report(summary_df):
    with open("outputs/report.md", "w") as f:
        f.write("# Resource Monitoring Report\n\n")
        f.write("This report shows the total consumption of each building.\n\n")

        for _, row in summary_df.iterrows():
            f.write(f"- **{row['building']}**: {row['total_consumption']}\n")

if __name__ == "__main__":
    buildings = load_buildings("data/building_data.csv")
    load_readings("data/meter_readings.csv", buildings)

    summary = generate_summary(buildings)
    generate_dashboard(summary)
    generate_report(summary)

    print("All tasks completed. Check the outputs folder.")
