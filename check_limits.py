class BatteryStatusChecker:
    LIMITS = {'temperature': (0, 45), 'soc': (20, 80), 'charge_rate': (0, 0.8)}
    
    def __init__(self, temperature, soc, charge_rate):
        self.params = {'temperature': temperature, 'soc': soc, 'charge_rate': charge_rate}
    
    def check(self):
        issues = []
        for param, (min_val, max_val) in self.LIMITS.items():
            if not (min_val <= self.params[param] <= max_val):
                issues.append(f"{param.replace('_', ' ').title()} out of range!")
        return issues

def battery_is_ok(temperature, soc, charge_rate):
    checker = BatteryStatusChecker(temperature, soc, charge_rate)
    issues = checker.check()
    if issues:
        for issue in issues:
            print(issue)
        return False
    return True

if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
