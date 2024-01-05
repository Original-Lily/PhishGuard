import pandas as pd
import sys

def update_email_text(input_file_path, output_file_path, user_input):
    # Read existing data
    df = pd.read_csv(input_file_path)

    # Find the index of the last row
    last_row_index = df.index[-1]

    # Replace the contents of the 'Email Text' cell in the last row with the user input
    df.at[last_row_index, 'Email Text'] = user_input

    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_file_path, index=False)

    print(f"Data with user input saved to: {output_file_path}")

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: usrInput.py <UserInput>")
        sys.exit(1)

    user_input = sys.argv[1]
    print(user_input)

    # Specify the input and output file paths
    input_file_path = 'Archive/Phishing_Email.csv'
    output_file_path = 'Phishing_Email_with_Input.csv'

    # Update the email text in the DataFrame and save to a new CSV file
    update_email_text(input_file_path, output_file_path, user_input)

if __name__ == "__main__":
    main()
