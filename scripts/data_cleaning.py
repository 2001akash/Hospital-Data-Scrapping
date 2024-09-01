import pandas as pd
import re

# Function to clean text data
def clean_text(text):
    """Clean text by removing special characters and extra spaces."""
    if pd.isna(text):
        return ""
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters (except spaces and alphanumeric)
    return text.strip()  # Remove leading and trailing spaces

def clean_data(input_file, output_file):
    """Load, clean, and save the data."""
    try:
        # Load the scraped data
        df = pd.read_csv(input_file)
        
        # Check if DataFrame is empty
        if df.empty:
            print(f"No data found in the file: {input_file}")
            return
        
        # Display the first few rows of the DataFrame for initial inspection
        print("Initial data preview:")
        print(df.head())

        # Clean relevant columns
        for column in ['name', 'specialty', 'department']:  # Adjust column names as needed
            if column in df.columns:
                df[column] = df[column].apply(clean_text)
        
        # Drop duplicates
        df.drop_duplicates(inplace=True)
        
        # Optional: Handle missing values
        df.fillna('', inplace=True)  # Replace NaN values with empty strings
        
        # Display the cleaned data preview
        print("Cleaned data preview:")
        print(df.head())
        
        # Save the cleaned data
        df.to_csv(output_file, index=False)
        print(f"Cleaned data saved to {output_file}")

    except Exception as e:
        print(f"An error occurred while cleaning the data: {e}")

# Main execution
if __name__ == "__main__":
    input_file = 'hospital_data.csv'  # Path to the collected data file
    output_file = 'cleaned_hospital_data.csv'  # Path to save the cleaned data
    clean_data(input_file, output_file)
