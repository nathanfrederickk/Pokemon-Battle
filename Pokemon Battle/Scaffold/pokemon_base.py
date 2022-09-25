"""
This file contains python code for creating a base class that will be used as 
a base for the other Pokemon's classes.
"""
__author__ = "Chang Yee Vern, Frederick Nathanael Thunardi, Alyssa Ting Sue-Lyn, Shawn Wang Shao En"
__date__ = "28.04.2022"

from abc import ABC, abstractmethod
import random


class PokemonBase(ABC):
    """
    This is an abstract class for pokemon. The pokemon class will inherit all 
    the basic methods and attributes
    
    The best and worst case time complexity for all the methods in this class 
    are O(1) because the methods holds only instance variables or they perform 
    constant time
    """
    BASE_LEVEL = 1
    __TYPES = ["Fire", "Grass", "Water", "None"]
        
    def __init__(self, hp: int, poke_type: str) -> None:
        """
        Constructor for pokemon

        :param hp: The pokemon's initial hp
        :param poke_type: The pokemon's poke_type
        :raises: TypeError: if invalid poke_type
        :raises: ValueError if hp < 0
        """
        if hp < 0:
            raise ValueError("Hp cannot be negative")
        self.hp = hp
        if poke_type not in PokemonBase.__TYPES:
            raise TypeError
        self.poke_type = poke_type
        self.level = PokemonBase.BASE_LEVEL

    def get_hp(self) -> int:
        """
        :return: Returns the current hp of pokemon
        """
        return self.hp
    
    def set_hp(self, hp: int) -> None:
        """
        Set the pokemon's hp

        :param hp: Takes in the new hp
        """
        self.hp = hp

    def get_level(self) -> int:
        """
        :return: Returns the current level of pokemon
        """
        return self.level

    def get_poke_type(self) -> str:
        """
        :return: Returns the class of pokemon
        """
        return self.poke_type

    def is_fainted(self) -> bool:
        """
        :return: Returns true if the pokemon is fainted, false if pokemon is
                 still alive
        """
        return self.hp <= 0

    def level_up(self) -> None:
        """
        Increase the level of pokemon by 1
        """
        self.level += 1
    
    @abstractmethod
    def get_name(self) -> str:
        """
        An abstract method, will be defined while inheriting the base class
        """
        pass

    @abstractmethod
    def get_attack(self) -> int:
        """
        An abstract method, will be defined while inheriting the base class
        """
        pass

    @abstractmethod
    def get_defence(self) -> int:
        """
        An abstract method, will be defined while inheriting the base class
        """
        pass

    @abstractmethod
    def get_speed(self) -> int:
        """
        An abstract method, will be defined while inheriting the base class
        """
        pass

    @abstractmethod
    def get_damage_after_attack(self, damage: int) -> int:
        """
        An abstract method, will be defined while inheriting the base class
        """
        pass

    def __str__(self) -> str:
        """
        :return: Returns the states of the object as a string
        """
        return f"{self.get_name()}'s HP = {self.get_hp()} and level = {self.get_level()}"


class GlitchMon(PokemonBase):
    """
    This is a child class of PokemonBase and a parent class of MissingNo. 
    The MissingNo class will inherit all the basic methods and attributes
    
    The best and worst case time complexity for all the methods in this class 
    are O(1) because they perform constant time
    """
    def increase_HP(self, hp: int) -> None:
        """
        Increase the hp of pokemon

        :param hp: Takes in value to be added into current HP
        :raises: ValueError if hp < 0
        """
        if hp < 0:
            raise ValueError("Hp cannot be negative")
        self.hp += hp
            
    def superpower(self):
        """
        This method has a random chance to choose one of three effects
            - Gain 1 level, or
            - Gain 1 HP, or
            - Gain 1 HP and level
        and the method is called at a 25% chance every time the Pokemon has to 
        defend from an attack
        """
        choice = [0, 1, 2]
        item = random.choice(choice)

        if item == 0:
            self.level = self.get_level() + 1
        elif item == 1:
            self.hp = self.get_hp() + 1
        else:
            self.hp = self.get_hp() + 1
            self.level = self.get_level() + 1
