import csv
import random
import time

def generate_motor_data():
    temperature = round(random.uniform(50, 100), 2)
    vibration = round(random.uniform(0.5, 5.0), 2)
    current = round(random.uniform(5, 20), 2)
    return temperature, vibration, current

with open("data/motor_sensor_data.csv", "a", newline="") as file:
    writer = csv.writer(file)

    while True:
        data = generate_motor_data()
        writer.writerow(data)
        print("Motor Data:", data)
        time.sleep(2)
