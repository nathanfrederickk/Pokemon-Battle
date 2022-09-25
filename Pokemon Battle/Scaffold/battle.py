"""
This file contains python code for stimulating the battle between two teams 
and producing a winner; or a draw.
"""
__author__ = "Chang Yee Vern, Frederick Nathanael Thunardi, Alyssa Ting Sue-Lyn, Shawn Wang Shao En"
__date__ = "28.04.2022"

from poke_team import PokeTeam
from pokemon_base import PokemonBase
from stack_adt import ArrayStack
from queue_adt import CircularQueue
from array_sorted_list import ArraySortedList, ListItem


class Battle:
    """
    Battle class stimulates the battle between 2 pokemon teams. It also 
    determines the winning team.
    """
    def __init__(self, trainer_one_name: str, trainer_two_name: str) -> None:
        """
        Create an instances of team1 and team2 and also set battle mode to none.
        
        Best and worst case time complexity for this method is O(1) because 
        the methods holds only instance variables
        """
        self.team1 = PokeTeam(trainer_one_name)
        self.team2 = PokeTeam(trainer_two_name)
        self.battle_mode = None

    def set_mode_battle(self) -> str:
        """
        Simulates combat between 2 players. Prompt user for the starting 
        pokemon and create 2 teams for simulating battle and set battle 
        mode to 0.

        :return: Winner or Draw

        Best and worst case time complexity for this method is O(n) because 
        it takes linear time for calling the method __commence_battle().
        """
        self.battle_mode = 0  # Sets the battle mode to 0
        self.team1.choose_team(self.battle_mode)    # Allocates the pokemon into team1
        self.team2.choose_team(self.battle_mode)    # Allocates the pokemon into team2
        return self.__commence_battle(self.team1, self.team2, self.battle_mode)  # Conducts the battle

    def rotating_mode_battle(self) -> str:  # Sets the battle mode to 1
        """
        Simulates combat between 2 players. Prompt user for the starting 
        pokemon and create 2 teams for simulating battle and set battle 
        mode to 1.

        :return: Winner or Draw
        
        Best and worst case time complexity for this method is O(n) because 
        it takes linear time for calling the method __commence_battle().
        """
        self.battle_mode = 1
        self.team1.choose_team(self.battle_mode)    # Allocates the pokemon into team1
        self.team2.choose_team(self.battle_mode)    # Allocates the pokemon into team2
        return self.__commence_battle(self.team1, self.team2, self.battle_mode)  # Conducts the battle

    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) -> str:
        """
        Simulates combat between 2 players. Prompt user for the starting 
        pokemon and create 2 teams for simulating battle and set battle
        mode to 2.
        
        Best and worst case time complexity for this method is O(n^2) because
        it takes linear time for calling the method __commence_battle().

        :param criterion_team1: Accepted input: ["hp", "attack", "defence", "speed", "lvl"]
        :param criterion_team2: Accepted input: ["hp", "attack", "defence", "speed", "lvl"]
        :return: Winner or Draw
        :raises: ValueError if criterion_team1 or criterion_team2 is none or not in __OPTIONS
        """
        __OPTIONS = ["hp", "attack", "defence", "speed", "lvl"]
        try:
            if not isinstance(criterion_team1, str) and not isinstance(criterion_team2, str):
                raise ValueError("Please input string for criterion")
        except ValueError as e:
            print(e)

        if criterion_team1 is None or criterion_team2 is None or criterion_team1.lower() not in __OPTIONS or \
                criterion_team2.lower() not in __OPTIONS:
            raise ValueError("incorrect input criterion")

        self.battle_mode = 2  # Sets the battle mode to 2
        self.team1.choose_team(self.battle_mode, criterion_team1)   # Allocates the pokemon into team1 and sort them according to the criterion from user
        self.team2.choose_team(self.battle_mode, criterion_team2)   # Allocates the pokemon into team2 and sort them according to the criterion from user
        return self.__commence_battle(self.team1, self.team2, self.battle_mode, criterion_team1, criterion_team2)  # Conducts the battle

    def __get_criterion(self, pokemon: PokemonBase, criterion: str) -> int:
        """
        Get the criterion of each pokemon based on the input criterion.
        
        Best and worst case time complexity for this method is O(1) because 
        it perform in constant time.

        :param pokemon: Current pokemon fighting
        :param criterion: Accepted input: ["hp", "attack", "defence", "speed", "lvl"]
        :return: Return equivalent value to criterion input
        """
        res = None  # Initialise variable value
        if criterion == "hp":  
            res = pokemon.get_hp()  
        elif criterion == "attack":
            res = pokemon.get_attack()
        elif criterion == "defence":
            res = pokemon.get_defence()
        elif criterion == "speed":
            res = pokemon.get_speed()
        elif criterion == "lvl":
            res = pokemon.get_level()
        return res

    def __commence_battle(self, team1: PokeTeam, team2: PokeTeam, battle_mode: int, criterion_team1: str = None,
                          criterion_team2: str = None) -> str:
        """
        Conducts combat between 2 PokeTeams and determines the winner.
        
        Best and worst case time complexity for this method is O(n^2)

        :param team1: first team
        :param team2: second team
        :param battle_mode: Accepted input: [0, 1, 2]
        :param criterion_team1: Accepted input: ["hp", "attack", "defence", "speed", "lvl"]
        :param criterion_team2: Accepted input: ["hp", "attack", "defence", "speed", "lvl"]
        :return: Winner or Draw
        :raises: ValueError if battle mode is invalid
        """
        if battle_mode not in [0, 1, 2]:  # Checks if the battle mode is correctly entered
            raise ValueError("Invalid battle_mode")

        if battle_mode == 0:
            current = ArrayStack.pop    # Simplifies the code, allocating the pop function that pops the value, to the variable.
            add = ArrayStack.push       # Simplifies the code, allocating the push function that pushes the last element to the first, to the variable.

        elif battle_mode == 1:
            current = CircularQueue.serve   # Simplifies the code, allocating the serve function that shows the first element in the list to the variable
            add = CircularQueue.append      # Simplifies the code, allocates the append function that appends a value to the element, to the variable.

        else:
            current = ArraySortedList.delete_at_index   # Simplifies the code, allocating the serve function that shows the first element in the list to the variable

        # Runs while any of the team is not empty
        while not team1.team.is_empty() and not team2.team.is_empty():
            if battle_mode == 0 or battle_mode == 1:    # If the battle mode is 1 or 0 it will remove the first element in the list
                p1 = current(team1.team)
                p2 = current(team2.team)
            else:  # Else it will remove value in the array sorted list at the last index
                p1 = current(team1.team, len(team1.team) - 1)
                p2 = current(team2.team, len(team2.team) - 1)
                
                # Code to check if all the other pokemons other than MissingNo have battled.
                if len(team1.unique_pokemon_in_team) > 1:
                    if p1.value.get_name() == "MissingNo":              # If current pokemon to battle is MissingNo
                        temp = p1
                        p1 = current(team1.team, len(team1.team) - 1)   # Take the pokemon after MissingNo to replace it
                        team1.team.optimized_add(temp)                  # Put MissingNo back into the team
                        if p1.value in team1.unique_pokemon_in_team:    # Mark current pokemon as battled if not yet done so
                            team1.unique_pokemon_in_team.remove(p1.value)
                    elif p1.value in team1.unique_pokemon_in_team:      # If current pokemon is not MissingNo
                        team1.unique_pokemon_in_team.remove(p1.value)   # Mark current pokemon as battled if not yet done so

                if len(team2.unique_pokemon_in_team) > 1:
                    if p2.value.get_name() == "MissingNo":              # If current pokemon to battle is MissingNo
                        temp = p2
                        p2 = current(team2.team, len(team2.team) - 1)   # Take the pokemon after MissingNo to replace it
                        team2.team.optimized_add(temp)                  # Put MissingNo back into the team
                        if p2.value in team2.unique_pokemon_in_team:    # Mark current pokemon as battled if not yet done so
                            team2.unique_pokemon_in_team.remove(p2.value)
                    elif p2.value in team2.unique_pokemon_in_team:      # If current pokemon is not MissingNo
                        team2.unique_pokemon_in_team.remove(p2.value)   # Mark current pokemon as battled if not yet done so
                        
            # If battle mode is 0 or 1
            if battle_mode == 0 or battle_mode == 1:
                # Starts and ends the battle round, reduce the hp of the losing pokemon each round
                self.__start_round(p1, p2)
                self.__end_round(p1, p2)

                # Rearrange the list according to battle modes if the pokemon is not fainted
                if not p1.is_fainted():
                    add(team1.team, p1)
                if not p2.is_fainted():
                    add(team2.team, p2)
                    
            # If battle mode is 2
            elif battle_mode == 2:
                # Starts and ends the battle round, reduce the hp of the losing pokemon
                self.__start_round(p1.value, p2.value)
                self.__end_round(p1.value, p2.value)

                # Sets the criterion and sort the pokemon list after each round
                criterion_1 = self.__get_criterion(p1.value, criterion_team1.lower())
                criterion_2 = self.__get_criterion(p2.value, criterion_team2.lower())

                # Rearrange the list according to battle modes if the pokemon is not fainted
                if not p1.value.is_fainted():
                    team1.team.optimized_add(ListItem(p1.value, criterion_1))
                if not p2.value.is_fainted():
                    team2.team.optimized_add(ListItem(p2.value, criterion_2))

        # Returns the result after combat
        if team1.team.is_empty() and team2.team.is_empty():
            return "Draw"
        elif team1.team.is_empty():
            return self.team2.trainer_name
        elif team2.team.is_empty():
            return self.team1.trainer_name

    def __start_round(self, p1: PokemonBase, p2: PokemonBase) -> None:
        """
        Simulates an attack round where both pokemons attack each other based 
        on their speed.
        
        Best and worst case time complexity for this method is O(1) as it
        perform in constant time.

        :param p1: Current pokemon to battle from team1
        :param p2: Current pokemon to battle from team2
        """
        # if pokemon 1 faster than pokemon 2
        if p1.get_speed() > p2.get_speed():
            damage = self.__attack(p1, p2)
            p2.get_damage_after_attack(damage)
            if not p2.is_fainted():  # retaliate
                damage = self.__attack(p2, p1)
                p1.get_damage_after_attack(damage)

        # if pokemon 2 faster than pokemon 1
        elif p2.get_speed() > p1.get_speed():
            damage = self.__attack(p2, p1)
            p1.get_damage_after_attack(damage)
            if not p1.is_fainted():  # retaliate
                damage = self.__attack(p1, p2)
                p2.get_damage_after_attack(damage)

        # if both same speed
        else:
            damage = self.__attack(p1, p2)
            p2.get_damage_after_attack(damage)
            damage = self.__attack(p2, p1)
            p1.get_damage_after_attack(damage)

    def __attack(self, attacker: PokemonBase, defender: PokemonBase) -> int:
        """
        Calculates the damage of attacker Pokemon inflicted on defender Pokemon.
        
        Beat and worst case time complexity for this method is O(1) as it
        perform in constant time.

        :param attacker: Attacking pokemon
        :param defender: Defending pokemon
        :return: damage inflicted
        """
        damage = attacker.get_attack()
        damage *= attacker.TYPE_EFFECTIVENESS[defender.poke_type]
        return int(damage)
    
    def __end_round(self, p1: PokemonBase, p2: PokemonBase) -> None:
        """
        Simulates the ending round based on the pokemon's hp. Increment 
        pokemon's level by 1 if pokemon faints another pokemon. Else, decrement 
        both of their hp by 1.
        
        Beat and worst case time complexity for this method is O(1) as it
        perform in constant time.

        :param p1: Current pokemon battling from team1
        :param p2: Current pokemon battling from team2
        """
        if p1.is_fainted() and not p2.is_fainted():
            p2.level_up()
        elif p2.is_fainted() and not p1.is_fainted():
            p1.level_up()
        elif not p1.is_fainted() and not p2.is_fainted():
            p1.hp -= 1
            p2.hp -= 1