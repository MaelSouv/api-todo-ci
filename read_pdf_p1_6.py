import pypdf
import sys

file_path = r"c:\Users\souve\Downloads\Atelier-final-Jour3.pdf"

try:
    reader = pypdf.PdfReader(file_path)
    # Print pages 0 to 5 (which are pages 1-6 in human terms)
    for i in range(6):
        print(f"--- Page {i+1} ---")
        print(reader.pages[i].extract_text())
except Exception as e:
    print(f"Error reading PDF: {e}")
