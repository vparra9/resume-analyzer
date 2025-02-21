import pdfplumber
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")
nltk.download("punkt")

#Define stopwords globally
stopWords = set(stopwords.words("english"))

# Function extractTextFromPdf to extract text from a pdf
def extractTextFromPdf(pdfPath):
    text = "" #Initializes an empty string
    #Opens pdf using pdfplumber moduke
    with pdfplumber.open(pdfPath) as pdf:
        for page in pdf.pages:
            extractedText = page.extract_text()
            if extractedText:
                text += extractedText + "\n"
    return text

#Function to clean and remove stopwords
def preProcessText(text):
    #Tokenize text
    words = nltk.word_tokenize(text)

    #Filter out stopwords
    filteredWords = [word for word in words if word.lower() not in stopWords]

    #Rebuild text without stopwords
    cleanedText = " ".join(filteredWords)

    return cleanedText

#Test with a sample PDF
pdf_file = "resume.pdf" #Replace with your file
resume_text = extractTextFromPdf(pdf_file)

#Preprocess and clean the extracted text
cleanedResumeText = preProcessText(resume_text)

#Print original and cleaned text for testing purposes, shows first 500 characters
print("Original Extracted Text:\n", resume_text[:5000]) 
print("\nCleaned Text:\n", cleanedResumeText[:500])

