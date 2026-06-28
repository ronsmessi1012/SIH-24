import pandas as pd
from collections import Counter
from sklearn.preprocessing import LabelEncoder

# Step 1: Load the dataset
file_path = r"C:\Users\HP\Desktop\SIH APP\indiapostapp\backend\user_dataset_india_with_timeslots_2.csv"
data = pd.read_csv(file_path)

# Step 2: Inspect the columns to ensure correct column names
data.columns = data.columns.str.strip()  # Remove extra spaces from column names

# Step 3: Convert time slots into numerical categories (if needed)
# Encode the 'Time Slot' column using LabelEncoder
if 'Time Slot' in data.columns:
    label_encoder_time = LabelEncoder()
    data['Time_Slot_Encoded'] = label_encoder_time.fit_transform(data['Time Slot'])
else:
    print("Required column 'Time Slot' does not exist in the dataset. Please check the column names.")

# Step 4: Calculate the success rate for each time slot per user
# Group by 'Name' and 'Time Slot' to calculate the delivery success rate
time_slot_success_rate = data.groupby(['Name', 'Time Slot'])['Delivery Successful'].mean().reset_index()

# Step 5: Find the time slot with the highest success rate for each user
user_successful_time_slot = time_slot_success_rate.loc[time_slot_success_rate.groupby('Name')['Delivery Successful'].idxmax()]

# Rename columns for clarity
user_successful_time_slot.columns = ['Name', 'Most_Successful_Time_Slot', 'Success_Rate']

# Step 6: Prepare the prediction function to get ETA based on user name
def get_ETA(user_name):
    # Check if the entered user name exists in the dataset
    if user_name not in data['Name'].values:
        return f"User '{user_name}' not found in the dataset. Please enter a valid user name."
    
    # Display the count of time slots and their success rates for the user
    user_data = time_slot_success_rate[time_slot_success_rate['Name'] == user_name]  # Get all rows for the selected user
    print(f"Time Slot Success Rates for {user_name}:")
    for time_slot, success_rate in zip(user_data['Time Slot'], user_data['Delivery Successful']):
        print(f"{time_slot}: {success_rate * 100:.2f}% success rate")
    
    # Get the most successful time slot for the user
    most_successful_time_slot = user_successful_time_slot[user_successful_time_slot['Name'] == user_name]['Most_Successful_Time_Slot'].values[0]
    
    return most_successful_time_slot

# Step 7: Take user input dynamically
user_name = input("Enter the user name to predict their most successful time slot: ")  # Get user input at runtime
predicted_eta = get_ETA(user_name)
print(f"Predicted most successful time slot for {user_name}: {predicted_eta}")
