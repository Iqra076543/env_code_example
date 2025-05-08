def report_status(stations, threshold):
    for station in stations:
        id, pm25 = station
        if pm25 < threshold:
            status = "safe"
        else:
            status = "Danger"
        print(f"{id} {pm25} µg/m³ ({status})")

stations = [
    ['A1', 62],
    ['B5', 97],
    ['C3', 155]
]

report_status(stations, 100)
