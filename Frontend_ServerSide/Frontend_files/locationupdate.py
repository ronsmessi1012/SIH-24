import json
import random
import time

# Define latitude and longitude boundaries for each continent
continent_boundaries = {
    'Asia': {'lat_min': 1.0, 'lat_max': 80.0, 'lon_min': 60.0, 'lon_max': 180.0},
    'North America': {'lat_min': 10.0, 'lat_max': 80.0, 'lon_min': -180.0, 'lon_max': -60.0},
    'South America': {'lat_min': -60.0, 'lat_max': 15.0, 'lon_min': -80.0, 'lon_max': -35.0},
    'Europe': {'lat_min': 35.0, 'lat_max': 71.0, 'lon_min': -30.0, 'lon_max': 60.0},
    'Africa': {'lat_min': -37.0, 'lat_max': 37.0, 'lon_min': -20.0, 'lon_max': 60.0},
    'Australia': {'lat_min': -44.0, 'lat_max': -10.0, 'lon_min': 112.0, 'lon_max': 155.0},
    'Antarctica': {'lat_min': -90.0, 'lat_max': -60.0, 'lon_min': -180.0, 'lon_max': 180.0}
}

# Map of reference numbers to continents
reference_to_continent = {
    'REF123': 'Asia',        # Example: New Delhi -> Asia
    'REF456': 'North America',  # Example: New York -> North America
    'REF789': 'Europe',      # Example: London -> Europe
}

# Function to generate random coordinates within the specified continent
def get_random_coordinates_for_continent(continent):
    boundaries = continent_boundaries.get(continent)
    
    if boundaries:
        latitude = random.uniform(boundaries['lat_min'], boundaries['lat_max'])
        longitude = random.uniform(boundaries['lon_min'], boundaries['lon_max'])
        return latitude, longitude
    else:
        print(f"Invalid continent: {continent}")
        return None, None

# Load the existing JSON data
def load_locations(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return []

# Save updated JSON data back to the file
def save_locations(file_path, locations):
    with open(file_path, 'w') as file:
        json.dump(locations, file, indent=4)

# Update the coordinates of all locations based on their continent
def update_location_data(locations):
    for location in locations:
        reference_number = location['reference_number']
        continent = reference_to_continent.get(reference_number)

        if continent:
            # Get random coordinates for the location's continent
            new_lat, new_lon = get_random_coordinates_for_continent(continent)

            if new_lat and new_lon:
                location['latitude'] = new_lat
                location['longitude'] = new_lon
                print(f"Updated {reference_number} to new coordinates: ({new_lat}, {new_lon})")
        else:
            print(f"Continent not found for {reference_number}")

    return locations

# Main function to periodically update the locations
def periodic_update(file_path, interval_seconds=5):
    while True:
        # Load the existing locations
        locations = load_locations(file_path)
        
        if locations:
            # Update the location data with new random coordinates within the same continent
            updated_locations = update_location_data(locations)
            
            # Save the updated data back to the JSON file
            save_locations(file_path, updated_locations)
        
        # Wait for the next update
        time.sleep(interval_seconds)

# Run the script
if __name__ == '__main__':
    locations_file = 'locations.json'  # Path to the JSON file
    periodic_update(locations_file, interval_seconds=5)  # Update every 5 seconds
