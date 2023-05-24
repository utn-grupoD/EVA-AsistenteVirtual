import datetime
import speech_recognition as sr;
import pyttsx3;
import pywhatkit;
import wikipedia;
import webbrowser;

name = 'eva';
listener = sr.Recognizer();


engine = pyttsx3.init();
voices = engine.getProperty('voices');
engine.setProperty('voice', voices[5].id);

def talk(text):
    engine.say(text);
    engine.runAndWait();

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...");
            voice = listener.listen(source);
            rec = listener.recognize_google(voice, languaje="es-US");
            rec = rec.lower();
            if name in rec:
                rec = rec.replace(name, '');
                talk(rec);
    except TimeoutError as msg:
            print(msg);
    
    return rec;

def run():
    rec= listen();
    if 'reproduce' in rec:
        music = rec.replace('reproduce','');
        print('Reproduciendo...' + music);
        pywhatkit.playonyt(music);
    elif 'hora' in rec:
        hora = datetime.datetime().now().strftime('%H:%M');
        talk('Son las '+ hora);
    elif 'busca' in rec:
        order = rec.replace('busca','');
        info = wikipedia.summary(order, 1);
        talk(info);
    elif 'facebook' in rec:
        fb = webbrowser.open('https://www.facebook.com/');
    elif 'google' in rec:
        gl = webbrowser.open('https://www.google.com.ar/')
    

run();
