import pdfplumber # library used to read pdf file 
import docx 

def extract_text(file):
    text="" #this variable  stored all the extracted text 
    if file.name.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:  #loop through each page in odf 
                 page_text = page.extract_text() #extract text from current page 
                 if page_text:
                    text += page_text + " " #add page text tp main text 
    elif file.name.endswith(".docx"):
        doc = docx.Document(file) #open docx file 
        for para in doc.paragraphs: #loop through each paragraph in docx file 
            text += para.text + " " #add paragraph text to main text
    text = text.lower()
    text = text.replace("\n", " ") #replace new line with space for better processing
    return text #all text convert to lowercase for easy comparison later