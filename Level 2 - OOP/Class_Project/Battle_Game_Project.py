#Battle Game Project

#importing the libs
from random import randint, choice

#Coding the three classes (general_character, user, computer)
class GeneralCharacter:
    def __init__(self, name, level, life) -> None:
        self.__name = name
        self.__level = level
        self.__life = life

    def get_name(self):
        return self.__name
    
    def get_level(self):
        return self.__level
    
    def get_life(self):
        return self.__life
    
    def show_details(self):
        return f'Name: {self.get_name()}\nLevel: {self.get_level()}\nLife: {self.get_life()}'
    
    def got_attacked(self, damage):
        self.__life -= damage
        if self.__life < 0:
            self.__life = 0
    
    def attacking(self, target):
        global damage_normal_attack
        damage_normal_attack = self.__level * randint(2,4)
        target.got_attacked(damage_normal_attack)
        print(f"{self.get_name()} has choosen a Normal Attack and it caused {damage_normal_attack} of damage in {target.get_name()}'s life.")

    def super_attack(self, target):
        global damage_super_attack
        damage_super_attack = self.__level * randint(5,6)
        target.got_attacked(damage_super_attack)
        print(f"{self.get_name()} has choosen a Special Attack and it caused {damage_super_attack} of damage in {target.get_name()}'s life.")

    def get_damage(self, choice):
        if choice == 1:
            return damage_normal_attack
        else:
            return damage_super_attack
    
class User(GeneralCharacter):
    def __init__(self, name, level, life, skill) -> None:
        super().__init__(name, level, life)
        self.__skill = skill
    
    def get_skill(self):
        return self.__skill

    def show_details(self):
        return f'{super().show_details()}\nSkill: {self.get_skill()}\n'
    
class Computer(GeneralCharacter):
    def __init__(self, name, level, life, type) -> None:
        super().__init__(name, level, life)
        self.__type = type
    
    def get_type(self):
        return self.__type
    
    def show_details(self):
        return f'{super().show_details()}\nType: {self.get_type()}\n'

# Coding the battles engine

class GameEngine():
    def __init__(self) -> None:
        self.user = User(name= name_user, level=level_user, life=life_user_computer, skill=skill_user)
        self.computer = Computer(name= name_computer, level=level_computer, life=life_user_computer, type=type_computer)
    
    def start_battle(self):
        print(f'\n---STARTING THE BATTLE---')
        print(f'\n{str(self.user.get_name()).upper()} X {str(self.computer.get_name()).upper()}')
        #the engine is bellow
        while self.user.get_life() > 0 and self.computer.get_life() > 0:
            
            print(f'\n--PLAYERS DETAILS--')
            print(self.user.show_details())
            print(self.computer.show_details())

            input('\nPress ENTER to play...')
            try:
                chosen_attack = int(input("What attack would you like to use in this round?\n( [1] - Normal Attack  ||  [2] - Special Attack ) "))
            except Exception as problems:
                print(f'Something went wrong! Here is the problem: {problems}')

            print()
            if chosen_attack == 1:
                self.user.attacking(self.computer)
            else:
                self.user.super_attack(self.computer)
            
            computer_choice = randint(1,2)

            if computer_choice == 1:
                self.computer.attacking(self.user)
            else:
                self.computer.super_attack(self.user)

        #now we have the result of the battle
        print('')
        if self.user.get_life() == 0 and self.computer.get_life() == 0:
            if self.user.get_damage(chosen_attack) > self.computer.get_damage(computer_choice):
                print(f'{self.user.get_name()} won the battle!')
            else:
                print(f'{self.computer.get_name()} won the battle!')
        elif self.user.get_life() > self.computer.get_life():
            print(f'{self.user.get_name()} won the battle!')
        elif self.user.get_life() < self.computer.get_life():
            print(f'{self.computer.get_name()} won the battle!')    
        else:
            print(f'There is a draw. Play again!')     

        return


#User informations Prompt

#dict with heroes
characters = {
    'Aang': 'Air',
    'Katara': 'Water',
    'Sokka': 'None',
    'Toph': 'Earth',
    'Zuko': 'Fire',
    'Iroh': 'Fire',
    'Azula': 'Fire',
    'Ozai': 'Fire',
    'Bumi': 'Earth',
    'Hama': 'Water',
    'Long Feng': 'Earth',
    'Korra': 'Water',
    'Mako': 'Fire',
    'Bolin': 'Earth',
    'Tenzin': 'Air',
    'Lin Beifong': 'Earth',
    'Jinora': 'Air',
    'Ikki': 'Air',
    'Meelo': 'Air',
    'Kya': 'Water',
    'Kuvira': 'Earth',
    'Zaheer': 'Air',
    'Ghazan': 'Earth'
    }
characters_sorted = {key: characters[key] for key in sorted(characters)}

#Program's Title and showing the heroes' name
print(f"=-=- WELCOME TO THE AVATAR'S BATTLE GAME -=-=")
print("\nHere's our heroes: ")
for index, character in enumerate(characters_sorted.keys()):
    if index != len(characters.keys())-1:
        print(f'{character}', end=' - ')
        if index == ((len(characters.keys())-1) / 2):
            print('')
    else:
        print(f'{character}')

#asking info for user
name_user = str(input("\nWhat hero do you choose? ").strip().title())
level_user = int(input("What's your hero's level? "))
life_user_computer = int(100)
skill_user = characters[name_user]

#Computer Informations Random
name_computer = choice(list(characters))
while name_computer == name_user:
    name_computer = choice(list(characters))
variation = 0.3
level_computer = randint(int((level_user - (level_user * variation))),int((level_user + (level_user * variation))))
type_computer = characters[name_computer]

#calling the functions for battle
game = GameEngine()
game.start_battle()