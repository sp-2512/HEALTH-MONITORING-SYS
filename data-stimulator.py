import random

def simulate_health_data():
    return {
        "age": random.randint(20, 80),
        "weight": random.randint(50, 100),
        "height": random.randint(150, 200),
        "heart_rate": random.randint(60, 130),
        "bp_systolic": random.randint(90, 180),
        "bp_diastolic": random.randint(60, 120),
        "oxygen_level": random.randint(90, 100)
    }
