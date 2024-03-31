import pandas as pd

def read_csv_to_dict(csv_filename):
    """
    Reads a CSV file and returns its content as a dictionary.
    Assumes that the CSV has two columns: the first column as keys and the second column as values.
    """
    data_dict = {}
    try:
        df = pd.read_csv(csv_filename)
        data_dict = dict(zip(df.iloc[:, 0], df.iloc[:, 1]))
    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
    return data_dict

# Example usage:
csv_filename = 'fire risk by county.csv'  # Replace with your actual CSV filename
my_dict = read_csv_to_dict(csv_filename)
print(my_dict)
