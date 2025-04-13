import PyPDF2
import os
import sys

def main():
    merger = PyPDF2.PdfMerger()

    pdfs_path = "pdfs/"
    merged_path = "merged/"

    pdf_files = [pdf for pdf in os.listdir(pdfs_path) if pdf.endswith(".pdf")]

    if not pdf_files:
        print("No PDF files found in pdfs folder.")
        return

    for file in pdf_files:
        merger.append(os.path.join(pdfs_path, file))

    if not os.path.exists(merged_path):
        os.makedirs(merged_path)

    merger.write(os.path.join(merged_path, "result.pdf"))

if __name__ == "__main__":
    main()