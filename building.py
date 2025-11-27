class Building:
    def __init__(self, building_id, name, address):
        self.building_id = building_id
        self.name = name
        self.address = address
        self.readings = []

    def add_reading(self, reading):
        self.readings.append(reading)

    def total_consumption(self):
        total = 0
        for r in self.readings:
            total += r.consumption
        return total

    def monthly_consumption(self):
        monthly = {}
        for r in self.readings:
            month = r.date[:7]  # "YYYY-MM"
            if month not in monthly:
                monthly[month] = 0
            monthly[month] += r.consumption
        return monthly

    def summary(self):
        return {
            "building": self.name,
            "total_consumption": self.total_consumption()
        }
