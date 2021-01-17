# recognizer_instance.recognize_google(language = "pl-PL")
import speech_recognition as sr
import keyboard
import threading

global newslaid
newslaid=False
global endflag = False


# Recognizer_instance.recognize_google(audio_data, key = None, language = "pl-PL", show_all = False)
class voiceRecordThred(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.filenum=1
        self.filename="notatki"
        self.counter = counter
        self.r = sr.Recognizer()
        # var = 1
        self.f = open(self.filename+str(self.filenum)+".txt", "a")
        # r.recognize_google(sr.Microphone(), key = None, language = "pl-PL", show_all = False)

    def run(self):
        global newslaid
        while True:
            while True:
                with sr.Microphone() as source:
                    print("Speak Anything :")
                    audio = self.r.listen(source, timeout=3000)
                    try:
                        text = self.r.recognize_google(audio, language="pl-PL")
                        print("You said : {}".format(text))
                        self.f.write("\n")
                        self.f.write(text)
                        # if var == 1:  # keyboard.is_pressed('p') or keyboard.is_pressed('q'):
                        #    print("koniec slajdu!!!")
                        #    break#po co 2 razy ?
                    except:
                        print("Sorry could not recognize what you said")
                if newslaid == True||endflag==True:  # keyboard.is_pressed('p') or keyboard.is_pressed('q'):
                    newslaid = False
                    self.f.close()
                    self.f = open(self.filename + str(self.filenum) + ".txt", "a")
                    filenum+=1;
                    break

            if endflag==True:  # keyboard.is_pressed('q'):
                break
