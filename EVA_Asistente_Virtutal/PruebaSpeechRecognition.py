import datetime
import speech_recognition as sr;
import pyttsx3;
import pywhatkit;
import wikipedia;

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
    except:
        pass
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


run();
