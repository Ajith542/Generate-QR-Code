from gtts import gTTS
import os
import io
import eel

eel.init('APP')

@eel.expose
def generate_Speech_Eng(data):
    language = 'en'
    output = gTTS(text = data,lang=language,slow=False)
    output.save("Eng.mp3")
    os.system("start Eng.mp3")  

@eel.expose
def generate_Speech_Mal(data):
    language = 'ml'
    output = gTTS(text = data,lang=language,slow=False)
    output.save("Mal.mp3")
    os.system("start Mal.mp3") 

eel.start('app.html', size = (750, 800))  