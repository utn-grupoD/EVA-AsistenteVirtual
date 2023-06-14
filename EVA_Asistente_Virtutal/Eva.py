import datetime
import webbrowser
import speech_recognition as sr
import pyttsx3;
import wikipedia;
import pywhatkit;

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
            talk("Hola, soy EVA, tu asistente virtual")
            audio = r.listen(source)
    
            try:
                text = r.recognize_google(audio, languaje="ES")
                print('Has dicho: {}'.format(text))
                print(text)
                if 'reproduce' in text:
                    music = text.replace('reproduce','');
                    print('Reproduciendo...' + music);
                    pywhatkit.playonyt(music);
                if 'busca' in text:
                    order = text.replace('busca','');
                    info = wikipedia.summary(order, 1);
                    talk(info);
                if "hora" in text:
                    hora = datetime.datetime().now().strftime('%H:%M');
                    talk('Son las '+ hora);
                if "Amazon" in text:
                    webbrowser.open('http://amazon.es')
                if "noticias" in text:
                    webbrowser.open('https://www.losandes.com.ar/')
                if "Facebook" in text:
                    webbrowser.open('www.facebook.com')
                if "Google" in text:
                    webbrowser.open('www.google.com')
                if "Instagram" in text:
                    webbrowser.open('www.instagram.com')
                if 'Noticias' in text:
                    webbrowser.open('www.mdzol.com')
                if "que tal" in text:
                    print("Bien y vos?")
                if("salir") in text:
                    break
            except:
                print('No te he entendido')

from tkinter import *

def onClosing():
    root.destroy()
    print("Ventana cerrada")

def press():
    run()

root = Tk()
root.title("EVA")
root.geometry("400x150")
root.config(bg="lightblue")

mensaje = Label(root, text="Asistente Virtual", bg="lightblue", font='candara 16 bold', justify="center")
mensaje2 = Label(root, text="Aprete el boton (Iniciar) para empezar a hablar", bg="lightblue", font='candara')
mensaje.pack()
mensaje2.pack()

button = Button(root, text="Iniciar", command=press, background="green", foreground="white")
button.pack()

button2 = Button(root, text="Salir", command=onClosing, background="red", foreground="white")
button2.pack()

root.mainloop()

