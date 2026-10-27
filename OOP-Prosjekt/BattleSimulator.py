Pokemons = []

pokemon_movepool = {

        "Watergun": 10,
        "Hydro pump": 20,
}

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10

for move in enumerate(pokemon_movepool):
    print()
# for move_index, move in enumerate(pokemon_movepool):
#         for move_name, move_damage in move.items():
#             print(f" {move_index} {move_name} - {move_damage}")
       

user_move_choice = int(input("Choose a move from the movepool "))
print(pokemon_movepool["moves"][user_move_choice])


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
        try:
            for index, pokemon in enumerate(Pokemons):
                index = -1
                for pokemon in Pokemons:
                    index += 1
                    print(f"Type {index} to choose {pokemon.name}")
                
                pokemon_choice = int(input("Choose a pokemon! "))

                if 0 <= index < len(Pokemons):
                    chosen_pokemon = Pokemons[pokemon_choice]
                    print(f"The pokemon you choose was: {chosen_pokemon.name}")
                    return chosen_pokemon
                else:
                    print("Invalid pokemon index!")
                    break
        except ValueError, IndexError:
            continue
chosen_pokemon = choose_a_pokemon()
damage = pokemon_movepool[user_move_choice]

def take_damage(pokemon, damage):
    pokemon.hp -= damage
    
    print(f"{pokemon.name} took {damage} damage")
    print(f"{pokemon.name} now has {pokemon.hp} hp")

take_damage(chosen_pokemon, damage)
    


        





# for i in Pokemons:
#      name_of_pokemon = i.name
#      print(name_of_pokemon)