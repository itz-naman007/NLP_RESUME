import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """Extract text from a single PDF file."""
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def process_dataset(data_folder):
    """Extract text from all PDFs in the dataset structure."""
    for subfolder in os.listdir(data_folder):
        subfolder_path = os.path.join(data_folder, subfolder)
        if os.path.isdir(subfolder_path):
            print(f"Processing folder: {subfolder}")
            
            # Create an output folder for the current subfolder
            output_folder = os.path.join(subfolder_path, "extracted_texts")
            os.makedirs(output_folder, exist_ok=True)
            
            # Process each PDF in the subfolder
            for root, _, files in os.walk(subfolder_path):
                for file in files:
                    if file.endswith(".pdf"):
                        pdf_path = os.path.join(root, file)
                        output_file = os.path.join(output_folder, f"{os.path.splitext(file)[0]}_text.txt")
                        
                        # Skip if text is already extracted
                        if os.path.exists(output_file):
                            print(f"  Skipping already processed: {pdf_path}")
                            continue
                        
                        print(f"  Extracting from: {pdf_path}")
                        text = extract_text_from_pdf(pdf_path)
                        
                        # Save extracted text to a file.
                        with open(output_file, "w", encoding="utf-8") as outfile:
                            outfile.write(text)
            print(f"Text from {subfolder} saved in {output_folder}")

# Path to your dataset folder and pls change path according to your location.
data_folder = r"C:\Users\user\OneDrive\Desktop\New folder\data"
process_dataset(data_folder)
