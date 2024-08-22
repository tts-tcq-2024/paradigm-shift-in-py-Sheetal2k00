import unittest
from unittest.mock import patch
from battery_monitor import classify_temperature_breach, ControllerReporter, EmailReporter, check_and_alert

class TestTypewiseAlert(unittest.TestCase):

    def test_classify_temperature_breach(self):
        # Testing different cooling types and temperatures
        self.assertEqual(classify_temperature_breach('PASSIVE_COOLING', 36), 'TOO_HIGH')
        self.assertEqual(classify_temperature_breach('PASSIVE_COOLING', -1), 'TOO_LOW')
        self.assertEqual(classify_temperature_breach('PASSIVE_COOLING', 30), 'NORMAL')
        
        self.assertEqual(classify_temperature_breach('HI_ACTIVE_COOLING', 46), 'TOO_HIGH')
        self.assertEqual(classify_temperature_breach('HI_ACTIVE_COOLING', 44), 'NORMAL')
        
        self.assertEqual(classify_temperature_breach('MED_ACTIVE_COOLING', 41), 'TOO_HIGH')
        self.assertEqual(classify_temperature_breach('MED_ACTIVE_COOLING', 40), 'NORMAL')

    @patch('builtins.print')
    def test_controller_reporter(self, mock_print):
        reporter = ControllerReporter()
        check_and_alert(reporter, {'coolingType': 'PASSIVE_COOLING'}, 36)
        mock_print.assert_called_with('0xfeed, TOO_HIGH')

    @patch('builtins.print')
    def test_email_reporter(self, mock_print):
        reporter = EmailReporter()
        check_and_alert(reporter, {'coolingType': 'PASSIVE_COOLING'}, -1)
        mock_print.assert_any_call('To: a.b@c.com')
        mock_print.assert_any_call('Hi, the temperature is too low')

if __name__ == "__main__":
    unittest.main()
