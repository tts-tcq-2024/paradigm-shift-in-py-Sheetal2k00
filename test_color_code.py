import unittest
from color_code import get_color_from_pair_number, get_pair_number_from_color
from battery_monitor import check_battery_status

class TestColorCode(unittest.TestCase):
    def test_number_to_pair(self):
        # Valid cases
        self.assertEqual(get_color_from_pair_number(1), ('White', 'Blue'))
        self.assertEqual(get_color_from_pair_number(10), ('Yellow', 'Green'))
        self.assertEqual(get_color_from_pair_number(25), ('Violet', 'Slate'))
        # Invalid cases
        with self.assertRaises(Exception):
            get_color_from_pair_number(0)
        with self.assertRaises(Exception):
            get_color_from_pair_number(26)
    
    def test_pair_to_number(self):
        # Valid cases
        self.assertEqual(get_pair_number_from_color('White', 'Blue'), 1)
        self.assertEqual(get_pair_number_from_color('Yellow', 'Green'), 10)
        self.assertEqual(get_pair_number_from_color('Violet', 'Slate'), 25)
        # Invalid cases
        with self.assertRaises(Exception):
            get_pair_number_from_color('Pink', 'Blue')
        with self.assertRaises(Exception):
            get_pair_number_from_color('White', 'Pink')

    def test_battery_status(self):
        # Normal conditions
        self.assertEqual(check_battery_status(temperature=25, soc=75, charge_rate=0.7), ["Battery status is normal"])
        
        # Boundary conditions
        self.assertEqual(check_battery_status(temperature=0, soc=20, charge_rate=0.0), [
            "Temperature out of range!", 
            "State of Charge out of range!", 
            "Charge Rate out of range!"
        ])
        self.assertEqual(check_battery_status(temperature=45, soc=80, charge_rate=0.8), [
            "Warning: Approaching temperature limit", 
            "Warning: Approaching charge peak/discharge", 
            "Warning: Approaching charge rate limit"
        ])
        
        # Warnings only
        self.assertEqual(check_battery_status(temperature=40, soc=21, charge_rate=0.79), [
            "Warning: Approaching charge peak/discharge", 
            "Warning: Approaching charge rate limit"
        ])
        self.assertEqual(check_battery_status(temperature=40, soc=22, charge_rate=0.79), [
            "Warning: Approaching charge peak/discharge", 
            "Warning: Approaching charge rate limit"
        ])
        self.assertEqual(check_battery_status(temperature=39, soc=22, charge_rate=0.79), [
            "Warning: Approaching charge peak/discharge"
        ])
        self.assertEqual(check_battery_status(temperature=40, soc=21, charge_rate=0.79), [
            "Warning: Approaching charge peak/discharge",
            "Warning: Approaching charge rate limit"
        ])
        
        # Breach conditions
        self.assertEqual(check_battery_status(temperature=46, soc=75, charge_rate=0.7), ["Temperature out of range!"])
        self.assertEqual(check_battery_status(temperature=4, soc=18, charge_rate=0.85), [
            "Temperature out of range!", 
            "State of Charge out of range!", 
            "Charge Rate out of range!"
        ])
        self.assertEqual(check_battery_status(temperature=50, soc=18, charge_rate=0.85), [
            "Temperature out of range!", 
            "State of Charge out of range!", 
            "Charge Rate out of range!"
        ])
        self.assertEqual(check_battery_status(temperature=50, soc=85, charge_rate=0.85), [
            "Temperature out of range!", 
            "State of Charge out of range!"
        ])
        self.assertEqual(check_battery_status(temperature=25, soc=15, charge_rate=0.85), [
            "State of Charge out of range!", 
            "Charge Rate out of range!"
        ])
        self.assertEqual(check_battery_status(temperature=25, soc=75, charge_rate=0.9), [
            "Charge Rate out of range!"
        ])

if __name__ == "__main__":
    unittest.main()
