
#recognizer_instance.recognize_google(language = "pl-PL")
import speech_recognition as sr
import keyboard
#Recognizer_instance.recognize_google(audio_data, key = None, language = "pl-PL", show_all = False)

r = sr.Recognizer()
var = 1
f = open("mytext.txt", "a")


#r.recognize_google(sr.Microphone(), key = None, language = "pl-PL", show_all = False)
while True:
    while True:
        
        with sr.Microphone() as source:
            print("Speak Anything :")
            audio = r.listen(source,timeout=3000)
            try:
                text = r.recognize_google(audio,language = "pl-PL")
                print("You said : {}".format(text))
                f.write("\n")
                f.write(text)
                if var == 1: #keyboard.is_pressed('p') or keyboard.is_pressed('q'):
                    print("koniec slajdu!!!")
                    break
            except:
                print("Sorry could not recognize what you said")
        if var == 1: #keyboard.is_pressed('p') or keyboard.is_pressed('q'):
            print("koniec slajdu!!!")
            break
        
    if var == 1:#keyboard.is_pressed('q'):
        break
f.close()