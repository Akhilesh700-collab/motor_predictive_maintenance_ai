import sys
import os
sys.path.append("ml")
sys.path.append("automation")

from fault_prediction_model import predict_fault
from maintenance_alert import maintenance_action

def main():
    print("\nAI-Based Motor Predictive Maintenance System\n")

    status, data = predict_fault()

    print(f"Temperature: {data['temperature']} °C")
    print(f"Vibration: {data['vibration']} mm/s")
    print(f"Current: {data['current']} A")
    print(f"System Status: {status}")

    maintenance_action(status)

if __name__ == "__main__":
    main()
