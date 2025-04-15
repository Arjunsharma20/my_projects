import PyPDF2
import os

def merge_pdfs(pdf_list, output_filename):
    merger = PyPDF2.PdfMerger()
    
    for pdf in pdf_list:
        if os.path.exists(pdf):
            merger.append(pdf)
        else:
            print(f"File not found: {pdf}")
    
    merger.write(output_filename)
    merger.close()
    print(f"Merged PDF saved as: {output_filename}")

# Example usage
pdf_files = [
    'C:/Users/Lenovo/OneDrive/Desktop/arjun/Python/PDF_merge/BCA (AI & ML)-5th Sem.pdf',
    'C:/Users/Lenovo/OneDrive/Desktop/arjun/Python/PDF_merge/BCA-3rd Sem Syllabus.pdf',
    'C:/Users/Lenovo/OneDrive/Desktop/arjun/Python/PDF_merge/biswajit python.pdf'
]
merge_pdfs(pdf_files, 'merged_output.pdf')
