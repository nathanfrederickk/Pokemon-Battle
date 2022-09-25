"""
This file contains python code for testing the methods created in the file pokemon.py
"""
__author__ = "Chang Yee Vern, Frederick Nathanael Thunardi, Alyssa Ting Sue-Lyn, Shawn Wang Shao En"
__date__ = "28.04.2022"

import unittest

from tester_base import TesterBase
from pokemon_base import *
from pokemon import Charmander, Bulbasaur, Squirtle, MissingNo


class TestPokemon(TesterBase):
    # =============================================================================
    #                           Test if pokemon class inherited from PokemonBase
    # =============================================================================
    # Test if Charmander inherited from Pokemon Base
    def test_charmander_inherit(self):
        b = Charmander()
        try:
            self.assertTrue(isinstance(b, PokemonBase), msg='Charmander did not inherit PokemonBase')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    # Test if Bulbasaur inherited from Pokemon Base
    def test_bulbasaur_inherit(self):
        b = Bulbasaur()
        try:
            self.assertTrue(isinstance(b, PokemonBase), msg='Bulbasaur did not inherit PokemonBase')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    # Test if Squirtle inherited from Pokemon Base
    def test_squirtle_inherit(self):
        b = Squirtle()
        try:
            self.assertTrue(isinstance(b, PokemonBase), msg='Squirtle did not inherit PokemonBase')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    # =============================================================================
    #                           Test get_name()
    # =============================================================================
    def test_charmander_name(self):
        try:
            c_name = Charmander().get_name()
        except Exception as e:
            self.verificationErrors.append(f"get_name() from Charmander could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(c_name, "Charmander",
                             msg=f"Charmander get_name test did not return correct name: {c_name}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_name() method failed. {e}")

    def test_bulbasaur_name(self):
        try:
            b_name = Bulbasaur().get_name()
        except Exception as e:
            self.verificationErrors.append(f"get_name() from Bulbasaur could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(b_name, "Bulbasaur", msg=f"Bulbasaur get_name test did not return correct name: {b_name}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_name() method failed. {e}")

    def test_squirtle_name(self):
        try:
            q_name = Squirtle().get_name()
        except Exception as e:
            self.verificationErrors.append(f"get_name() from Squirtle could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(q_name, "Squirtle", msg=f"Squirtle get_name test did not return correct name: {q_name}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_name() method failed. {e}")

    def test_MissingNo_name(self):
        try:
            q_name = MissingNo().get_name()
        except Exception as e:
            self.verificationErrors.append(f"get_name() from MissingNo could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(q_name, "MissingNo", msg=f"MissingNo get_name test did not return correct name: {q_name}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_name() method failed. {e}")

    # =============================================================================
    #                           Test get_attack()
    # =============================================================================
    def test_charmander_attack_damage(self):
        try:
            c_attack_damage = Charmander().get_attack()
        except Exception as e:
            self.verificationErrors.append(f"get_attack() from Charmander could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(c_attack_damage, 7,
                             msg=f"Charmander get_attack test did not return correct damage: {c_attack_damage}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_attack() method failed. {e}")

    def test_bulbasaur_attack_damage(self):
        try:
            b_attack_damage = Bulbasaur().get_attack()
        except Exception as e:
            self.verificationErrors.append(f"get_attack() from Bulbasaur could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(b_attack_damage, 5,
                             msg=f"Bulbasaur get_attack test did not return correct damage: {b_attack_damage}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_attack() method failed. {e}")

    def test_squirtle_attack_damage(self):
        try:
            q_attack_damage = Squirtle().get_attack()
        except Exception as e:
            self.verificationErrors.append(f"get_attack() from Squirtle could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(q_attack_damage, 4,
                             msg=f"Squirtle get_attack test did not return correct damage: {q_attack_damage}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_attack() method failed. {e}")

    def test_MissingNo_attack_damage(self):
        try:
            q_attack_damage = MissingNo().get_attack()
        except Exception as e:
            self.verificationErrors.append(f"get_attack() from MissingNo could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(q_attack_damage, 5,
                             msg=f"MissingNo get_attack test did not return correct damage: {q_attack_damage}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_attack() method failed. {e}")

    # =============================================================================
    #                           Test get_attack() with type effectiveness
    # =============================================================================
    def test_charmander_attack_damage_with_type_effectiveness(self):
        try:
            opponent = Charmander().TYPE_EFFECTIVENESS["Fire"]
            c_attack_damage = Charmander().get_attack() * opponent
        except Exception as e:
            self.verificationErrors.append(f"get_attack() from Charmander could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(c_attack_damage, 7,
                             msg=f"Charmander get_attack() test against Charmander did not return correct damage: "
                                 f"{c_attack_damage}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_attack() method from Charmander failed. {e}")
            return

        # test attack damage against Bulbasaur
        try:
            opponent = Charmander().TYPE_EFFECTIVENESS["Grass"]
            c_attack_damage = Charmander().get_attack() * opponent
            self.assertEqual(c_attack_damage, 14,
                             msg=f"Charmander get_attack() test against Bulbasaur did not return correct damage: "
                                 f"{c_attack_damage}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_attack() method from Charmander failed. {e}")
            return

        # test attack damage against Squirtle
        try:
            opponent = Charmander().TYPE_EFFECTIVENESS["Water"]
            c_attack_damage = Charmander().get_attack() * opponent
            self.assertEqual(c_attack_damage, 3.5,
                             msg=f"Charmander get_attack() test against Squirtle did not return correct damage: "
                                 f"{c_attack_damage}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_attack() method from Charmander failed. {e}")
            return

        # test attack damage against MissingNo
        try:
            opponent = Charmander().TYPE_EFFECTIVENESS["None"]
            c_attack_damage = Charmander().get_attack() * opponent
            self.assertEqual(c_attack_damage, 7,
                             msg=f"Charmander get_attack() test against MissingNo did not return correct damage: "
                                 f"{c_attack_damage}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_attack() method from Charmander failed. {e}")
            return

    def test_bulbasaur_attack_damage_with_type_effectiveness(self):
        try:
            opponent = Bulbasaur().TYPE_EFFECTIVENESS["Grass"]
            b_attack_damage = Bulbasaur().get_attack() * opponent
        except Exception as e:
            self.verificationErrors.append(f"get_attack() from Bulbasaur could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(b_attack_damage, 5,
                             msg=f"Bulbasaur get_attack() test against Bulbasaur did not return correct damage: "
                                 f"{b_attack_damage}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_attack() method from Bulbasaur failed. {e}")
            return

        # test attack damage against Charmander
        try:
            opponent = Bulbasaur().TYPE_EFFECTIVENESS["Fire"]
            b_attack_damage = Bulbasaur().get_attack() * opponent
            self.assertEqual(b_attack_damage, 2.5,
                             msg=f"Bulbasaur get_attack() test against Charmander did not return correct damage: "
                                 f"{b_attack_damage}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_attack() method from Bulbasaur failed. {e}")
            return

        # test attack damage against Squirtle
        try:
            opponent = Bulbasaur().TYPE_EFFECTIVENESS["Water"]
            b_attack_damage = Bulbasaur().get_attack() * opponent
            self.assertEqual(b_attack_damage, 10,
                             msg=f"Bulbasaur get_attack() test against Squirtle did not return correct damage: "
                                 f"{b_attack_damage}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_attack() method from Bulbasaur failed. {e}")
            return

        # test attack damage against MissingNo
        try:
            opponent = Bulbasaur().TYPE_EFFECTIVENESS["None"]
            b_attack_damage = Bulbasaur().get_attack() * opponent
            self.assertEqual(b_attack_damage, 5,
                             msg=f"Bulbasaur get_attack() test against MissingNo did not return correct damage: "
                                 f"{b_attack_damage}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_attack() method from Bulbasaur failed. {e}")

    def test_squirtle_attack_damage_with_type_effectiveness(self):
        try:
            opponent = Squirtle().TYPE_EFFECTIVENESS["Water"]
            q_attack_damage = Squirtle().get_attack() * opponent
        except Exception as e:
            self.verificationErrors.append(f"get_attack() from Squirtle could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(q_attack_damage, 4,
                             msg=f"Squirtle get_attack() test against Squirtle did not return correct damage: "
                                 f"{q_attack_damage}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_attack() method from Squirtle failed. {e}")
            return

        # test attack damage against Charmander
        try:
            opponent = Squirtle().TYPE_EFFECTIVENESS["Fire"]
            q_attack_damage = Squirtle().get_attack() * opponent
            self.assertEqual(q_attack_damage, 8,
                             msg=f"Squirtle get_attack() test against Charmander did not return correct damage: "
                                 f"{q_attack_damage}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_attack() method from Squirtle failed. {e}")
            return

        # test attack damage against Bulbasaur
        try:
            opponent = Squirtle().TYPE_EFFECTIVENESS["Grass"]
            q_attack_damage = Squirtle().get_attack() * opponent
            self.assertEqual(q_attack_damage, 2,
                             msg=f"Squirtle get_attack() test against Bulbasaur did not return correct damage: "
                                 f"{q_attack_damage}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_attack() method from Squirtle failed. {e}")

    def test_MissingNo_attack_damage_with_type_effectiveness(self):
        try:
            opponent = MissingNo().TYPE_EFFECTIVENESS["None"]
            q_attack_damage = MissingNo().get_attack() * opponent
        except Exception as e:
            self.verificationErrors.append(f"get_attack() from MissingNo could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(q_attack_damage, 5,
                             msg=f"MissingNo get_attack() test against MissingNo did not return correct damage: "
                                 f"{q_attack_damage}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_attack() method from MissingNo failed. {e}")
            return

        # test attack damage against Charmander
        try:
            opponent = MissingNo().TYPE_EFFECTIVENESS["Fire"]
            q_attack_damage = MissingNo().get_attack() * opponent
            self.assertEqual(q_attack_damage, 5,
                             msg=f"MissingNo get_attack() test against Charmander did not return correct damage: "
                                 f"{q_attack_damage}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_attack() method from MissingNo failed. {e}")
            return

        # test attack damage against Bulbasaur
        try:
            opponent = MissingNo().TYPE_EFFECTIVENESS["Grass"]
            q_attack_damage = MissingNo().get_attack() * opponent
            self.assertEqual(q_attack_damage, 5,
                             msg=f"MissingNo get_attack() test against Bulbasaur did not return correct damage: "
                                 f"{q_attack_damage}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_attack() method from MissingNo failed. {e}")
            return

        # test attack damage against Squirtle
        try:
            opponent = MissingNo().TYPE_EFFECTIVENESS["Water"]
            q_attack_damage = MissingNo().get_attack() * opponent
            self.assertEqual(q_attack_damage, 5,
                             msg=f"MissingNo get_attack test against Squirtle did not return correct damage: "
                                 f"{q_attack_damage}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_attack() method from MissingNo failed. {e}")

    # =============================================================================
    #                           Test get_defence()
    # =============================================================================
    def test_charmander_defence(self):
        try:
            c_defence = Charmander().get_defence()
        except Exception as e:
            self.verificationErrors.append(f"get_defence() from Charmander could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(c_defence, 4,
                             msg=f"Charmander get_defence test did not return correct defense: {c_defence}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_defence() method failed. {e}")

    def test_bulbasaur_defence(self):
        try:
            b_defence = Bulbasaur().get_defence()
        except Exception as e:
            self.verificationErrors.append(f"get_defence() from Bulbasaur could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(b_defence, 5,
                             msg=f"Bulbasaur get_defence test did not return correct defense: {b_defence}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_defence() method failed. {e}")

    def test_squirtle_defence(self):
        try:
            q_defence = Squirtle().get_defence()
        except Exception as e:
            self.verificationErrors.append(f"get_defence() from Squirtle could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(q_defence, 7, msg=f"Squirtle get_defence test did not return correct defense: {q_defence}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_defence() method failed. {e}")

    def test_MissingNo_defence(self):
        try:
            q_defence = MissingNo().get_defence()
        except Exception as e:
            self.verificationErrors.append(f"get_defence() from MissingNo could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(q_defence, 5, msg=f"MissingNo get_defence test did not return correct defense: "
                                               f"{q_defence}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_defence() method failed. {e}")

    # =============================================================================
    #                           Test get_speed()
    # =============================================================================
    def test_charmander_speed(self):
        try:
            c_speed = Charmander().get_speed()
        except Exception as e:
            self.verificationErrors.append(f"get_speed() from Charmander could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(c_speed, 8, msg=f"Charmander get_speed test did not return correct speed: {c_speed}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_speed() method failed. {e}")

    def test_bulbasaur_speed(self):
        try:
            b_speed = Bulbasaur().get_speed()
        except Exception as e:
            self.verificationErrors.append(f"get_speed() from Bulbasaur could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(b_speed, 7, msg=f"Bulbasaur get_speed test did not return correct speed: {b_speed}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_speed() method failed. {e}")

    def test_squirtle_speed(self):
        try:
            q_speed = Squirtle().get_speed()
        except Exception as e:
            self.verificationErrors.append(f"get_speed() from Squirtle could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(q_speed, 7, msg=f"Squirtle get_speed test did not return correct speed: {q_speed}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_speed() method failed. {e}")

    def test_MissingNo_speed(self):
        try:
            q_speed = MissingNo().get_speed()
        except Exception as e:
            self.verificationErrors.append(f"get_speed() from MissingNo could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(q_speed, 7, msg=f"MissingNo get_speed test did not return correct speed: {q_speed}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_speed() method failed. {e}")

    # =============================================================================
    #                           Test get_damage_after_attack()
    # =============================================================================
    def test_charmander_damage_after_attack(self):
        try:
            damage = 3
            c_damage_after_attack = Charmander().get_damage_after_attack(damage)
        except Exception as e:
            self.verificationErrors.append(f"get_damage_after_attack() from Charmander could not be instantiated: "
                                           f"{str(e)}.")
            return

        try:        # damage is less than defense -> hp = hp - damage (defense: 4, damage: 3)
            self.assertEqual(c_damage_after_attack, 6,
                             msg=f"Charmander get_damage_after_attack test did not return correct hp: "
                                 f"{c_damage_after_attack}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_damage_after_attack() method failed. {e}")
            return

        try:        # damage is more than defense -> hp = hp - damage // 2 (defense: 4, damage: 5)
            damage = 5
            c_damage_after_attack = Charmander().get_damage_after_attack(damage)
            self.assertEqual(c_damage_after_attack, 2,
                             msg=f"Charmander get_damage_after_attack test did not return correct hp: "
                                 f"{c_damage_after_attack}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_damage_after_attack() method failed. {e}")

    def test_bulbasaur_damage_after_attack(self):
        try:
            damage = 4
            b_damage_after_attack = Bulbasaur().get_damage_after_attack(damage)
        except Exception as e:
            self.verificationErrors.append(f"get_damage_after_attack() from Bulbasaur could not be instantiated: "
                                           f"{str(e)}.")
            return

        try:        # damage is less than defense -> hp = hp - damage (defense: 5, damage: 4)
            self.assertEqual(b_damage_after_attack, 7,
                             msg=f"Bulbasaur get_damage_after_attack test did not return correct hp: "
                                 f"{b_damage_after_attack}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_damage_after_attack() method failed. {e}")
            return

        try:        # damage is more than defense -> hp = hp - damage (defense: 5, damage: 7)
            damage = 11
            b_damage_after_attack = Bulbasaur().get_damage_after_attack(damage)
            self.assertEqual(b_damage_after_attack, -2,
                             msg=f"Bulbasaur get_damage_after_attack test did not return correct hp: "
                                 f"{b_damage_after_attack}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_damage_after_attack() method failed. {e}")

    def test_squirtle_damage_after_attack(self):
        try:
            damage = 4
            q_damage_after_attack = Squirtle().get_damage_after_attack(damage)
        except Exception as e:
            self.verificationErrors.append(f"get_damage_after_attack() from Squirtle could not be instantiated: "
                                           f"{str(e)}.")
            return

        try:        # damage is less than defense -> hp = hp - damage (defense: 6 + level (1), damage: 4)
            self.assertEqual(q_damage_after_attack, 6,
                             msg=f"Squirtle get_damage_after_attack test did not return correct hp: "
                                 f"{q_damage_after_attack}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_damage_after_attack() method failed. {e}")
            return

        try:        # damage is more than defense -> hp = hp - damage (defense: 6 + level (1), damage: 15)
            damage = 15
            q_damage_after_attack = Squirtle().get_damage_after_attack(damage)
            self.assertEqual(q_damage_after_attack, -7,
                             msg=f"Squirtle get_damage_after_attack test did not return correct hp: "
                                 f"{q_damage_after_attack}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_damage_after_attack() method failed. {e}")

    def test_MissingNo_damage_after_attack(self):
        try:
            damage = 4
            q_damage_after_attack = MissingNo().get_damage_after_attack(damage)
        except Exception as e:
            self.verificationErrors.append(f"get_damage_after_attack() from MissingNo could not be instantiated: "
                                           f"{str(e)}.")
            return

        try:        # damage is less than defense
            """
            Expect result of either 6, 9 or 8
            6: health after receiving damage 4
            9: superpower <- hp + 1
            8: superpower <- level + 1, hp no change
            """
            if q_damage_after_attack != 6 and q_damage_after_attack != 9 and q_damage_after_attack != 8:
                raise ValueError(f"MissingNo get_damage_after_attack test did not return correct hp: "
                                 f"{q_damage_after_attack}")
        except ValueError as e:
            self.verificationErrors.append(f"get_damage_after_attack() method failed. {e}")
            return

        try:        # damage is more than defense
            """
            Expect result of either -7, 9 or 8
            -7: health after receiving damage 15
            9: superpower <- hp + 1
            8: superpower <- level + 1, hp no change
            """
            damage = 15
            q_damage_after_attack = MissingNo().get_damage_after_attack(damage)
            if q_damage_after_attack != -7 and q_damage_after_attack != 8 and q_damage_after_attack != 9:
                raise ValueError(f"MissingNo get_damage_after_attack test did not return correct hp: "
                                 f"{q_damage_after_attack}")
        except ValueError as e:
            self.verificationErrors.append(f"get_damage_after_attack() method failed. {e}")

    # =============================================================================
    #                           Test level_up() for MissingNo
    # =============================================================================
    def test_level_up_MissingNo(self):
        try:
            m = MissingNo()
            m.level_up()
        except Exception as e:
            self.verificationErrors.append(f"level_up() from MissingNo could not be instantiated: {str(e)}.")
            return

        try:
            m_hp = m.get_hp()
            self.assertEqual(m_hp, 9, msg=f"MissingNo get_hp test did not return correct hp: {m_hp}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_hp() method failed. {e}")
            return

        try:
            m_lvl = m.get_level()
            self.assertEqual(m_lvl, 2, msg=f"MissingNo get_level test did not return correct level: {m_lvl}")
        except AssertionError as e:
            self.verificationErrors.append(f"get_level() method failed. {e}")

    # =============================================================================
    #                           Test MissingNo inherit
    # =============================================================================
    # Test if MissingNo inherited from Pokemon Base
    def test_MissingNo_inherit(self):
        b = MissingNo()
        try:
            self.assertTrue(isinstance(b, GlitchMon), msg='MissingNo did not inherit GlitchMon')
        except AssertionError as e:
            self.verificationErrors.append(str(e))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemon)
    unittest.TextTestRunner(verbosity=0).run(suite)
