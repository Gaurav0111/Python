import pyttsx3
import PyPDF2
book = open('Social Media Hacking Hack Facebook Whatsapp Instagram Twitter.pdf' , 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(6)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()