"""
This file contains python code for testing the methods created in the file battle.py
"""
__author__ = "Chang Yee Vern, Frederick Nathanael Thunardi, Alyssa Ting Sue-Lyn, Shawn Wang Shao En"
__date__ = "28.04.2022"

import unittest

from tester_base import TesterBase, captured_output
from battle import Battle
import random


class BattleTester(TesterBase):
    # Test if Battle can be instantiated
    def test_battle(self):
        try:
            b = Battle("Ash", "Misty")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")

    # =============================================================================
    #                           TASK 3 - set_mode_battle()
    # =============================================================================

    # Test for draw result between players given both players have the same pokemons in their team
    def test_set_mode_battle_draw(self):
        b = Battle("Crystal", "Misty")
        try:
            with captured_output("1 2 1\n1 2 1") as (inp, out, err):
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        try:
            assert result == "Draw"
        except AssertionError:
            self.verificationErrors.append(f"It should be a draw: {result}.")

    # Test if player 1 wins given player 1 has more pokemons
    def test_set_mode_battle_player1_win(self):
        b = Battle("Ditto", "Corsola")
        try:
            with captured_output("2 2 2\n2 1 1") as (inp, out, err):
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        try:
            assert result == "Ditto"
        except AssertionError:
            self.verificationErrors.append(f"Ditto should win: {result}.")
            return

        try:
            assert str(b.team1) == "Bulbasaur's HP = 6 and level = 2, Squirtle's HP = 8 and level = 1, " \
                                   "Squirtle's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Team 2 is not correct after battle: {str(b.team1)}")

    # Test if player 2 wins given player 2 has more pokemons
    def test_set_mode_battle_player2_win(self):
        b = Battle("Chansey", "Onix")
        try:
            with captured_output("2 1 0\n2 2 0") as (inp, out, err):
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        try:
            assert result == "Onix"
        except AssertionError:
            self.verificationErrors.append(f"Onix should win: {result}.")
            return

        try:
            assert str(b.team2) == "Bulbasaur's HP = 9 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Team 2 is not correct after battle: {str(b.team2)}")

    # =============================================================================
    #                           TASK 4 - rotating_mode_battle()
    # =============================================================================
    # When the pokemon is the same, result will be draw
    def test_rotating_mode_battle_draw(self):
        b = Battle("Ash", "Misty")
        try:
            with captured_output("1 0 0\n1 0 0") as (inp, out, err):
                result = b.rotating_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        try:
            assert result == "Draw"
        except AssertionError:
            self.verificationErrors.append(f"It should be a draw: {result}.")

    # Test this battle mode when player 1 have better pokemons
    def test_rotating_mode_battle_player1_win(self):
        b = Battle("Ditto", "Corsola")
        try:
            with captured_output("3 2 1\n2 2 2") as (inp, out, err):
                result = b.rotating_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        try:
            assert result == "Ditto"
        except AssertionError:
            self.verificationErrors.append(f"Ditto should win: {result}.")
            return

        try:
            assert str(b.team1) == "Squirtle's HP = 5 and level = 1, Charmander's HP = 7 and level = 3, " \
                                   "Bulbasaur's HP = 5 and level = 2, Bulbasaur's HP = 6 and level = 2"
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(b.team1)}")

    # Test when player 2 wins with more pokemon in this battle mode
    def test_rotating_mode_battle_player2_win(self):
        b = Battle("Chansey", "Onix")
        try:
            with captured_output("2 1 1\n2 2 1") as (inp, out, err):
                result = b.rotating_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        try:
            assert result == "Onix"
        except AssertionError:
            self.verificationErrors.append(f"Onix should win: {result}.")
            return

        try:
            assert str(b.team2) == "Bulbasaur's HP = 5 and level = 2, Bulbasaur's HP = 4 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Team 2 is not correct after battle: {str(b.team2)}")

    # =============================================================================
    #                           TASK 5 - optimised_mode_battle()
    # =============================================================================
    # When both teams have same criteria and number of pokemon
    def test_optimised_mode_battle_draw(self):
        b = Battle("Simon", "Tom")
        try:
            with captured_output("0 1 1\n0 1 1") as (inp, out, err):
                result = b.optimised_mode_battle("hp", "hp")
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        try:
            assert result == "Draw"
        except AssertionError:
            self.verificationErrors.append(f"Should be a Draw, but {result} wins.")

    # When player 1 have better criterion specification than player 2, player 1 wins
    def test_optimised_mode_battle_player1_win(self):
        b = Battle("Simon", "Tom")
        try:
            with captured_output("1 0 1\n0 2 1") as (inp, out, err):
                result = b.optimised_mode_battle("attack", "hp")
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        try:
            assert result == "Simon"
        except AssertionError:
            self.verificationErrors.append(f"Simon should win: {result}.")
            return

        try:
            assert str(b.team1) == "Squirtle's HP = 2 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(b.team1)}")

    # When number of pokemon is the same, but different criterion
    def test_def_optimised_mode_battle_player1_win(self):
        b = Battle("Ash", "Tom")
        try:
            with captured_output("1 0 1\n1 0 1") as (inp, out, err):
                result = b.optimised_mode_battle("defence", "attack")
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        try:
            assert result == "Ash"
        except AssertionError:
            self.verificationErrors.append(f"Ash should win: {result}.")
            return

        try:
            assert str(b.team1) == "Charmander's HP = 7 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(b.team1)}")

    # Tests for different criterion, speed against defence. Player 2 wins.
    def test_spd_optimised_mode_battle_player2_win(self):
        b = Battle("Ash", "Tom")
        try:
            with captured_output("1 0 1\n1 2 1") as (inp, out, err):
                result = b.optimised_mode_battle("defence", "speed")
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        try:
            assert result == "Tom"
        except AssertionError:
            self.verificationErrors.append(f"Tom should win: {result}.")
            return

        try:
            assert str(b.team2) == "Squirtle's HP = 6 and level = 2"
        except AssertionError:
            self.verificationErrors.append(f"Team 2 is not correct after battle: {str(b.team2)}")

    # Tests for speed vs level criterion. Where player 2 wins.
    def test_lvl_optimised_mode_battle_player2_win(self):
        b = Battle("Ash", "Tom")
        try:
            with captured_output("1 0 1\n1 2 1") as (inp, out, err):
                result = b.optimised_mode_battle("speed", "lvl")
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        try:
            assert result == "Tom"
        except AssertionError:
            self.verificationErrors.append(f"Tom should win: {result}.")
            return

        try:
            assert str(b.team2) == "Bulbasaur's HP = 6 and level = 2, Bulbasaur's HP = 9 and level = 1, " \
                                   "Squirtle's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Team 2 is not correct after battle: {str(b.team2)}")

    # =============================================================================
    #                           TASK 6
    # =============================================================================
    # Test when a glitch/MissingNo pokemon appears in team 1 and team 2 in battle mode 0
    def test_set_mode_battle_player2_win_with_MissingNo(self):
        b = Battle("Ditto", "Corsola")
        try:
            random.seed(0)
            with captured_output("2 2 1 1\n2 1 2 1") as (inp, out, err):
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        try:
            assert result == "Ditto"
        except AssertionError:
            self.verificationErrors.append(f"Ditto should win: {result}.")
            return

        try:
            assert str(b.team1) == "MissingNo's HP = 10 and level = 3"
        except AssertionError:
            self.verificationErrors.append(f"Team 2 is not correct after battle: {str(b.team1)}")
    
    # Test when a glitch/MissingNo pokemon appears in team 1 and team 2 in battle mode 1
    def test_rotating_mode_battle_player1_win_with_MissingNo(self):
        b = Battle("Ash", "Tom")
        try:
            random.seed(0)
            with captured_output("1 2 1 1\n1 0 1 1") as (inp, out, err):
                result = b.rotating_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        try:
            assert result == "Ash"
        except AssertionError:
            self.verificationErrors.append(f"Ash should win: {result}.")
            return

        try:
            assert str(b.team1) == "MissingNo's HP = 5 and level = 1, Bulbasaur's HP = 4 and level = 1, " \
                                   "Bulbasaur's HP = 2 and level = 1, Squirtle's HP = 3 and level = 3"
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(b.team1)}")

    # Test when a glitch/MissingNo pokemon appears in team 1 and team 2 in battle mode 2
    def test_optimised_mode_battle_player1_win_with_MissingNo(self):
        b = Battle("Johan", "Tenma")
        try:
            random.seed(0)
            with captured_output("2 1 1 1\n1 2 1 1") as (inp, out, err):
                result = b.optimised_mode_battle("speed", "lvl")
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        try:
            assert result == "Johan"
        except AssertionError:
            self.verificationErrors.append(f"Tenma should win: {result}.")
            return

        try:
            assert str(b.team1) == "Squirtle's HP = 8 and level = 1, MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(b.team1)}")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BattleTester)
    unittest.TextTestRunner(verbosity=0).run(suite)