
import pytesseract   
from PIL import Image    
import playsound
import speech_recognition as sr  
from gtts import gTTS  
from googletrans import Translator   


img = Image.open('lol1.png')    


print(img)                       
 
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe' 
result = pytesseract.image_to_string(img) 

# with open('abc.txt',mode ='w') as file:  
#     file.write(result) 

print(result) 
                
p = Translator()                     
k = p.translate(result,dest='hindi')    
print(k) 
def speak(result):
    tts=gTTS(text=result,lang="en")
    filename ="vo.mp3"
    tts.save(filename)
    playsound.playsound(filename)
speak(result);
