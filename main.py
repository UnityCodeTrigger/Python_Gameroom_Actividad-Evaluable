import adivina, piedraPapelTijera, ahorcado

# Diccionario de juegos disponibles
gamesDictionary = { 
    "1": "Adivina Un Numero",
    "2": "Piedra Papel o Tijera",
    "3": "El Ahorcado"
}

def show_game_menu():
    lines = [" - Seleccione un juego"]
    for key, game in gamesDictionary.items():
        lines.append(f"    ({key}) {game}")
    
    padding = 8
    max_length = max(len(line) for line in lines)
    width = max_length + padding
    
    print('#' * width)
    for line in lines:
        print(f"# {line.ljust(int(max_length + padding / 2))} #")
    print('#' * width)

def start_selected_game(game_id):
    if game_id == 1:
         adivina.StartGame()

    elif game_id == 2:
        piedraPapelTijera.StartGame()

    elif game_id == 3:
        ahorcado.StartGame()

    else:
        print("Selección inválida.")

while (True):
    show_game_menu()
    gameSelected = input()
    start_selected_game(int(gameSelected))