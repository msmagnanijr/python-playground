from gtts import gTTS 
from playsound import playsound 
import pytesseract as ocr

from PIL import Image

text = ocr.image_to_string(Image.open('motivacao.jpg'), lang='por')

var = gTTS(text = text,lang = "pt") 
var.save("text.mp3") 
playsound("text.mp3")
