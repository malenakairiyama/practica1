import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]


def preparar_palabra(nivel):
    
    word = random.choice(words)
    if nivel == 1:
        word_displayed = "".join(letra if letra.lower() in "aeiou" else "_" for letra in word)
    elif nivel == 2:
        word_displayed = word[0] + "_" * (len(word) - 2) + word[-1]
    elif nivel == 3:
         word_displayed = "_" * len(word)
    else:
        raise ValueError("Nivel de dificultad no válido. Los niveles son 1 (Fácil), 2 (Media) o 3 (Difícil).")
    return word, word_displayed


#Solicita al usuario que elija el nivel de dificultad
while True:
    try:
        nivel = int(input("Elige el nivel de dificultad (1 para Fácil, 2 para Media, 3 para Difícil): "))
        secret_word, word_displayed = preparar_palabra(nivel)
        break
    except ValueError:
        print("Error: Ingresa un número válido (1, 2 o 3) para elegir el nivel de dificultad.")



#Número máximo de intentos permitidos
max_fallos = 10

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
print(f"Palabra: {word_displayed}")

fallos = 0 #contador

while fallos < max_fallos:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    
    # Verificar si se ingresó una letra válida
    if len(letter) != 1 or not letter.isalpha():
        print("Error: Debes ingresar una única letra válida.")
        continue
    
    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        fallos+=1
        
    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter, display_letter in zip(secret_word, word_displayed):
        if letter.lower() in guessed_letters:
            letters.append(letter.lower())
        else:
            letters.append(display_letter) #display_letter de wor_display en este caso es un guion bajo
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    
# Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta:{secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_fallos} intentos.")
    print(f"La palabra secreta era: {secret_word}")
