class MeterReading:
    def __init__(self, building_id, date, consumption):
        self.building_id = building_id
        self.date = date
        self.consumption = float(consumption)
