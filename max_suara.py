from gtts import gTTS
import json
from playsound import playsound

def suara(a):
    lang = "id"
    speak = gTTS(a,lang=lang)
    speak.save("k.mp3")
    playsound("k.mp3")

try:
    while True:
        i = input("Anda: ")
        with open('json/assist.json','r') as source:
            data = json.load(source)
            if i in data:
                print("bot: ",data[i])
                suara(data[i])
            else:
                print("bot: Maaf aku tidak mengerti")
                suara("maaf aku tidak mengerti")
except (KeyboardInterrupt) as a:
    print("program dihentikan")
    suara("sampai jumpa")
    
    

