import time
import numpy as np
import sys
import json
 
 
# Delay printing
 
def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
 
 
# Create the class
class Pokemon:
    def __init__(self, name, types, moves, EVs, health='======'):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 50  # Amount of health bars
 
    def fight(self, Pokemon2):
        # Allow two pokemon to fight each other
 
        # Print fight information
        print("-----POKEMONE BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3 * (1 + np.mean([self.attack, self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3 * (1 + np.mean([Pokemon2.attack, Pokemon2.defense])))
 
        time.sleep(2)
 
        # Consider type advantages
        # version = ['Fire', 'Water', 'Grass', 'Bug', 'Ice', 'Normal', 'Psychic']
        weaker_types = {'fire': ['water',],
                        'normal': ['steel'],
                        'water': ['grass'],
                        'ground': ['bug', 'grass'],
                        'grass': ['fire'],
                        'bug': ['flying', 'grass', 'ground'],
                        'poison': ['ground', 'poison', 'steel'],
                        'ice': ['steel', 'fire', 'water', 'ice'],
                        'fairy': ['poison', 'steel', 'fire'],
                        'steel': ['steel', 'fire', 'water']}

 
        stronger_types = {'fire': ['bug', 'steel', 'grass', 'ice'],
                          'water': ['fire', 'steel', 'water', 'ice'],
                          'ground': ['poison'],
                          'grass': ['ground', 'water', 'grass'],
                          'bug': ['ground', 'grass'],
                          'poison': ['grass', 'fairy'],
                          'flying': ['ground', 'bug', 'grass'],
                          'fairy': ['bug'],
                          'steel': ['normal', 'poison', 'bug', 'steel', 'grass', 'ice', 'fairy']
                          }
 
        # Both are same type
        if self.types == Pokemon2.types:
            string_1_attack = '\nIts not very effective...'
            string_2_attack = '\nIts not very effective...'
 
        # Pokemon is weaker
        elif Pokemon2.types in weaker_types[self.types.lower()]:
            Pokemon2.attack *= 2
            Pokemon2.defense *= 2
            self.attack /= 2
            self.defense /= 2
            string_1_attack = '\nIts not very effective...'
            string_2_attack = '\nIts super effective!'
 
        # Pokemon is stronger
        elif Pokemon2.types in stronger_types[self.types.lower()]:
            self.attack *= 2
            self.defense *= 2
            Pokemon2.attack /= 2
            Pokemon2.defense /= 2
            string_1_attack = '\nIts super effective!'
            string_2_attack = '\nIts not very effective...'

        # If pokemon have no weakness to each other


 
        # Now for the actual fighting...
        # Continue while pokemon still have health
        while (self.bars > 0) and (Pokemon2.bars > 0):
            # Print the health of each pokemon
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
 
            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i + 1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{self.name} used {self.moves[index - 1]}!")
            time.sleep(1)
            delay_print(string_1_attack)
 
            # Determine damage
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""
 
            # Add back bars plus defense boost
            for j in range(int(Pokemon2.bars + .1 * Pokemon2.defense)):
                Pokemon2.health += "="
 
            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)
 
            # Check to see if Pokemon fainted
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' fainted.')
                break
 
            # Pokemon2s turn
 
            print(f"Go {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i + 1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index - 1]}!")
            time.sleep(1)
            delay_print(string_2_attack)
 
            # Determine damage
            self.bars -= Pokemon2.attack
            self.health = ""
 
            # Add back bars plus defense boost
            for j in range(int(self.bars + .1 * self.defense)):
                self.health += "="
 
            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)
 
            # Check to see if Pokemon fainted
            if self.bars <= 0:
                delay_print("\n..." + self.name + ' fainted.')
                break
 
        delay_print(f"\nChoose your next Pokemon\n")
 
 
class PokeCardDex():
    def __init__(self, json_file_path=None):
        # NOTE: It is important to handle the case where no path is passed in
        # meaning that json_file_path has a value of None.
        pass
 
    def set_order(self, order):
        pass
 
    def battle(self, challenger_party):
        pass
 
    def heal_party(self):
        pass
 
    def add_to_party(self, pokemon):
        pass
 
 
if __name__ == '__main__':
    # Create Pokemon
    my_dex = PokeCardDex('pokemon_party.json')
    rival_dex = PokeCardDex()
    charmander = Pokemon('Charmander', 'fire', ['Scratch', 'Ember'], {'ATTACK': 10, 'DEFENSE': 50})
    venusaur = Pokemon('Venusaur', 'grass', ['Vine'], {'ATTACK': 35, 'DEFENSE': 40})
    charizard = Pokemon('Charizard', 'fire',['Tail Smash', 'Flamethrower'], {'ATTACK': 40, 'DEFENSE': 100})
    seaking = Pokemon('Seaking', 'water', ['Horn Attack', 'Waterfall'], {'ATTACK': 30, 'DEFENSE': 70})
    venonat = Pokemon('Venonat', 'bug', ['Stun Spore', 'Leeech Life'], {'ATTACK': 10, 'DEFENSE': 40})
    ninetales = Pokemon('Ninetales', 'fire', ['Fireblast'], {'ATTACK': 80, 'DEFENSE': 80})
    butterfree = Pokemon('Butterfree', 'bug', ['Spiral Drain'], {'ATTACK':40, 'DEFENSE': 80}) 
    cloyster = Pokemon('Cloyster', 'ice', ['Lick', 'Auto Fire'], {'ATTACK': 25, 'DEFENSE': 80})
    chikorita = Pokemon('Chikorita', 'grass', ['Razor Leaf'], {'ATTACK': 20, 'DEFENSE': 50})



    charizard.fight(seaking)