from gtts import gTTS
import os
import io
import eel

eel.init('APP')

@eel.expose

def generate_Speech(data):
    language = 'en'
    output = gTTS(text = data,lang=language,slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")  

eel.start('app.html', size = (750, 800))  