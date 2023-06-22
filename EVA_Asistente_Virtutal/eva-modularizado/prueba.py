import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import datetime
from tkinter import Text
import tkinter as tk



# Crear un objeto de reconocimiento de voz
r = sr.Recognizer()

# Crear un objeto de síntesis de voz
engine = pyttsx3.init()

# Configurar la voz en español
engine.setProperty('voice', 'es')

# Establecer el idioma de Wikipedia como español
wikipedia.set_lang('es')

# Función para procesar los comandos de voz
def procesar_comando(texto, resultado_label, respuesta_text, ventana):

    if "HOLA" in texto.upper():
        # Imprimir la respuesta
        print("¡Hola! ¿En qué puedo ayudarte?")
        resultado_label.config(text="¡Hola! ¿En qué puedo ayudarte?")

        # Hacer que el programa hable
        engine.say("¡Hola! ¿En qué puedo ayudarte?")
        engine.runAndWait()

    elif "ADIOS" in texto.upper():
        # Imprimir respuesta
        print("Hasta luego. ¡Que tengas un buen día!")
        resultado_label.config(text="Hasta luego. ¡Que tengas un buen día!")

        # Hablar
        engine.say("Hasta luego. ¡Que tengas un buen día!")
        engine.runAndWait()

        ventana.quit()

    elif "HORA" in texto.upper():
        # Obtener la hora actual
        hora_actual = datetime.datetime.now().strftime("%H:%M:%S")

        # Imprimir la hora actual
        print("La hora actual es:", hora_actual)

        # Decir la hora actual
        engine.say("La hora actual es: " + hora_actual)
        engine.runAndWait()

    elif "FECHA" in texto.upper():
        # Obtener la fecha actual
        fecha_actual = datetime.datetime.now().strftime("%d de %B de %Y")

        # Imprimir la fecha actual
        print("La fecha actual es:", fecha_actual)

        engine.say("La fecha actual es: " + fecha_actual)
        engine.runAndWait()

    elif "GOOGLE" in texto.upper():
        engine.say("Abriendo Google")
        engine.runAndWait()
        webbrowser.open('https://www.google.com.ar/')

    elif "FACEBOOK" in texto.upper():
        engine.say("Abriendo Facebook")
        engine.runAndWait()
        webbrowser.open('https://www.facebook.com/')

    elif "MERCADO LIBRE" in texto.upper():
        engine.say("Abriendo Mercado Libre")
        engine.runAndWait()
        webbrowser.open('https://www.mercadolibre.com/')

    elif "BUSCA" in texto.upper():
        # Obtener el término de búsqueda eliminando la palabra "busca"
        termino_busqueda = texto.replace("Busca", "").strip()

        # Realizar la búsqueda en Wikipedia
        try:
            resultado = wikipedia.summary(termino_busqueda, sentences=2)
            print("Resultado de búsqueda en Wikipedia:")
            print(resultado)
            resultado_label.config(text="")

            respuesta_text.insert(tk.END, resultado)

            engine.say("Resultado de la búsqueda en Wikipedia: " + resultado)
            engine.runAndWait()

        except wikipedia.exceptions.DisambiguationError as e:
            engine.say("La búsqueda tiene múltiples resultados. Por favor, sé más específico.")
            engine.runAndWait()

            print("La búsqueda tiene múltiples resultados. Por favor, sé más específico.")
            respuesta_text.delete(1.0, tk.END)  # Limpiar el contenido anterior
            respuesta_text.insert(tk.END, "La búsqueda tiene múltiples resultados. Por favor, sé más específico.")
        except wikipedia.exceptions.PageError as e:
            engine.say("No se encontró ninguna página en Wikipedia para el término de búsqueda.")
            engine.runAndWait()

            print("No se encontró ninguna página en Wikipedia para el término de búsqueda.")
            respuesta_text.delete(1.0, tk.END)  # Limpiar el contenido anterior
            respuesta_text.insert(tk.END, "No se encontró ninguna página en Wikipedia para el término de búsqueda.")
    else:
        engine.say("Lo siento. Por el momento no reconozco ese comando.")
        engine.runAndWait()
        print("Comando no reconocido")
        resultado_label.config(text="Comando no reconocido")


# Función para detener la escucha
def detener_escucha(ventana):
    ventana.destroy()

