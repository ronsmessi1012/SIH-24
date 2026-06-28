import simpy
import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()

# Parameters
SIMULATION_DAYS = 180  # Number of days to simulate
DELIVERY_HOURS = [(9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18)]
REGIONS = ['Central', 'North', 'South', 'East', 'West']
TRAFFIC_PATTERNS = ['Light', 'Moderate', 'Heavy', 'Peak']

# Define Kolkata-specific area pincodes and their distances from the nearest post office
PINCODE_DISTANCE_MAPPING = {
    '700001': 2.0,
    '700002': 2.5,
    '700003': 2.5,
    '700004': 2.5,
    '700005': 4.0,
    '700006': 5.0,
    '700007': 5.5,
    '700008': 3.5,
    '700009': 6.0,
    '700010': 2.0,
    '700011': 7.0,
    '700012': 4.0,
    '700013': 5.5,
    '700014': 4.0,
    '700015': 4.5,
    '700016': 5.0,
    '700017': 6.0,
    '700018': 6.0,
    '700019': 6.5,
    '700020': 4.5,
    # Add more pincodes and distances as needed
}

# Helper function to determine traffic pattern based on time slot
def determine_traffic_pattern(hour):
    if 9 <= hour < 12:
        return np.random.choice(['Moderate', 'Heavy', 'Peak'], p=[0.2, 0.5, 0.3])
    elif 12 <= hour < 15:
        return np.random.choice(['Light', 'Moderate'], p=[0.4, 0.6])
    else:
        return np.random.choice(['Light', 'Moderate'], p=[0.6, 0.4])

# Helper function to generate delivery data
def generate_delivery_data(env, user_id, deliveries, pincode, customer_name):
    failed_count = 0
    while True:
        timestamp = env.now
        hour = timestamp % 24
        time_slot = DELIVERY_HOURS[np.random.randint(0, len(DELIVERY_HOURS))]
        region = np.random.choice(REGIONS)
        traffic = determine_traffic_pattern(hour)
        if failed_count > 0:
            success = 1
            failed_count = 0
        else:
            success = np.random.choice([0, 1], p=[0.3, 0.7])
            if success == 0:
                failed_count += 1
        deliveries.append({
            'Timestamp': timestamp,
            'UserID': user_id,
            'Customer Name': customer_name,
            'Area Pincode': pincode,
            'Distance from Nearest Postal Service': PINCODE_DISTANCE_MAPPING.get(pincode, 10.0),
            'Time Slot': f"{time_slot[0]:02d}:00-{time_slot[1]:02d}:00",
            'Traffic Pattern': traffic,
            'Region': region,
            'Success Indicator': success,
            'User Rating': np.random.randint(0, 6) if success == 1 else 0
        })
        # Generate next delivery in a random interval
        yield env.timeout(np.random.uniform(1, 24))

# Initialize environment
env = simpy.Environment()
deliveries = []

# Create a subset of users for demonstration purposes
user_ids = [f'UID{str(i).zfill(6)}' for i in range(1000)]  # Use fewer users to avoid memory issues

# Assign each user a fixed pincode and a consistent name
pincodes = list(PINCODE_DISTANCE_MAPPING.keys())
user_data = {}
for user_id in user_ids:
    pincode = np.random.choice(pincodes)  # Randomly assign a pincode
    customer_name = fake.name()  # Generate a unique name for each user
    user_data[user_id] = {'pincode': pincode, 'customer_name': customer_name}
    env.process(generate_delivery_data(env, user_id, deliveries, pincode, customer_name))

# Run simulation
env.run(until=SIMULATION_DAYS * 24)  # Running for 180 days

# Convert to DataFrame
df = pd.DataFrame(deliveries)

# Convert 'Timestamp' to readable date format
df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='h', origin=pd.Timestamp('2024-04-01'))

# Print the shape of the generated data
print(f"Shape of the generated data: {df.shape}")

# Save to CSV
csv_file_path = 'delivery_data.csv'
try:
    df.to_csv(csv_file_path, index=False)
    print(f"Data successfully saved to '{csv_file_path}'.")
except Exception as e:
    print(f"An error occurred while saving the CSV file: {e}")
