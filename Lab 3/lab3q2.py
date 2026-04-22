
def railway_agent(train_sensor, obstacle_sensor, emergency):

   
    if emergency == "Active":
        return {
            "Gate": "Lower",
            "Siren": "On",
            "Train_Signal": "Red"
        }

    
    if train_sensor == "Detected" and obstacle_sensor == "Stuck":
        return {
            "Gate": "Lower",
            "Siren": "On",
            "Train_Signal": "Red"
        }

    
    if train_sensor == "Detected" and obstacle_sensor == "Clear":
        return {
            "Gate": "Lower",
            "Siren": "On",
            "Train_Signal": "Green"
        }

    if train_sensor == "NotDetected":
        return {
            "Gate": "Raise",
            "Siren": "Off",
            "Train_Signal": "Green"
        }


test_cases = [
    ("Detected", "Clear", "Neutral"),
    ("Detected", "Stuck", "Neutral"),
    ("NotDetected", "Clear", "Neutral"),
    ("Detected", "Clear", "Active")
]

print("Percept (Train, Obstacle, Emergency) -> Action")

for case in test_cases:
    action = railway_agent(case[0], case[1], case[2])
    print(case, "->", action)
