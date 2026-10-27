Pokemons = []

pokemon_movepool = [
    {
        "Watergun": 10
    },
    {
        "Hydro pump": 20
     },
]

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
move_index = -1
for move in pokemon_movepool:
        move_index += 1
        print(f"{move.items()}, {move_index}")

user_move_choice = int(input("Choose a move from the movepool "))
print(user_move_choice)

while True:
    try:
        if len(Pokemons) < 2:
            try:
                user_choice = int(input("Choose an option: 1: Create a pokemon "))

            except ValueError:
                continue
            if user_choice == 1:

                def create_pokemon():
                    pokemon_name = input("Choose a name for the pokemon you want to create: ")
                    new_pokemon = Pokemon(pokemon_name)
                    Pokemons.append(new_pokemon)
                    return new_pokemon
            else:
                break

        else:
            break
        create_pokemon()
    except ValueError:
        continue

    def show_status():
        i = 0
        while i < len(Pokemons):
            for pokemon in Pokemons:
                print(pokemon.name)
                print(pokemon.hp)
                print(pokemon.attack)
                i += 1 
show_status()

def choose_a_pokemon():
    while True:
        pokemon_index = -1
        try:
            if pokemon_index < len(Pokemons):
                for pokemon in Pokemons:
                    pokemon_index += 1
                    print(f"Write {pokemon_index} to choose {pokemon.name}")
                pokemon_choice = int(input("Choose a pokemon! "))

                print(f"The pokemon you choose was: {Pokemons[pokemon_choice].name}")
                return pokemon_choice
            else:
                break

        
        except ValueError, IndexError:
            continue
    
choose_a_pokemon()



# for i in Pokemons:
#      name_of_pokemon = i.name
#      print(name_of_pokemon)
