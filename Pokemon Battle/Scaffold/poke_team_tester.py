"""
This file contains python code for testing the methods created in the file 
poke_team.py
"""
__author__ = "Chang Yee Vern, Frederick Nathanael Thunardi, Alyssa Ting Sue-Lyn, Shawn Wang Shao En"
__date__ = "28.04.2022"

import unittest

from tester_base import TesterBase, captured_output
from poke_team import PokeTeam


class TestPokeTeam(TesterBase):
    # =============================================================================
    #                           Tests for Task 2 & 6
    # =============================================================================
    # Test adding ONLY Charmander into the team
    def test_only_charmander(self):
        try:
            team = PokeTeam("Ash")
            with captured_output("1 0 0") as (inp, out, err):
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Charmander's HP = 7 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")

    # Test adding ONLY Bulbasaur into the team
    def test_only_bulbasaur(self):
        try:
            team = PokeTeam("Fiona")
            with captured_output("0 1 0") as (inp, out, err):
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Fiona's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Bulbasaur's HP = 9 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")

    # Test adding ONLY Squirtle into the team
    def test_only_squirtle(self):
        try:
            team = PokeTeam("Penny")
            with captured_output("0 0 1") as (inp, out, err):
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Penny's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Squirtle's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")

    # Test adding ONLY MissingNo into the team
    def test_only_MissingNo(self):
        try:
            team = PokeTeam("Loki")
            with captured_output("0 0 0 1") as (inp, out, err):
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Loki's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")

    # Test creating a random team
    def test_random_team(self):
        try:
            team = PokeTeam("Misty")
            with captured_output("1 2 1 1") as (inp, out, err):
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Misty's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, " \
                                "Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1, " \
                                "MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")

    # =============================================================================
    #                           Tests for Task 3 & 6
    # =============================================================================
    # Test with battle_mode = 0
    def test_choose_team_battle_mode_0(self):
        try:
            team = PokeTeam("Ash")
            with captured_output("3 3 1\n3 2 1"):
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Charmander's HP = 7 and level = 1, " \
                                "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, " \
                                "Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")
            return

        # Test with MissingNo
        try:
            team = PokeTeam("Ash")
            with captured_output("2 1 1 2\n2 1 1 1"):
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Charmander's HP = 7 and level = 1, " \
                                "Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1, " \
                                "MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")

    # =============================================================================
    #                           Tests for Task 4 & 6
    # =============================================================================
    # test with battle_mode = 1
    def test_choose_team_battle_mode_1(self):
        try:
            team = PokeTeam("Misty")
            with captured_output("1 1 1"):
                team.choose_team(1, None)
        except Exception as e:
            self.verificationErrors.append(f"Misty's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, " \
                                "Squirtle's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")
            return

        # Test with MissingNo
        try:
            team = PokeTeam("Misty")
            with captured_output("1 1 1 2\n1 1 1 1"):
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Misty's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, " \
                                "Squirtle's HP = 8 and level = 1, MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")

    # =============================================================================
    #                           Tests for Task 5 & 6
    # =============================================================================
    # test with battle_mode = 2 with no criterion
    def test_choose_team_battle_mode_2_criterion_None(self):
        try:
            team = PokeTeam("Ketchum")
            with captured_output("1 1 0"):
                team.choose_team(1, None)
        except Exception as e:
            self.verificationErrors.append(f"Ketchum's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")
            return

        # Test with MissingNo
        try:
            team = PokeTeam("Ketchum")
            with captured_output("1 0 1 2\n1 0 1 1"):
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Ketchum's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Squirtle's HP = 8 and level = 1, " \
                                "MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")

    # test with battle_mode = 2 with criterion: "hp"
    def test_choose_team_battle_mode_2_criterion_hp(self):
        try:
            team = PokeTeam("Ketchum")
            with captured_output("0 1 1"):
                team.choose_team(2, "hp")
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")
            return

        # Test with MissingNo
        try:
            team = PokeTeam("Ketchum")
            with captured_output("0 1 1 2\n0 1 1 1"):
                team.choose_team(2, "hp")
        except Exception as e:
            self.verificationErrors.append(f"Ketchum's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1, " \
                                "MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam with MissingNo does not handle limit correctly. {str(team)}")

    # test with battle_mode = 2 with criterion: "attack"
    def test_choose_team_battle_mode_2_criterion_attack(self):
        try:
            team = PokeTeam("Ketchum")
            with captured_output("1 2 1"):
                team.choose_team(2, "attack")
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, " \
                                "Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")
            return

        # Test with MissingNo
        try:
            team = PokeTeam("Ketchum")
            with captured_output("1 1 0 2\n1 1 0 1"):
                team.choose_team(2, "attack")
        except Exception as e:
            self.verificationErrors.append(f"Ketchum's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, " \
                                "MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam with MissingNo does not handle limit correctly. {str(team)}")

    # test with battle_mode = 2 with criterion: "defence"
    def test_choose_team_battle_mode_2_criterion_defence(self):
        try:
            team = PokeTeam("Ketchum")
            with captured_output("0 2 1"):
                team.choose_team(2, "defence")
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Squirtle's HP = 8 and level = 1, Bulbasaur's HP = 9 and level = 1, " \
                                "Bulbasaur's HP = 9 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")
            return

        # Test with MissingNo
        try:
            team = PokeTeam("Ketchum")
            with captured_output("0 2 1 2\n0 2 1 1"):
                team.choose_team(2, "defence")
        except Exception as e:
            self.verificationErrors.append(f"Ketchum's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Squirtle's HP = 8 and level = 1, Bulbasaur's HP = 9 and level = 1, " \
                                "Bulbasaur's HP = 9 and level = 1, MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam with MissingNo does not handle limit correctly. {str(team)}")

    # test with battle_mode = 2 with criterion: "speed"
    def test_choose_team_battle_mode_2_criterion_speed(self):
        try:
            team = PokeTeam("Ketchum")
            with captured_output("1 0 2"):
                team.choose_team(2, "speed")
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Squirtle's HP = 8 and level = 1, " \
                                "Squirtle's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")
            return

        # Test with MissingNo
        try:
            team = PokeTeam("Ketchum")
            with captured_output("1 0 2 1"):
                team.choose_team(2, "speed")
        except Exception as e:
            self.verificationErrors.append(f"Ketchum's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Squirtle's HP = 8 and level = 1, " \
                                "Squirtle's HP = 8 and level = 1, MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam with MissingNo does not handle limit correctly. {str(team)}")

    # test with battle_mode = 2 with criterion: "lvl"
    def test_choose_team_battle_mode_2_criterion_lvl(self):
        try:
            team = PokeTeam("Ketchum")
            with captured_output("2 1 1"):
                team.choose_team(2, "lvl")
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Charmander's HP = 7 and level = 1, " \
                                "Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")
            return

        # Test with MissingNo
        try:
            team = PokeTeam("Ketchum")
            with captured_output("2 1 1 1"):
                team.choose_team(2, "lvl")
        except Exception as e:
            self.verificationErrors.append(f"Ketchum's team could not be chosen: {str(e)}.")
            return

        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Charmander's HP = 7 and level = 1, " \
                                "Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1, " \
                                "MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam with MissingNo does not handle limit correctly. {str(team)}")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokeTeam)
    unittest.TextTestRunner(verbosity=0).run(suite)
