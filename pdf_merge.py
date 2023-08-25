#by Jakub Wawak
#kubawawak@gmail.com

import PyPDF2, os

# function for merging pdf files into a single pdf file
# no input, files are taken from the current directory
def run_pdf_merge(merged_file_name):
        print("pdf_merge script startning...")
        pdfiles = []
        for filename in os.listdir('.'):
                if filename.endswith('.pdf'):
                        if filename != 'merged.pdf':
                                print("Added to collection: "+filename)
                                pdfiles.append(filename)
                                
        pdfiles.sort(key = str.lower)

        pdfMerge = PyPDF2.PdfMerger()
        for filename in pdfiles:
                pdfFile = open(filename, 'rb')
                pdfReader = PyPDF2.PdfReader(pdfFile)
                pdfMerge.append(pdfReader)
        pdfFile.close()
        pdfMerge.write(merged_file_name+'.pdf')
        print("pdf_merge script finished.")

# main function
if __name__ == "__main__":
        merged_file_name = input("Enter the name of the merged pdf file: ")
        run_pdf_merge(merged_file_name)
