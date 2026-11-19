import random
from Visuals import BattleUI

ui = BattleUI()

console = ui.console

Pokemons = []

# "Pokemon" klassen inneholder generelle attributer for overordnede pokemoner, samt metoden for å velge et angrep for en pokemon.

class Pokemon: #Super-klassen
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.pokemon_movepool = {
        "Watergun": 10,
        "Hydro pump": 20,
}
        
    def is_alive(self):
            return self.hp > 0 #Ved å ha > 0 her vil den returnere en bolean istedenfor selve hp verdien

    def choose_attack(self):

        ui.show_moves(self) #Lager en tabell med tilgjengelige trekk og info om dem
        
        print(f"Now you have to choose an attack to use against your oppononent: {active_enemy.name}")

        moves = list(self.pokemon_movepool.keys())

        while True:
            try:
                user_move_choice = int(input("Choose a move from the movepool "))
                
                if 0 <= user_move_choice < len(moves):

                    print(moves[user_move_choice])

                    chosen_move = moves[user_move_choice]
                    damage_number = self.pokemon_movepool[chosen_move]

                    ui.message( #Lager en boks med "cyan" farge som sier at objektet brukte det valgte trekket
                    f"{self.name} used {chosen_move}! \n"
                    f"Damage: {damage_number}",
                    "cyan"
                    )

                    print(damage_number)

                    return damage_number
                else:
                    console.print("[red]You have to choose an available move![/red]") 

            except (ValueError, IndexError):
                console.print("[red]Please choose a move with a valid index![/red]")
        

class Enemy(Pokemon): #Sub-klassen
    def __init__(self, name):
        super().__init__(name)
    
    def choose_target(self, target):
        return target

    def enemy_move(self):

        moves = list(self.pokemon_movepool.keys())

        chosen_move = random.choice(moves)

        attack_damage = self.pokemon_movepool[chosen_move]

        ui.message(
            f"{self.name} used {chosen_move}! \n"
            f"Damage: {attack_damage}",
            "red"
        )

        return attack_damage
    
enemy_team = [
     Enemy("TestMotstander"),
     Enemy("TestMotstander2"),
     Enemy("TestMotstander3")
]

active_enemy = enemy_team[0]

def choose_enemy_pokemon():
    available_pokemon = []

    for pokemon in enemy_team:
        if pokemon.is_alive():
            available_pokemon.append(pokemon)

    if available_pokemon:
        return random.choice(available_pokemon)
        
    return None
    

def choose_action(): #Lar brukeren velge hva de vil bruke turen til
    while True:
        try:   
            user_action = int(input("Choose an option: 0: Fight --- 1: Switch "))
    
            if user_action == 0:
                return "fight"
        
            elif user_action == 1:
                if len(Pokemons) <= 1:
                    print("You can't switch when you only have 1 pokemon left!")
                    continue #Ved å ha continue her returnerer den ingenting hvis brukeren ikke skal kunne bytte. Dermed mister de ikke turen sin
                else:
                    return "switch"
                
            else:
                print("You have to choose either 0 (fight) or 1 (switch)")
          

        except (IndexError, ValueError):
            ui.message(
                "You have to choose a valid option! \n",
                "red"
            )
            continue

#While loop for å lage karakterene til spilleren ved start av programmet!

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

def choose_a_pokemon(current_pokemon=None): #Funksjon for å velge hvilken karakter som kjemper
    while True:
        try:
            print("Now you have to choose a pokemon to fight your opponent")

            for index, pokemon in enumerate(Pokemons):
                print(f"Type {index} to choose {pokemon.name}")
              
            pokemon_choice = int(input("Choose a pokemon! "))

            if Pokemons[pokemon_choice] == current_pokemon:
                ui.message(
                    f"{current_pokemon.name} is already battling!",
                    "red"
                )
                continue
            else:
                if 0 <= pokemon_choice < len(Pokemons):
                    chosen_pokemon = Pokemons[pokemon_choice]
                    print(f"The pokemon you chose was: {chosen_pokemon.name}")
                    return chosen_pokemon
                
                else:
                    print("Invalid pokemon index!")
                    continue
        except (ValueError, IndexError):
            continue

def take_damage(pokemon, damage_number): #Funksjon for å påføre karakterene skade (både motstander og egen)
    pokemon.hp = max(0, pokemon.hp - damage_number)

    ui.message(
        f"{pokemon.name} took {damage_number} damage! \n"
        f"Remanining HP: {pokemon.hp}",
        "yellow"
    )

    return damage_number





# Begynnelse på den turbaserte delen av spillet

chosen_pokemon = choose_a_pokemon() #Bestemmer den første karakteren spiller sender ut
current_pokemon = chosen_pokemon #Brukes til å passe på at brukeren ikke senere kan sende ut en karakter som allerede kjemper

player_turn = True
turn = 1

while (
    any(pokemon.is_alive() for pokemon in Pokemons) 
    and any(pokemon.is_alive() for pokemon in enemy_team)
):
    
    ui.show_battle( # 
        chosen_pokemon,
        active_enemy,
        turn
    )

    if player_turn:

        action = choose_action()

        if action == "fight":
            damage = chosen_pokemon.choose_attack()
            take_damage(active_enemy, damage)

        elif action == "switch":
            chosen_pokemon = choose_a_pokemon(chosen_pokemon)
            ui.message(
                f"{chosen_pokemon.name} has been sent out!",
                "green"
            )

        player_turn = False

    else:
        enemy_damage = active_enemy.enemy_move()
        take_damage(chosen_pokemon, enemy_damage)
        player_turn = True
        turn += 1
        input("Press enter to continue..")

    if active_enemy.hp <= 0:

        ui.message(
            f"{active_enemy.name} has been defeated",
            "green"
        )
        
        if any(pokemon.is_alive() for pokemon in enemy_team):
            active_enemy = choose_enemy_pokemon()
        else:
            ui.message(
                f"All enemy pokemon has been defeated! \n"
                "You win!!",
                "green"
            )
            break
        
    if chosen_pokemon.hp <= 0:
        ui.message(
            f"{chosen_pokemon.name} has been defeated!",
            "red"
        )
        Pokemons.remove(chosen_pokemon)
        
        if any(pokemon.is_alive() for pokemon in Pokemons):
            chosen_pokemon = choose_a_pokemon()
        else:
            ui.message(
                "All your pokemon has been defeated \n"
                "You lose!"
            )
            break