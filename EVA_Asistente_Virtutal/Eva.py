import webbrowser
import speech_recognition as sr
import pyttsx3;

r = sr.Recognizer() 


engine = pyttsx3.init();
voices = engine.getProperty('voices');
engine.setProperty('voice', voices[20].id);


def talk(text):
    engine.say(text);
    engine.runAndWait();

def run():
    while True:
        with sr.Microphone() as source:
            talk("Hola, soy EVA tu asistente por voz")
            audio = r.listen(source)
    
            try:
                text = r.recognize_google(audio)
                print('Has dicho: {}'.format(text))
                print(text)
                if "Amazon" in text:
                    webbrowser.open('http://amazon.es')
                if "noticias" in text:
                    webbrowser.open('https://www.losandes.com.ar/')
                if "Facebook" in text:
                    webbrowser.open('www.facebook.com')
                if "Google" in text:
                    webbrowser.open('www.google.com')
                if "que tal" in text:
                    print("Bien y vos?")
                if(text != ""):
                    break
                if("salir") in text:
                    break
            except:
                print('No te he entendido')

from tkinter import Tk, Button

def onClosing():
    root.destroy()
    print("Ventana cerrada")
    
def press():
    run()

root = Tk()
root.title("Uso de Boton")
root.geometry("400x400")
root.protocol("WM_DELETE_WINDOW",onClosing)

button = Button(root,text="Iniciar", command=press, background="green", foreground="white")
button.pack()

root.mainloop()
