import re

def clean_line(line):
    # Use regular expressions to remove numbers and percentages
    cleaned_line = re.sub(r'\d+|\d*\.\d+|\d+%|%\d*', '', line)
    return cleaned_line.strip()

def clean_file(input_file, output_file):
    cleaned_data = set()  # Use a set to automatically remove duplicates

    with open(input_file, 'r') as infile:
        for line in infile:
            cleaned_line = clean_line(line)
            if cleaned_line:  # Skip empty lines after cleaning
                duplicate_line = clean_line(line)  # Assuming you want to duplicate cleaned data
                cleaned_data.add((cleaned_line, duplicate_line))

    with open(output_file, 'w') as outfile:
        outfile.write("STATUS = (\n")
        for cleaned_line, duplicate_line in sorted(cleaned_data):
            outfile.write(f"('{cleaned_line}', '{duplicate_line}'),\n")
        outfile.write(")\n")

# Replace 'input.txt' and 'output.txt' with your actual file names
clean_file('ecom/data.txt', 'cleaneddata.txt')
