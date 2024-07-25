from color_code import get_color_from_pair_number, get_pair_number_from_color
from reference_manual import ReferenceManual
from battery_monitor import check_battery_status

def main():
    pair_number = 4
    major_color, minor_color = get_color_from_pair_number(pair_number)
    print(f"Pair Number {pair_number} is: Major Color - {major_color}, Minor Color - {minor_color}")

    major_color = "Black"
    minor_color = "Orange"
    pair_number = get_pair_number_from_color(major_color, minor_color)
    print(f"Major Color {major_color} and Minor Color {minor_color} correspond to Pair Number {pair_number}")

    # Print reference manual
    manual = ReferenceManual()
    manual.print_manual()

    # Check battery status
    check_battery_status(temperature=25, soc=75, charge_rate=0.7)

if __name__ == "__main__":
    main()
