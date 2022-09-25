"""
This file contains python code for the 4 pokemon classes: Charmander, 
Bulbasaur, Squirtle and MissingNo. Each of these classes contain the base 
stats of each individual pokemon. Those are: name, type effectiveness against 
other pokemon, attack, defence, speed, poke_type, defence systems and priority 
in which would determine the pokemon's position in the ream should the need arises.
"""
__author__ = "Chang Yee Vern, Frederick Nathanael Thunardi, Alyssa Ting Sue-Lyn, Shawn Wang Shao En"
__date__ = "28.04.2022"

from pokemon_base import PokemonBase, GlitchMon
import random


class Charmander(PokemonBase):
    """
    Charmander is the child class of PokemonBase. It inherits all the basic 
    methods and attributes. The base attributes of Charmander is set using 
    class variables.

    The best and worst case time complexity for all the methods in this class 
    are O(1) because the methods perform in constant time
    """
    POKE_NAME = "Charmander"
    TYPE_EFFECTIVENESS = {"Fire": 1, "Water": 0.5, "Grass": 2, "None": 1}
    BASE_HP = 7
    BASE_ATTACK = 6
    BASE_DEFENCE = 4
    BASE_SPEED = 7
    POKE_TYPE = "Fire"
    PRIORITY = 4  # used in task 5

    def __init__(self) -> None:
        """
        Constructor for Charmander
        """
        PokemonBase.__init__(self, Charmander.BASE_HP, Charmander.POKE_TYPE)

    def get_name(self) -> str:
        """
        Gets the name of the pokemon
        
        :return: "Charmander"
        """
        return self.POKE_NAME

    def get_attack(self) -> int:
        """
        Gets the pokemon's attack value with respect to the level
        
        :return: 6 + current level
        """
        return Charmander.BASE_ATTACK + self.get_level()

    def get_defence(self) -> int:
        """
        Gets the pokemon's defence value
        
        :return: 4
        """
        return Charmander.BASE_DEFENCE

    def get_speed(self) -> int:
        """
        Gets the speed of the pokemon with respect to the level
        
        :return: 7 + current level
        """
        return Charmander.BASE_SPEED + self.get_level()

    def get_damage_after_attack(self, damage: int) -> int:
        """
        Gets the damage the pokemon receives with respect to the defence value
        
        :param damage: total attack power of opposing pokemon
        :return: hp after receiving damage from the opposing pokemon
        """
        if damage > self.get_defence():
            self.hp -= damage
            return self.hp
        else:
            self.hp -= (damage // 2)
            return self.hp


class Bulbasaur(PokemonBase):
    """
    Bulbasaur is the child class of PokemonBase. It inherits all the basic 
    methods and attributes. The base attributes of Bulbasaur is set using 
    class variables.

    The best and worst case time complexity for all the methods in this class 
    are O(1) because the methods perform in constant time
    """
    POKE_NAME = "Bulbasaur"
    TYPE_EFFECTIVENESS = {"Fire": 0.5, "Water": 2, "Grass": 1, "None": 1}
    BASE_HP = 9
    BASE_ATTACK = 5
    BASE_DEFENCE = 5
    BASE_SPEED = 7
    POKE_TYPE = "Grass"
    PRIORITY = 3  # used in task 5

    def __init__(self) -> None:
        """
        Constructor for Bulbasaur
        """
        PokemonBase.__init__(self, Bulbasaur.BASE_HP, Bulbasaur.POKE_TYPE)

    def get_name(self) -> str:
        """
        Gets the name of the pokemon
        
        :return: "Bulbasaur"
        """
        return self.POKE_NAME

    def get_attack(self) -> int:
        """
        Gets the pokemon's attack value
        
        :return: 5
        """
        return Bulbasaur.BASE_ATTACK

    def get_defence(self) -> int:
        """
        Gets the pokemon's defence value
        
        :return: 5
        """
        return Bulbasaur.BASE_DEFENCE

    def get_speed(self) -> int:
        """
        Gets the speed of the pokemon with respect to the level
        
        :return: 7 + current level // 2
        """
        return Bulbasaur.BASE_SPEED + self.get_level() // 2

    def get_damage_after_attack(self, damage: int) -> int:
        """
        Gets the damage the pokemon receives with respect to the defence value
        
        :param damage: total attack power of opposing pokemon
        :return: hp after receiving damage from the opposing pokemon
        """
        if damage > self.get_defence() + 5:
            self.hp -= damage
            return self.hp
        else:
            self.hp -= (damage // 2)
            return self.hp


class Squirtle(PokemonBase):
    """
    Squirtle is the child class of PokemonBase. It inherits all the basic 
    methods and attributes. The base attributes of Squirtle is set using 
    class variables.

    The best and worst case time complexity for all the methods in this class 
    are O(1) because the methods perform in constant time
    """
    POKE_NAME = "Squirtle"
    TYPE_EFFECTIVENESS = {"Fire": 2, "Water": 1, "Grass": 0.5, "None": 1}
    BASE_HP = 8
    BASE_ATTACK = 4
    BASE_DEFENCE = 6
    BASE_SPEED = 7
    POKE_TYPE = "Water"
    PRIORITY = 2  # used in task 5

    def __init__(self) -> None:
        """
        Constructor for Squirtle
        """
        PokemonBase.__init__(self, Squirtle.BASE_HP, Squirtle.POKE_TYPE)

    def get_name(self) -> str:
        """
        Gets the name of the pokemon
        
        :return: "Squirtle"
        """
        return self.POKE_NAME

    def get_attack(self) -> int:
        """
        Gets the pokemon's attack value with respect to the level
        
        :return: 4 + current level // 2
        """
        return Squirtle.BASE_ATTACK + self.get_level() // 2

    def get_defence(self) -> int:
        """
        Gets the pokemon's defence value with respect to the pokemon level
        
        :return: 6 + current level
        """
        return Squirtle.BASE_DEFENCE + self.get_level()

    def get_speed(self) -> int:
        """
        Gets the speed of the pokemon
        
        :return: 7
        """
        return Squirtle.BASE_SPEED

    def get_damage_after_attack(self, damage: int) -> int:
        """
        Gets the damage the pokemon receives with respect to the defence value
        
        :param damage: total attack power of opposing pokemon
        :return: hp after receiving damage from the opposing pokemon
        """
        if damage > self.get_defence() * 2:
            self.hp -= damage
            return self.hp
        else:
            self.hp -= (damage // 2)
            return self.hp

class MissingNo(GlitchMon):
    """
    MissingNo is the child class of GlitchMon. It inherits all the basic
    methods and attributes. The base attributes of MissingNo is set using
    class variables.

    The best and worst case time complexity for all the methods in this class
    are O(1) because the methods perform in constant time
    """
    POKE_NAME = "MissingNo"
    TYPE_EFFECTIVENESS = {"Fire": 1, "Water": 1, "Grass": 1, "None": 1}
    AVERAGE_HP = (7 + 9 + 8) // 3
    AVERAGE_ATTACK = (6 + 1 + 5 + 4 + (1 // 2)) // 3
    AVERAGE_DEFENCE = (4 + 5 + 6 + 1) // 3
    AVERAGE_SPEED = (7 + 1 + 7 + (1 // 2) + 7) // 3
    POKE_TYPE = "None"
    PERCENT_CHANCE_ONETHIRD = 3
    PRIORITY = 1  # used in task 5

    def __init__(self) -> None:
        """
        Constructor for MissingNo
        """
        PokemonBase.__init__(self, MissingNo.AVERAGE_HP, MissingNo.POKE_TYPE)

    def get_name(self) -> str:
        """
        Gets the name of the pokemon
        
        :return: "MissingNo"
        """
        return self.POKE_NAME

    def get_attack(self) -> int:
        """
        Gets the pokemon's attack value
        
        :return: 5 + 1 for each level up
        """
        return MissingNo.AVERAGE_ATTACK + self.get_level() - 1

    def get_defence(self) -> int:
        """
        Gets the pokemon's defence value
        
        :return: 5 + 1 for each level up
        """
        return MissingNo.AVERAGE_DEFENCE + self.get_level() - 1

    def get_speed(self) -> int:
        """
        Gets the speed of the pokemon with respect to the level.
        
        :return: 7 + 1 for each level up
        """
        return MissingNo.AVERAGE_SPEED + self.get_level() - 1

    # Gets the level of the pokemon class and +1 level and hp to the pokemon class.
    def level_up(self) -> None:
        """
        Increases the level of MissingNo
        
        :return: None
        """
        self.level += 1
        self.increase_HP(1)

    def get_damage_after_attack(self, damage: int) -> int:
        """
        Gives MissingNo 25% chance to activate superpower or gets the damage
        the pokemon receives with respect to the defence value obtained from 
        a random system used by the other 3 pokemons.
        
        :param damage: total attack power of opposing pokemon
        :return: hp after receiving damage from the opposing pokemons
        """
        # Use array to implement the 25% chance of activating the superpower
        choice = [0, 0, 1, 0]
        item = random.choice(choice)

        if item == 1:
            self.superpower()
        else:
            # Random choice for random defence system
            choice = [0, 1, 2]
            item = random.choice(choice)

            # System used by Charmander
            if item == 0:
                if damage > self.get_defence():
                    self.hp -= damage
                else:
                    self.hp -= (damage // 2)

            # System used by Bulbasaur
            elif item == 1:
                if damage > self.get_defence() + 5:
                    self.hp -= damage
                else:
                    self.hp -= (damage // 2)

            # System used by Squirtle
            else:
                if damage > self.get_defence() * 2:
                    self.hp -= damage
                else:
                    self.hp -= (damage // 2)
        return self.hp