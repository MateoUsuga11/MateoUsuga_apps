import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial Por Mateo Úsuga")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Cuenta cuentos")
 image = Image.open('1.png')
 st.image(image, width=190)
 st.write("En esta aplicación tenemos una IA que puede leer cuentos con diferentes voces y velocidades.") 
 url = "https://traductorcongtts.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Reconocimiento de Objetos")
 image = Image.open('4.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
 url = "https://yolov5matthew.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Modelo entrenado")
 image = Image.open('7.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace puedes ver como funcionan IAS generativas de texto como chatgpt") 
 url = "https://matthewtdfesp.streamlit.app"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Traductor")
 image = Image.open('2.jpg')
 st.image(image, width=200)
 st.write("En esta aplicación puedes hablar y generar un audio con traducción en multiples idiomas.") 
 url = "https://traductor-matthew.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Creador de imagenes basado en dibujos")
 image = Image.open('5.png')
 st.image(image, width=190)
 st.write("Aquí tienes un tablero para dibujar lo que quieras y la ia mejorará tu dibujo en un estilo que elijas") 
 url = "https://drawrecogmatt.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Piedra, papel o tijera")
 image = Image.open('8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace podrás jugar piedra papel o tijeras con la IA") 
 url = "https://tmmatthew.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Apoyo de aprendizaje en unity")
 image = Image.open('3.png')
 st.image(image, width=190)
 st.write("Esta IA recibe un documento de unity para apoyar el aprendizaje de este software") 
 url = "https://chatpdfunity.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Recomendador de Imagenes")
 image = Image.open('6.jpg')
 st.image(image, width=200)
 st.write("Agrega una imagen de tu videojuego favorito y la IA se encargará de recomnedarte experiencias parecidas") 
 url = "https://visionapp-matt.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Controlar robot con voz")
 image = Image.open('9.jpg')
 st.image(image, width=200)
 st.write("Con comandos de voz puedes controlar elementos del mundo real") 
 url = "https://ctrlvoice-matthew.streamlit.app/"  
 st.write(f"Vision: [Enlace]({url})")


