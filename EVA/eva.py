import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import datetime
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import pyjokes
import subprocess


# Crear un objeto de reconocimiento de voz
r = sr.Recognizer()

# Crear un objeto de síntesis de voz
engine = pyttsx3.init()

# Configurar la voz en español
engine.setProperty('voice', 'es')

# Establecer el idioma de Wikipedia como español
wikipedia.set_lang('es')

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Eva asistente virtual")

# Crear un contenedor Frame para los botones y la imagen
contenedor = tk.Frame(ventana)
contenedor.pack()
contenedor2 = tk.Frame(ventana)
contenedor2.pack()

# Cargar la imagen
imagen = Image.open("EVA/eva.jpeg")
imagen = imagen.resize((100, 100))  # Ajustar el tamaño de la imagen según tus necesidades
imagen = ImageTk.PhotoImage(imagen)

#Crear un widget Label para mostrar la imagen
imagen_label = tk.Label(contenedor, image=imagen)
imagen_label.pack(side=tk.RIGHT, padx=10, pady=10)

# Crear la etiqueta para mostrar el resultado del reconocimiento de voz
resultado_label = tk.Label(ventana, text="")
resultado_label.pack(padx=10, pady=(10, 0))

# Crear el widget Text para mostrar la respuesta de búsqueda en Wikipedia
respuesta_text = tk.Text(ventana, height=6, width=40)
respuesta_text.pack(padx=10, pady=10)

# Cargar la imagen del GIF de carga y ajustar su tamaño
imagen_carga = Image.open("EVA/carga.gif")
imagen_carga = imagen_carga.resize((30, 30))  # Ajustar el tamaño del GIF según tus necesidades
imagen_carga = ImageTk.PhotoImage(imagen_carga)

# Crear un widget Label para mostrar el GIF de carga
imagen_carga_label = tk.Label(contenedor2, image=imagen_carga)
imagen_carga_label.pack(side=tk.LEFT, padx=10, pady=10)
imagen_carga_label.pack_forget()



# Función para mostrar el GIF de carga

def mostrar_carga():
    # Mostrar la imagen del GIF de carga
    imagen_carga_label.pack()

    # Deshabilitar los botones mientras se muestra el GIF de carga
    inicio_button.config(state=tk.DISABLED)
    detener_button.config(state=tk.DISABLED)

    ventana.update()

    ventana.after(2000, ocultar_carga)  # Llamar a la función ocultar_carga después de 2 segundos


# Función para ocultar la imagen del GIF de carga y habilitar los botones
def ocultar_carga():
    # Ocultar la imagen del GIF de carga
    imagen_carga_label.pack_forget()

    # Habilitar los botones después de ocultar el GIF de carga
    inicio_button.config(state=tk.NORMAL)
    detener_button.config(state=tk.NORMAL)


# Función para reconocer y procesar el audio
def reconocer_voz():
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)

        mostrar_carga()

        try:
            # Utilizar el reconocimiento de voz de Google para convertir el audio en texto
            texto = r.recognize_google(audio, language="es-ES")

            # Imprimir el texto
            print("Has dicho: " + texto)
            resultado_label.config(text="Has dicho: " + texto)

            # Procesar los comandos de voz
            procesar_comando(texto)
        except sr.UnknownValueError:
            engine.say("Lo siento. No te entendí")
            engine.runAndWait()
            print("No se pudo entender el audio")
            resultado_label.config(text="No se pudo entender el audio")
        except sr.RequestError as e:
            print("Error al solicitar resultados del servicio de reconocimiento de voz; {0}".format(e))
            resultado_label.config(text="Error en el reconocimiento de voz")
        
            


# Función para procesar los comandos de voz
def procesar_comando(texto):
    if "HOLA" in texto.upper():
        # Imprimir la respuesta
        print("¡Hola! ¿En qué puedo ayudarte?")
        resultado_label.config(text="¡Hola! ¿En qué puedo ayudarte?")

        # Hacer que el programa hable
        engine.say("¡Hola! ¿En qué puedo ayudarte?")
        engine.runAndWait()

    elif "ADIÓS" in texto.upper() or "ADIÓS" in texto.upper():
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
    
    elif "DIARIO" and "LOS ANDES" in texto.upper():
        engine.say("Abriendo Diario Los Andes")
        engine.runAndWait()
        webbrowser.open('https://www.losandes.com.ar')
        
    elif "YOUTUBE" in texto.upper():
        engine.say("Abriendo Youtube")
        engine.runAndWait()
        webbrowser.open('https://www.youtube.com/')

    elif "GITHUB" in texto.upper():
        engine.say("Abriendo Github")
        engine.runAndWait()
        webbrowser.open('https://github.com')

    elif "BUSCA" in texto.upper() or "BUSQUE" in texto.upper() or "BUSCAME" in texto.upper() or "BUSCAR" in texto.upper():
        # Obtener el término de búsqueda eliminando las palabras clave
        termino_busqueda = texto.replace("BUSCA", "").replace("BUSQUE", "").replace("BUSCAME", "").replace("BUSCAR", "").strip()

        try:
            resultado = wikipedia.summary(termino_busqueda, sentences=2)
            print("Resultado de búsqueda en Wikipedia:")
            print(resultado)
            respuesta_text.delete(1.0, tk.END)  # Limpiar el contenido anterior
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

    elif "CHISTE" in texto.upper():
        # Obtener un chiste
        chiste = pyjokes.get_joke(language='es')

        print(chiste)

        # Decir el chiste
        engine.say(chiste)
        engine.runAndWait()

    elif "SPOTIFY" in texto.upper():
        engine.say("Abriendo Spotify")
        engine.runAndWait()
        subprocess.Popen(["spotify"])

    elif "CALCULADORA" in texto.upper():
        engine.say("Abriendo la calculadora")
        engine.runAndWait()
        abrir_calculadora()


def abrir_calculadora():
    try:
        # Intentar abrir gnome-calculator
        subprocess.Popen(["gnome-calculator"])      
    except FileNotFoundError:
        try:
            # Intentar abrir mate-calc
            subprocess.Popen(["mate-calc"])
        except FileNotFoundError:
            try:
                # Intentar abrir kcalc
                subprocess.Popen(["kcalc"])
            except FileNotFoundError:
                print("No se encontró ninguna calculadora instalada en el sistema.")

# Función para detener la escucha
def detener_escucha():
    ventana.quit()


# Crear los botones
inicio_button = tk.Button(contenedor, text="Iniciar", command=reconocer_voz)
inicio_button.pack(side=tk.LEFT, padx=10, pady=10)

detener_button = tk.Button(contenedor, text="Detener", command=detener_escucha)
detener_button.pack(side=tk.LEFT, padx=10, pady=10)

# Ejecutar la interfaz gráfica
ventana.mainloop()
