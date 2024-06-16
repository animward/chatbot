import re
import hashlib
import os

def clean_text(input_folder, output_folder, input_filename, output_filename):
    # Construct file paths
    input_file_path = os.path.join(input_folder, input_filename)
    output_file_path = os.path.join(output_folder, output_filename)
    
    # Read data from input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    
    # Normalize whitespace and strip leading/trailing whitespace
    data_cleaned = re.sub(r'\s+', ' ', data).strip()
    
    # Only keep basic punctuation
    data_cleaned = re.sub(r'[^a-zA-Z0-9\s.,!?\'"-]', '', data_cleaned)
    
    # Normalize text to lowercase
    data_cleaned = data_cleaned.lower()
    
    # Handle duplicates
    seen = set()
    unique_lines = []
    for line in data_cleaned.split('.'):
        line = line.strip()
        if line:
            hash_value = hashlib.md5(line.encode()).hexdigest()
            if hash_value not in seen:
                seen.add(hash_value)
                unique_lines.append(line)
    
    # Back to single string
    data_cleaned = '. '.join(unique_lines) + '.'
    
    # Write cleaned data to output file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(data_cleaned)
    
    # Print a shorter and more comprehensive message
    print(f"Text has been cleaned and saved to '{os.path.relpath(output_file_path, start=os.getcwd())}'")

# Example usage
base_folder = os.path.join(os.path.dirname(__file__), '..', 'data')
input_folder = os.path.join(base_folder, 'input')
output_folder = os.path.join(base_folder, 'output')
input_filename = 'example_data.txt'
output_filename = 'output_cleaned.txt'

# Ensure the output directory exists
os.makedirs(output_folder, exist_ok=True)

clean_text(input_folder, output_folder, input_filename, output_filename)
