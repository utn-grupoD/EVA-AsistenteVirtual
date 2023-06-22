import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
from prueba import *
from functools import partial

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Eva asistente virtual")

# Crear un contenedor Frame para los botones y la imagen
contenedor = tk.Frame(ventana)
contenedor.pack()
contenedor2 = tk.Frame(ventana)
contenedor2.pack()

# Cargar la imagen
imagen = Image.open("eva.jpeg")
imagen = imagen.resize((100, 100))  # Ajustar el tamaño de la imagen según tus necesidades
imagen = ImageTk.PhotoImage(imagen)

# Crear un widget Label para mostrar la imagen
imagen_label = tk.Label(contenedor, image=imagen)
imagen_label.pack(side=tk.RIGHT, padx=10, pady=10)

# Crear la etiqueta para mostrar el resultado del reconocimiento de voz
resultado_label = tk.Label(ventana, text="")
resultado_label.pack(padx=10, pady=(10, 0))

# Crear el widget Text para mostrar la respuesta de búsqueda en Wikipedia
respuesta_text = tk.Text(ventana, height=6, width=40)
respuesta_text.pack(padx=10, pady=10)

# Cargar la imagen del GIF de carga y ajustar su tamaño
imagen_carga = Image.open("carga.gif")
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

    # Habilitar los botones nuevamente
    inicio_button.config(state=tk.NORMAL)
    detener_button.config(state=tk.NORMAL)


# Función para iniciar la escucha
def iniciar_escucha(resultado_label):
    mostrar_carga()  # Mostrar el GIF de carga al iniciar la escucha

    with sr.Microphone() as source:
        print("Escuchando...")
        resultado_label.config(text="Escuchando...")

        r.pause_threshold = 1  # Establecer el umbral de pausa en 1 segundo

        # Escuchar el audio del usuario
        audio = r.listen(source)

    try:
        print("Reconociendo...")
        resultado_label.config(text="Reconociendo...")

        # Utilizar la API de reconocimiento de voz de Google para reconocer el audio
        texto = r.recognize_google(audio, language='es-ES')

        # Imprimir el texto reconocido
        print("Texto reconocido:", texto)
        resultado_label.config(text="Texto reconocido: " + texto)

        procesar_comando(texto, resultado_label, respuesta_text, ventana)



    except sr.UnknownValueError:
        messagebox.showinfo("Error", "No se pudo reconocer el audio.")
        resultado_label.config(text="No se pudo reconocer el audio.")

    except sr.RequestError as e:
        messagebox.showinfo("Error", "No se puede acceder al servicio de reconocimiento de voz.")
        resultado_label.config(text="No se puede acceder al servicio de reconocimiento de voz.")

    ocultar_carga()  # Ocultar el GIF de carga después de procesar el comando


# Crear el botón de inicio
inicio_button = tk.Button(ventana, text="Iniciar")
inicio_button.config(command=partial(iniciar_escucha, resultado_label))
inicio_button.pack(pady=(0, 10))

# Crear el botón de detener
detener_button = tk.Button(ventana, text="Detener", command=detener_escucha)
detener_button.pack(pady=(0, 10))

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()
