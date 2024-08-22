class CoolingTypeLimits:
    LIMITS = {
        'PASSIVE_COOLING': (0, 35),
        'HI_ACTIVE_COOLING': (0, 45),
        'MED_ACTIVE_COOLING': (0, 40)
    }

    @staticmethod
    def get_limits(cooling_type):
        if cooling_type in CoolingTypeLimits.LIMITS:
            return CoolingTypeLimits.LIMITS[cooling_type]
        raise ValueError(f"Unknown cooling type: {cooling_type}")

def infer_breach(value, lower_limit, upper_limit):
    if value < lower_limit:
        return 'TOO_LOW'
    if value > upper_limit:
        return 'TOO_HIGH'
    return 'NORMAL'

def classify_temperature_breach(cooling_type, temperature_in_c):
    lower_limit, upper_limit = CoolingTypeLimits.get_limits(cooling_type)
    return infer_breach(temperature_in_c, lower_limit, upper_limit)

class Reporter:
    def report(self, breach_type):
        raise NotImplementedError("Subclasses should implement this!")

class ControllerReporter(Reporter):
    def report(self, breach_type):
        header = 0xfeed
        print(f'0x{header:x}, {breach_type}')

class EmailReporter(Reporter):
    def report(self, breach_type):
        recipient = "a.b@c.com"
        messages = {
            'TOO_LOW': 'Hi, the temperature is too low',
            'TOO_HIGH': 'Hi, the temperature is too high'
        }
        print(f'To: {recipient}')
        print(messages[breach_type])

def check_and_alert(reporter: Reporter, battery_char, temperature_in_c):
    breach_type = classify_temperature_breach(battery_char['coolingType'], temperature_in_c)
    reporter.report(breach_type)
