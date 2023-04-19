import speech_recognition as sr  
import webbrowser

r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Hable:")                                                                                   
    audio = r.listen(source)   

try:
    print("Has dicho " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("No se puede reconocer el audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))