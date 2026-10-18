"""Simulated Device Monitoring and Alert System for CPP102 Week 17."""


def get_initial_readings():
    """Return the starting temperature readings in degrees Celsius."""
    return [28, 31, 35, 37, 29]


def is_whole_number(text):
    """Check for digits with an optional leading minus sign."""
    if len(text) == 0:
        return False

    start = 0
    if text[0] == "-":
        start = 1

    if start == len(text):
        return False

    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False

    return True


def add_reading(readings, lowest, highest):
    """Add one valid reading or show an error and return to the menu."""
    text = input("Enter new reading: ").strip()

    if len(text) == 0:
        print("Invalid input. The reading cannot be empty.")
    elif not is_whole_number(text):
        print("Invalid input. Enter a whole number only.")
    else:
        # Check the range before changing the list.
        value = int(text)

        if value < lowest or value > highest:
            print(f"Invalid reading. Enter a value from {lowest} to {highest}.")
        else:
            readings.append(value)
            print("Reading added successfully.")


def classify_reading(reading, warning_limit, critical_limit):
    """Return the category for one temperature reading."""
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"


def compute_total(readings):
    """Return the total using a loop."""
    total = 0

    for reading in readings:
        total = total + reading

    return total


def compute_average(readings):
    """Return the average of the nonempty reading list."""
    return compute_total(readings) / len(readings)


def find_minimum(readings):
    """Return the lowest reading using a loop."""
    minimum = readings[0]

    for reading in readings:
        if reading < minimum:
            minimum = reading

    return minimum


def find_maximum(readings):
    """Return the highest reading using a loop."""
    maximum = readings[0]

    for reading in readings:
        if reading > maximum:
            maximum = reading

    return maximum


def count_category(readings, warning_limit, critical_limit, category):
    """Return how many readings belong to the requested category."""
    count = 0

    for reading in readings:
        if classify_reading(reading, warning_limit, critical_limit) == category:
            count = count + 1

    return count


def determine_overall_status(warning_count, critical_count):
    """Return the monitoring status with critical readings taking priority."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_menu():
    """Print the five available menu options."""
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def display_readings(readings):
    """Print each stored reading with its position number."""
    print("\nCURRENT READINGS")
    print("----------------")

    for index in range(len(readings)):
        print(f"Reading {index + 1}: {readings[index]} °C")


def display_classifications(readings, warning_limit, critical_limit):
    """Print each reading and its temperature category."""
    print("\nREADING CLASSIFICATION")
    print("----------------------")

    for reading in readings:
        category = classify_reading(reading, warning_limit, critical_limit)
        print(f"{reading} °C -> {category}")


def display_summary(readings, warning_limit, critical_limit):
    """Print the numerical summary, category counts, and overall status."""
    number = len(readings)

    normal_count = count_category(
        readings, warning_limit, critical_limit, "NORMAL"
    )
    warning_count = count_category(
        readings, warning_limit, critical_limit, "WARNING"
    )
    critical_count = count_category(
        readings, warning_limit, critical_limit, "CRITICAL"
    )

    normal_percentage = normal_count / number * 100
    warning_percentage = warning_count / number * 100
    critical_percentage = critical_count / number * 100

    status = determine_overall_status(warning_count, critical_count)

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings  : {number}")
    print(f"Total of readings   : {compute_total(readings)}")
    print(f"Average temperature : {compute_average(readings):.2f} °C")
    print(f"Minimum temperature : {find_minimum(readings)} °C")
    print(f"Maximum temperature : {find_maximum(readings)} °C")
    print(f"\nNORMAL   : {normal_count} ({normal_percentage:.2f}%)")
    print(f"WARNING  : {warning_count} ({warning_percentage:.2f}%)")
    print(f"CRITICAL : {critical_count} ({critical_percentage:.2f}%)")
    print(f"\nOverall Status: {status}")


def main():
    """Manage readings and use only the original readings for the summary."""
    readings = get_initial_readings()

    # Keep a separate copy so added readings do not change the summary.
    summary_readings = readings.copy()

    warning_limit = 30
    critical_limit = 35

    while True:
        display_menu()
        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            display_readings(readings)
        elif choice == "2":
            add_reading(readings, 0, 100)
        elif choice == "3":
            display_classifications(readings, warning_limit, critical_limit)
        elif choice == "4":
            display_summary(
                summary_readings, warning_limit, critical_limit
            )
        elif choice == "5":
            print("Thank you for using the Device Monitoring System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()