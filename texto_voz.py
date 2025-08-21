from gtts import gTTS
import os
texto="chinito comel aloz con su novia kenia"
output=gTTS(texto, lang='es', slow=False)
output.save("output.mp3")
os.system('start output.mp3')