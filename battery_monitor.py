def check_battery_status(temperature, soc, charge_rate):
    def in_warning_range(value, lower, upper):
        tolerance = (upper - lower) * 0.05
        return lower <= value <= lower + tolerance or upper - tolerance <= value <= upper

    def in_breach_range(value, lower, upper):
        return value < lower or value > upper

    temperature_range = (0, 45)
    soc_range = (20, 80)
    charge_rate_range = (0.0, 0.8)

    status = []
    
    if in_breach_range(temperature, *temperature_range):
        status.append("Temperature out of range!")
    elif in_warning_range(temperature, *temperature_range):
        status.append("Warning: Approaching temperature limit")

    if in_breach_range(soc, *soc_range):
        status.append("State of Charge out of range!")
    elif in_warning_range(soc, *soc_range):
        status.append("Warning: Approaching charge peak/discharge")

    if in_breach_range(charge_rate, *charge_rate_range):
        status.append("Charge Rate out of range!")
    elif in_warning_range(charge_rate, *charge_rate_range):
        status.append("Warning: Approaching charge rate limit")

    return status if status else ["Battery status is normal"]
