import pyttsx3
import PyPDF2
from PyPDF2 import PdfReader
book = open("Seminar Topics.pdf", "rb") #Open the PDF file in binary mode
reader= PyPDF2.PdfReader(book)   #Read the PDF file using PyPDF2
pages=len(reader.pages)
print(pages)


speaker= pyttsx3.init() #Initialize the pyttsx3 engine
for i in range(pages):
    page = reader.pages[i]
    text = page.extract_text()
    speaker.say(text) #Convert the text to speech

    speaker.runAndWait() #Run the engine
    #speaker.save_to_file(text, 'pages.mp3'
