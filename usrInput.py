import pandas as pd

# Read existing data
input_file_path = 'Archive/Phishing_Email.csv'
df = pd.read_csv(input_file_path)

# Get user input for a new email
user_input = input("Enter the email text: ")

# Find the index of the last row
last_row_index = df.index[-1]

# Replace the contents of the 'Email Text' cell in the last row with the user input
df.at[last_row_index, 'Email Text'] = user_input

# Save the updated DataFrame to a new CSV file
output_file_path = 'Phishing_Email_with_Input.csv'
df.to_csv(output_file_path, index=False)

print(f"Data with user input saved to: {output_file_path}")
