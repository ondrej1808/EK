import os

def extract_headings_from_file(file_path):
    headings = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("#"):  # Assuming headings start with '#'
                headings.append(line)
    return headings

def export_headings_from_folder(folder_path, output_file):
    all_headings = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):  # Process only Python files
                file_path = os.path.join(root, file)
                all_headings.extend(extract_headings_from_file(file_path))
    
    with open(output_file, 'w') as out_file:
        for heading in all_headings:
            out_file.write(heading + '\n')

if __name__ == "__main__":
    folder_path = "SEMESTR_4/SEE/priprava"  # Replace with your folder path
    output_file = "headings.txt"  # Replace with your output file path
    export_headings_from_folder(folder_path, output_file)
    print(f"Headings exported to {output_file}")