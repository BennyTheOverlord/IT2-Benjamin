import random

Pokemons = [] #Kan være lurt å lagre i en dictionary senere

# "Pokemon" klassen inneholder generelle egenskaper for overordnede pokemoner, samt funksjonen for å velge et angrep for en pokemon.

player_turn = True
opponent_turn = False

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.pokemon_movepool = {
        "Watergun": 10,
        "Hydro pump": 20,

}
        
    def is_alive(self):
        if self.hp > 0:
            return self.hp

    def choose_attack(self):

        print(f"Now you have to choose an attack to use against your oppononent: {enemy_test.name}")

        for move_index, move in enumerate(self.pokemon_movepool):
            print(f"{move_index} - {move}")

        moves = list(self.pokemon_movepool.keys())

        user_move_choice = int(input("Choose a move from the movepool "))
        print(moves[user_move_choice])

        chosen_move = moves[user_move_choice]
        damage_number = self.pokemon_movepool[chosen_move]
        print(damage_number)

        return damage_number
        

class Enemy(Pokemon):
    def __init__(self, name):
        super().__init__(name)

    def is_alive(self):
        if self.hp > 0:
            return self.hp
    
    def choose_target(self, target):
        return target

    def enemy_move(self):

        moves = list(self.pokemon_movepool.keys())
        chosen_move = random.choice(moves)

        attack_damage = self.pokemon_movepool[chosen_move]

        print(f"{self.name} used {chosen_move} and did {attack_damage} damage!")

        return attack_damage
    

# Må gjerne lage flere mostandere på forhånd
enemy_test = Enemy("TestMotstander")


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
                print(f"Name: {pokemon.name}")
                print(f"Hp: {pokemon.hp}")
                i += 1 
show_status()

def choose_a_pokemon():
    while True:
        try:

            print("Now you have to choose a pokemon to fight your opponent")

            for index, pokemon in enumerate(Pokemons):
                print(f"Type {index} to choose {pokemon.name}")
              
            pokemon_choice = int(input("Choose a pokemon! "))

            if 0 <= pokemon_choice < len(Pokemons):
                chosen_pokemon = Pokemons[pokemon_choice]
                print(f"The pokemon you choose was: {chosen_pokemon.name}")
                return chosen_pokemon
            else:
                print("Invalid pokemon index!")
                break
        except (ValueError, IndexError):
            continue

chosen_pokemon = choose_a_pokemon()

def take_damage(pokemon, damage_number):
    pokemon.hp -= damage_number
    
    print(f"{pokemon.name} took {damage_number} damage")
    print(f"{pokemon.name} now has {pokemon.hp} hp")

    return damage_number

damage = chosen_pokemon.choose_attack()
enemy_damage = enemy_test.enemy_move()

take_damage(chosen_pokemon, enemy_damage) #Spillerens pokemon tar skade

take_damage(enemy_test, damage) #Motstanderens pokemon tar skade
    


# Begynnelse på den turbaserte delen av spillet        

while chosen_pokemon.hp > 0 and enemy_test.hp > 0:
    if player_turn:
        chosen_pokemon = choose_a_pokemon




# for i in Pokemons:
#      name_of_pokemon = i.name
#      print(name_of_pokemon)