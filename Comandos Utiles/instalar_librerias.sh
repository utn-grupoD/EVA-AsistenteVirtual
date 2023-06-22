#!/bin/bash

# Instalar las librerías de Python
sudo apt update
sudo apt install -y python3-pip
pip3 install SpeechRecognition
pip3 install pyaudio
pip3 install pyttsx3
pip3 install wikipedia
pip3 install pyjokes

# Instalar las dependencias adicionales
sudo apt install -y apt
sudo apt install -y portaudio19-dev
sudo apt install -y python3-tk
sudo apt install -y espeak

# Instalar y actualizar Pillow
pip3 install pillow
pip3 install --upgrade pillow
