import pyttsx3
import wikipedia

wikipedia.set_lang("es")
asistente = pyttsx3.init()

entrada = input("Buscar en Wikipedia Google: ")

resultado = wikipedia.summary(entrada, sentences = 1)
print(resultado)

asistente.say(resultado)
asistente.runAndWait()
