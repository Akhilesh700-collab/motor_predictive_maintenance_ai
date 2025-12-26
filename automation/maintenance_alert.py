def maintenance_action(status):
    if status == "FAULT_PREDICTED":
        print("🚨 MAINTENANCE ALERT: Potential Motor Failure Detected")
        print("✔ Recommendation: Inspect bearings and reduce load")
    else:
        print("✅ Motor operating normally")
