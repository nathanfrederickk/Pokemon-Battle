"""
This file contains python code for testing the methods created in the file pokemon_base.py
"""
__author__ = "Chang Yee Vern, Frederick Nathanael Thunardi, Alyssa Ting Sue-Lyn, Shawn Wang Shao En"
__date__ = "28.04.2022"

import unittest

from tester_base import TesterBase
from pokemon_base import PokemonBase, GlitchMon
from pokemon import Charmander, Bulbasaur, Squirtle, MissingNo


class TestPokemonBase(TesterBase):
    # =============================================================================
    #                           Test get_hp()  
    # =============================================================================
    def test_charmander_get_hp(self):
        try:
            c_get_hp = Charmander().get_hp()
        except Exception as e:
            self.verificationErrors.append(f"get_hp() from Charmander could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(int(c_get_hp), 7, msg=f"Charmander's HP test did not return correct hp: {c_get_hp}")
        except AssertionError as e:
            self.verificationErrors.append(f"Charmander's HP test failed. {e}")

    def test_bulbasaur_get_hp(self):
        try:
            b_get_hp = Bulbasaur().get_hp()
        except Exception as e:
            self.verificationErrors.append(f"get_hp() from Bulbasaur could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(b_get_hp, 9, msg=f"Bulbasaur's HP test did not return correct hp: {b_get_hp}")
        except AssertionError as e:
            self.verificationErrors.append(f"Bulbasaur's HP test failed. {e}")

    def test_squirtle_get_hp(self):
        try:
            q_get_hp = Squirtle().get_hp()
        except Exception as e:
            self.verificationErrors.append(f"get_hp() from Squirtle could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(q_get_hp, 8, msg=f"Squirtle's HP test did not return correct hp: {q_get_hp}")
        except AssertionError as e:
            self.verificationErrors.append(f"Squirtle's HP test failed. {e}")

    def test_MissingNo_get_hp(self):
        try:
            q_get_hp = MissingNo().get_hp()
        except Exception as e:
            self.verificationErrors.append(f"get_hp() from MissingNo could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(q_get_hp, 8, msg=f"MissingNo's HP test did not return correct hp: {q_get_hp}")
        except AssertionError as e:
            self.verificationErrors.append(f"MissingNo's HP test failed. {e}")

    # =============================================================================
    #                           Test set_hp()  
    # =============================================================================
    def test_charmander_set_hp(self):
        try:
            c = Charmander()
            c.set_hp(5)     # Set HP for Charmander to 5
        except Exception as e:
            self.verificationErrors.append(f"set_hp() from Charmander could not be instantiated: {str(e)}.")
            return

        try:
            c_get_hp = c.get_hp()       # Use get_hp() to verify that the HP has been set correctly
            self.assertEqual(int(c_get_hp), 5, msg=f"Charmander's HP test did not return correct hp: {c_get_hp}")
        except AssertionError as e:
            self.verificationErrors.append(f"Charmander's HP test failed. {e}")

    def test_bulbasaur_set_hp(self):
        try:
            b = Bulbasaur()
            b.set_hp(6)     # Set HP for Bulbasaur to 6
        except Exception as e:
            self.verificationErrors.append(f"set_hp() from Bulbasaur could not be instantiated: {str(e)}.")
            return

        try:
            b_get_hp = b.get_hp()       # Use get_hp() to verify that the HP has been set correctly
            self.assertEqual(int(b_get_hp), 6, msg=f"Bulbasaur's HP test did not return correct hp: {b_get_hp}")
        except AssertionError as e:
            self.verificationErrors.append(f"Bulbasaur's HP test failed. {e}")

    def test_squirtle_set_hp(self):
        try:
            s = Squirtle()
            s.set_hp(3)     # Set HP for Squirtle to 3
        except Exception as e:
            self.verificationErrors.append(f"set_hp() from Squirtle could not be instantiated: {str(e)}.")
            return

        try:
            s_get_hp = s.get_hp()       # Use get_hp() to verify that the HP has been set correctly
            self.assertEqual(int(s_get_hp), 3, msg=f"Squirtle's HP test did not return correct hp: {s_get_hp}")
        except AssertionError as e:
            self.verificationErrors.append(f"Squirtle's HP test failed. {e}")

    def test_MissingNo_set_hp(self):
        try:
            s = MissingNo()
            s.set_hp(1)     # Set HP for MissingNo to 1
        except Exception as e:
            self.verificationErrors.append(f"set_hp() from MissingNo could not be instantiated: {str(e)}.")
            return

        try:
            s_get_hp = s.get_hp()       # Use get_hp() to verify that the HP has been set correctly
            self.assertEqual(int(s_get_hp), 1, msg=f"MissingNo's HP test did not return correct hp: {s_get_hp}")
        except AssertionError as e:
            self.verificationErrors.append(f"MissingNo's HP test failed. {e}")

    # =============================================================================
    #                           Test get_level()  
    # =============================================================================
    def test_charmander_get_level(self):
        try:
            c_get_level = Charmander().get_level()
        except Exception as e:
            self.verificationErrors.append(f"get_level() from Charmander could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(c_get_level, 1, msg=f"Charmander level test did not return correct level: {c_get_level}")
        except AssertionError as e:
            self.verificationErrors.append(f"Charmander's level test failed. {e}")

    def test_bulbasaur_get_level(self):
        from pokemon import Bulbasaur
        try:
            b_get_level = Bulbasaur().get_level()
        except Exception as e:
            self.verificationErrors.append(f"get_level() from Bulbasaur could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(b_get_level, 1, msg=f"Bulbasaur level test did not return correct level: {b_get_level}")
        except AssertionError as e:
            self.verificationErrors.append(f"Bulbasaur's level test failed. {e}")

    def test_squirtle_get_level(self):
        try:
            q_get_level = Squirtle().get_level()
        except Exception as e:
            self.verificationErrors.append(f"get_level() from Squirtle could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(q_get_level, 1, msg=f"Squirtle level test did not return correct level: {q_get_level}")
        except AssertionError as e:
            self.verificationErrors.append(f"Squirtle's level test failed. {e}")

    def test_MissingNo_get_level(self):
        try:
            q_get_level = MissingNo().get_level()
        except Exception as e:
            self.verificationErrors.append(f"get_level() from MissingNo could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(q_get_level, 1, msg=f"MissingNo level test did not return correct level: {q_get_level}")
        except AssertionError as e:
            self.verificationErrors.append(f"MissingNo's level test failed. {e}")

    # =============================================================================
    #                         Test get_poke_type()  
    # =============================================================================
    def test_charmander_get_poke_type(self):
        try:
            c_get_poke_type = Charmander().get_poke_type()
        except Exception as e:
            self.verificationErrors.append(f"get_poke_type() from Charmander could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(c_get_poke_type, "Fire", msg=f"Charmander poke_type test did not return correct poke_type: {c_get_poke_type}")
        except AssertionError as e:
            self.verificationErrors.append(f"Charmander's poke_type test failed. {e}")

    def test_bulbasaur_get_poke_type(self):
        try:
            b_get_poke_type = Bulbasaur().get_poke_type()
        except Exception as e:
            self.verificationErrors.append(f"get_poke_type() from Bulbasaur could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(b_get_poke_type, "Grass", msg=f"Bulbasaur poke_type test did not return correct poke_type: {b_get_poke_type}")
        except AssertionError as e:
            self.verificationErrors.append(f"Bulbasaur's poke_type test failed. {e}")

    def test_squirtle_get_poke_type(self):
        try:
            q_get_poke_type = Squirtle().get_poke_type()
        except Exception as e:
            self.verificationErrors.append(f"get_poke_type() from Squirtle could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(q_get_poke_type, "Water", msg=f"Squirtle poke_type test did not return correct poke_type: {q_get_poke_type}")
        except AssertionError as e:
            self.verificationErrors.append(f"Squirtle's poke_type test failed. {e}")

    def test_MissingNo_get_poke_type(self):
        try:
            q_get_poke_type = MissingNo().get_poke_type()
        except Exception as e:
            self.verificationErrors.append(f"get_poke_type() from MissingNo could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(q_get_poke_type, "None", msg=f"MissingNo poke_type test did not return correct poke_type: {q_get_poke_type}")
        except AssertionError as e:
            self.verificationErrors.append(f"MissingNo's poke_type test failed. {e}")

    # =============================================================================
    #                           Test is_fainted()  
    # =============================================================================
    def test_charmander_is_fainted(self):
        try:
            c_is_fainted = Charmander().is_fainted()
        except Exception as e:
            self.verificationErrors.append(f"is_fainted() from Charmander could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(c_is_fainted, False, msg=f"Charmander is_fainted test did not return correct boolean: {c_is_fainted}")
        except AssertionError as e:
            self.verificationErrors.append(f"Charmander's is_fainted test failed. {e}")

    def test_bulbasaur_is_fainted(self):
        try:
            b_is_fainted = Bulbasaur().is_fainted()
        except Exception as e:
            self.verificationErrors.append(f"is_fainted() from Bulbasaur could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(b_is_fainted, False, msg=f"Bulbasaur is_fainted test did not return correct boolean: {b_is_fainted}")
        except AssertionError as e:
            self.verificationErrors.append(f"Bulbasaur's is_fainted test failed. {e}")

    def test_squirtle_is_fainted(self):
        try:
            q_is_fainted = Squirtle().is_fainted()
        except Exception as e:
            self.verificationErrors.append(f"is_fainted() from Squirtle could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(q_is_fainted, False, msg=f"Squirtle is_fainted test did not return correct boolean: {q_is_fainted}")
        except AssertionError as e:
            self.verificationErrors.append(f"Squirtle's is_fainted test failed. {e}")

    def test_MissingNo_is_fainted(self):
        try:
            q_is_fainted = MissingNo().is_fainted()
        except Exception as e:
            self.verificationErrors.append(f"is_fainted() from MissingNo could not be instantiated: {str(e)}.")
            return

        try:
            self.assertEqual(q_is_fainted, False, msg=f"MissingNo is_fainted test did not return correct boolean: {q_is_fainted}")
        except AssertionError as e:
            self.verificationErrors.append(f"MissingNo's is_fainted test failed. {e}")

    # =============================================================================
    #                           Test level_up()  
    # =============================================================================
    def test_charmander_level_up(self):
        try:
            c = Charmander()
            c.level_up()
        except Exception as e:
            self.verificationErrors.append(f"level_up() from Charmander could not be instantiated: {str(e)}.")
            return

        try:
            c_get_level = c.get_level()
            self.assertEqual(c_get_level, 2, msg=f"Charmander's level test did not return correct level: {c_get_level}")
        except AssertionError as e:
            self.verificationErrors.append(f"Charmander's level test failed. {e}")

    def test_bulbasaur_level_up(self):
        try:
            b = Bulbasaur()
            b.level_up()
        except Exception as e:
            self.verificationErrors.append(f"level_up() from Bulbasaur could not be instantiated: {str(e)}.")
            return

        try:
            b_get_level = b.get_level()
            self.assertEqual(b_get_level, 2, msg=f"Bulbasaur's level test did not return correct level: {b_get_level}")
        except AssertionError as e:
            self.verificationErrors.append(f"Bulbasaur's level test failed. {e}")

    def test_squirtle_level_up(self):
        try:
            s = Squirtle()
            s.level_up()
        except Exception as e:
            self.verificationErrors.append(f"level_up() from Squirtle could not be instantiated: {str(e)}.")
            return

        try:
            s_get_level = s.get_level()
            self.assertEqual(s_get_level, 2, msg=f"Squirtle's level test did not return correct level: {s_get_level}")
        except AssertionError as e:
            self.verificationErrors.append(f"Squirtle's level test failed. {e}")
    
    def test_MissingNo_level_up(self):
        try:
            s = MissingNo()
            s.level_up()
        except Exception as e:
            self.verificationErrors.append(f"level_up() from MissingNo could not be instantiated: {str(e)}.")
            return

        try:
            s_get_level = s.get_level()
            self.assertEqual(s_get_level, 2, msg=f"MissingNo's level test did not return correct level: {s_get_level}")
        except AssertionError as e:
            self.verificationErrors.append(f"MissingNo's level test failed. {e}")

    # =============================================================================
    #                           Test abstract classes
    # =============================================================================
    # Test get_name()
    def test_get_name(self):
        try:
            get_name = PokemonBase.get_name
        except Exception as e:
            self.verificationErrors.append(f"get_name could not be instantiated: {str(e)}.")

    # Test get_attack()
    def test_get_attack(self):
        try:
            get_attack = PokemonBase.get_attack
        except Exception as e:
            self.verificationErrors.append(f"get_attack could not be instantiated: {str(e)}.")

    # Test get_defence()
    def test_get_defence(self):
        try:
            get_defence = PokemonBase.get_defence
        except Exception as e:
            self.verificationErrors.append(f"get_defence could not be instantiated: {str(e)}.")

    # Test get_speed()
    def test_get_speed(self):
        try:
            get_speed = PokemonBase.get_speed
        except Exception as e:
            self.verificationErrors.append(f"get_speed could not be instantiated: {str(e)}.")

    # Test get_damage_after_attack()
    def test_get_damage_after_attack(self):
        try:
            get_damage_after_attack = PokemonBase.get_damage_after_attack
        except Exception as e:
            self.verificationErrors.append(f"get_damage_after_attack could not be instantiated: {str(e)}.")

    # =============================================================================
    #                           Test GlitchMon
    # =============================================================================
    # Test increase_HP()
    def test_increase_HP(self):
        try:
            m = MissingNo()
            m.increase_HP(1)    # Increase the HP by 1
        except Exception as e:
            self.verificationErrors.append(f"increase_HP() from MissingNo could not be instantiated: {str(e)}.")
            return

        try:
            m_get_level = m.get_hp()    # Returned HP should be 8 + 1 = 9
            self.assertEqual(m_get_level, 9, msg=f"MissingNo's HP test did not return correct HP: {m_get_level}")
        except AssertionError as e:
            self.verificationErrors.append(f"MissingNo's HP test failed. {e}")

    # Test superpower()
    def test_superpower(self):
        try:
            superpower = GlitchMon.superpower
        except Exception as e:
            self.verificationErrors.append(f"superpower could not be instantiated: {str(e)}.")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemonBase)
    unittest.TextTestRunner(verbosity=0).run(suite)
