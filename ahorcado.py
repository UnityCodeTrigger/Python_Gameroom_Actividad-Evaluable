import random

words = [
    "Gato", "Casa", "Mesa", "Libro", "Silla", "Flor", "Coche", "Pez", "Niño", "Sol",
    "Agua", "Luna", "Mano", "Ropa", "Perro", "Reloj", "Taza", "Pan", "Nube", "Vaso",
    "Oro", "Sala", "Lápiz", "Jugo", "Verde", "Pared", "Azul", "Fruta", "Tren", "Sombrero"
]

selectedChars = []

MAX_TRIES = 5

def StartGame():
    randIndex = random.randint(0, len(words) - 1)
    currentWord = words[randIndex]
    
    for i in range(MAX_TRIES):
        print(ShowProgress(currentWord))
        
        selectedChar = input("Ingresa una letra: ")
        selectedChars.append(selectedChar[0])
    
    print(f"La respuesta correcta era: {currentWord}")

def ShowProgress(currentWord):
    hiddedWord = list("_" * len(currentWord))

    if len(selectedChars) != 0:
        for i in range(len(currentWord)):
            if currentWord[i] in selectedChars:
                hiddedWord[i] = currentWord[i]

    return "".join(hiddedWord)

