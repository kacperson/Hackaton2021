# recognizer_instance.recognize_google(language = "pl-PL")
import speech_recognition as sr
import keyboard
import threading




# Recognizer_instance.recognize_google(audio_data, key = None, language = "pl-PL", show_all = False)
class voiceRecordThred(threading.Thread):
    endflag=False
    newslaid=False
    currentnumber=0;
    def __init__(self, threadID, name, counter):
        self.notatki=voiceRecordThred.currentnumber;
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.filename = "notatki"
        self.counter = counter
        self.r = sr.Recognizer()
        # var = 1

        self.f = open(self.filename + str(voiceRecordThred.currentnumber) + ".txt", "a")
        # r.recognize_google(sr.Microphone(), key = None, language = "pl-PL", show_all = False)

    def run(self):
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
                    except:
                        print("Sorry could not recognize what you said")
                if voiceRecordThred.currentnumber!=self.notatki or voiceRecordThred.endflag == True:  # keyboard.is_pressed('p') or keyboard.is_pressed('q'):
                    print("zmiana")
                    self.notatki=voiceRecordThred.currentnumber
                    self.f.close()
                    self.f = open(self.filename + str(voiceRecordThred.currentnumber) + ".txt", "a")
                    break
            print(voiceRecordThred.endflag)
            if voiceRecordThred.endflag == True:  # keyboard.is_pressed('q'):
                self.f.close()
                break
