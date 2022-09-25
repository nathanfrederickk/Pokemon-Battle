"""
This file contains python code for creating the PokeTeam according to the 
battle mode chosen.
- battle mode 1: PokeTeam is created using stack ADT
- battle mode 2: PokeTeam is created using queue ADT
- battle mode 3: PokeTeam is created using sorted list ADT and it's sorted 
  according to the criterion given by the user
"""
__author__ = "Chang Yee Vern, Frederick Nathanael Thunardi, Alyssa Ting Sue-Lyn, Shawn Wang Shao En"
__date__ = "28.04.2022"

from pokemon_base import PokemonBase
from pokemon import Charmander, Bulbasaur, Squirtle, MissingNo
from queue_adt import CircularQueue
from stack_adt import ArrayStack
from array_sorted_list import ArraySortedList, ListItem


class PokeTeam:
    """
    This is a class that instantiates the pokemons.
    """
    LIMIT = 6                   # Sets the team limit to 6
    SET_MODE_BATTLE = 0
    ROTATING_MODE_BATTLE = 1
    OPTIMISED_MODE_BATTLE = 2

    def __init__(self, name: str) -> None:
        """
        Instantiates a PokeTeam instance.

        The best and worst case complexity is O(1) because it only assign a 
        value to instance variables.
        """
        self.trainer_name = name
        self.team = None
        self.battle_mode = None
        self.unique_pokemon_in_team = []

    def choose_team(self, battle_mode: int = 0, criterion: str = None) -> None:
        """
        Prompts the user to input number of pokemon and assigns the number of 
        pokemon in the team.  Will prompt user repeatedly until the correct 
        team format is given.
        
        The best and worst case time complexity for this method is O(n)
        because its calling __assign_team with a time complexity of O(n)
        for best and worst case.

        :param battle_mode: Can only input 1, 2 or 3 <- Only 3 modes to choose from
        :param criterion: Optional, but if required for battle mode 3 to sort the team according to the input given
        :raises: ValueError if incorrect battle mode
        """
        if battle_mode < 0 or battle_mode > 2:  # if the battle mode is not in [0,1,2]
            raise ValueError("Battle mode cannot be anything other than either 0, 1 or 2")

        print(f"Howdy {self.trainer_name}! Choose your team as C B S")
        print("where C is the number of Charmanders")
        print("      B is the number of Bulbasaurs")
        print("      S is the number of Squirtles")

        self.battle_mode = battle_mode
        team = input().split(' ')

        # Check to see if the input is a positive integer
        try:
            for i in team:
                check = i.isdigit()
                if check is False:
                    raise ValueError("Please input positive integer for PokeTeam")
        except ValueError as e:
            print(e)
            self.choose_team(self.battle_mode, criterion)
            return

        team = [int(i) for i in team]

        if len(team) == 3:  # assign user input to c b s m respectively
            c, b, s = team[0], team[1], team[2]
            m = 0           # Set value to MissingNo to 0 as default

        else:
            c, b, s, m = team[0], team[1], team[2], team[3]

        # Without criterion
        if self.battle_mode == PokeTeam.SET_MODE_BATTLE or self.battle_mode == PokeTeam.ROTATING_MODE_BATTLE:
            self.__assign_team(c, b, s, m)

        # if battle mode is 2, the criterion parameter will be assigned
        elif battle_mode == PokeTeam.OPTIMISED_MODE_BATTLE:
            self.__assign_team(c, b, s, m, criterion.lower())  # With criterion

    def __assign_team(self, charm: int, bulb: int, squir: int, missing: int, criterion: str = None) -> None:
        """
        Assign the pokemon to self.team based on the battle mode.
        
        Best and worst case time complexity for this method is O(n), where n is
        the total number of pokemon (n = charm + bulb + squir + missing)

        :param charm: Number of Charmander
        :param bulb: Number of Bulbasaur
        :param squir: Number of Squirtle
        :param missing: Number of MissingNo
        :param criterion: Optional, but it is used to sort the team according to the input given
        :raises: ValueError 
            i) if missing is not 0 or 1
            ii) if any of the number of pokemon is negative value
            iii) if the number of pokemon is greater than 6
        """
        try:
            if missing > 1:
                raise ValueError("MissingNo cannot be more than 1, please input the team again")

            if charm + bulb + squir + missing > self.LIMIT:
                raise ValueError("Team is too big, please input the team again")

        except ValueError as e:
            print(e)
            self.choose_team(self.battle_mode, criterion)
        else:  # assign the pokemon accordingly
            if self.battle_mode == PokeTeam.SET_MODE_BATTLE:  # Uses Stack ADT (Last in first out)
                # Assigns space for the list
                self.team = ArrayStack(self.LIMIT)
                for _ in range(missing):
                    self.team.push(MissingNo())
                for _ in range(squir):
                    self.team.push(Squirtle())
                for _ in range(bulb):
                    self.team.push(Bulbasaur())
                for _ in range(charm):
                    self.team.push(Charmander())
                    
            elif self.battle_mode == PokeTeam.ROTATING_MODE_BATTLE:  # Uses Queue ADT (First in first out)
                # Assigns space for the list
                self.team = CircularQueue(self.LIMIT)
                for _ in range(charm):
                    self.team.append(Charmander())
                for _ in range(bulb):
                    self.team.append(Bulbasaur())
                for _ in range(squir):
                    self.team.append(Squirtle())
                for _ in range(missing):
                    self.team.append(MissingNo())

            elif self.battle_mode == PokeTeam.OPTIMISED_MODE_BATTLE:  # Uses Sorted List ADT
                # Assigns space for the list
                self.team = ArraySortedList(self.LIMIT)
                for _ in range(charm):
                    p = Charmander()
                    self.team.optimized_add(ListItem(p, self.__get_key(p, criterion)))
                    self.unique_pokemon_in_team.append(p)
                for _ in range(bulb):
                    p = Bulbasaur()
                    self.team.optimized_add(ListItem(p, self.__get_key(p, criterion)))
                    self.unique_pokemon_in_team.append(p)
                for _ in range(squir):
                    p = Squirtle()
                    self.team.optimized_add(ListItem(p, self.__get_key(p, criterion)))
                    self.unique_pokemon_in_team.append(p)
                for _ in range(missing):
                    p = MissingNo()
                    self.team.optimized_add(ListItem(p, self.__get_key(p, criterion)))
                    self.unique_pokemon_in_team.append(p)

    def __get_key(self, pokemon: PokemonBase, criterion: str):
        """
        Return the current stats based on criterion
        
        Best and worst time complexity for this method is O(1) as it only
        returns the value.

        :param pokemon: Current pokemon
        :param criterion: Used to get the value of the input given
        :return: Equivalent value to input given
        :raises: ValueError if invalid criterion
        """
        if criterion == "hp":
            return pokemon.get_hp()
        elif criterion == "attack":
            return pokemon.get_attack()
        elif criterion == "defence":
            return pokemon.get_defence()
        elif criterion == "speed":
            return pokemon.get_speed()
        elif criterion == "lvl":
            return pokemon.get_level()
        else:
            raise ValueError("Invalid criterion")

    def __str__(self) -> str:
        """
        :return: Returns the state of each pokemon in the team

        The best and worst case time complexity for this method  is O(1) as
        it only returns the string.
        """
        if self.team is None:
            return ""
        return str(self.team)