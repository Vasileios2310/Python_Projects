import pickle
import sys
from datetime import datetime

# --- Class Definition ---

class SensorReading:
    """
    Class representing a single reading from a sensor.
    """
    def __init__(self, sensor_id, timestamp, value, reading_type):
        """
        Initialize the reading.
        :param sensor_id: Sensor identifier (str)
        :param timestamp: Time of the reading (str)
        :param value: Measurement value (float or int)
        :param reading_type: Measurement type (e.g., TEMP, VOLT, INTR, ACC)
        """
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.value = value
        self.reading_type = reading_type

    def __str__(self):
        """
        Return a string representation of the reading.
        """
        return (
            f"Sensor ID: {self.sensor_id} at time: {self.timestamp}, "
            f"value: {self.value}, type: {self.reading_type}"
        )

# --- Functionality Functions ---
def read_log_file(filename):
    """
    Reads the log file and returns a list of SensorReading objects.
    """

    print(f"\n--- Reading file: {filename} ---")
    readings = []
    valid_types = {"TEMP", "VOLT", "INTR", "ACC"}
    valid_sensors = {
        "TEMP": {"Motor_L", "Motor_R", "CPU_Core"},
        "VOLT": {"Bat_Main", "Bat_Backup"},
        "INTR": {"Case_Back", "Case_Front"},
        "ACC": {"IMU_Main"}
    }

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_num, raw in enumerate(file, start=1):
                try:
                    original = raw.rstrip("\n")
                    line = original.strip()
                    if not line:
                        continue

                    parts = [p.strip() for p in line.split(",")]

                    if len(parts) != 4:
                        print(f"Error reading line {line_num}: missing required fields -> Line: '{original}'")
                        continue

                    timestamp, reading_type, sensor_id, raw_value = parts

                    # reading_type check
                    if reading_type not in valid_types:
                        print(f"Line {line_num}: unknown type '{reading_type}' - ignored -> Line: '{original}'")
                        continue

                    # sensor_id check for this reading_type
                    if sensor_id not in valid_sensors[reading_type]:
                        print(f"Line {line_num}: unknown Sensor_ID '{sensor_id}' for type {reading_type} - ignored -> Line: '{original}'")
                        continue

                    # timestamp check (HH:MM:SS)
                    times = timestamp.split(":")
                    if len(times) != 3:
                        print(f"Error reading line {line_num}: invalid timestamp format -> Line: '{original}'")
                        continue

                    hour, minute, second = map(int, times)
                    if not (0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59):
                        print(f"Error reading line {line_num}: invalid timestamp value -> Line: '{original}'")
                        continue

                    # value check
                    try:
                        value = float(raw_value)
                    except ValueError as ex:
                        print(f"Error reading line {line_num}: {ex} -> Line: '{original}'")
                        continue

                    # INTR check
                    if reading_type == "INTR" and value not in (0, 1, 0.0, 1.0):
                        print(f"Line {line_num}: invalid INTR value '{raw_value}' - ignored -> Line: '{original}'")
                        continue

                    reading = SensorReading(
                        timestamp=timestamp,
                        reading_type=reading_type,
                        sensor_id=sensor_id,
                        value=value
                    )
                    readings.append(reading)

                except (ValueError, IndexError) as ex:
                    # generic parsing error for this line
                    print(f"Error reading line {line_num}: {ex} -> Line: '{original}'")
                    continue

    except FileNotFoundError:
        print(f"File with name {filename} not found")
        return []

    print(f"Finished. Loaded {len(readings)} valid readings.")
    return readings


def print_statistics(data_list):
    """
    Displays number of readings per type and Min/Max values.
    :param data_list: List of SensorReading objects
    """
    types = ["TEMP", "VOLT", "INTR", "ACC"]

    print("\n--- Reading Statistics ---")
    if not data_list:
        print("No data available for processing.")
        return

    print("\nDetected (Count per Type):")
    counts = {t: 0 for t in types}
    for r in data_list:
        if r.reading_type in counts:
            counts[r.reading_type] += 1

    for t in types:
        print(f" - {t}: {counts[t]}")

    print("\nDetailed Measurement Statistics\n")

    for t in types:
        type_readings = [r for r in data_list if r.reading_type == t]
        if not type_readings:
            continue

        values = [r.value for r in type_readings]
        t_min = min(values)
        t_max = max(values)

        print(f"[TYPE: {t}]")
        print(f" >> GLOBAL {t}: Min {t_min:.2f}, Max {t_max:.2f}")

        # Min/Max per sensor_id
        sen_id = {}
        for r in type_readings:
            sen_id.setdefault(r.sensor_id, []).append(r.value)

        for s_id in sorted(sen_id.keys()):
            s_id_min = min(sen_id[s_id])
            s_id_max = max(sen_id[s_id])
            print(f"    * ID '{s_id}': Min {s_id_min:.2f}, Max {s_id_max:.2f}")

        print()


def save_to_pickle(data_list, filename="robot_data.pkl"):
    """
    Saves the data list into a binary pickle file.
    """
    try:
        with open(filename, "wb") as f:
            pickle.dump(data_list, f)
        print(f"Successfully saved to {filename}")
    except (OSError, pickle.PickleError) as ex:
        print(f"Save error to {filename}: {ex}")


def load_pkl(filename):
    """
    Loads data from a pickle file and returns it as a list.
    """
    print(f"\n--- Loading from {filename} ---")

    data_list = []

    try:
        with open(filename, "rb") as input_file:
            data_list = pickle.load(input_file)
        print(f"Successfully loaded from {filename} into a list.")
        return data_list

    except FileNotFoundError as ex1:
        print(f"File {filename} not found: {ex1}")
        return data_list

    except (OSError, pickle.PickleError) as ex2:
        print(f"Load error from {filename}: {ex2}")
        return data_list


# --- Main Menu ---
def main():
    # Local list that holds data during program execution
    sensor_data = []

    while True:
        print("\n=== TALOS-X ROBOT DATA MANAGEMENT MENU ===")
        print("1. Read Log File")
        print("2. Print Statistics")
        print("3. Save to Binary (Pickle)")
        print("4. Load from Binary (Pickle)")
        print("9. Exit")

        choice = input("Choice: ")

        if choice == '1':
            sensor_data = read_log_file("sensors_log.txt")
        elif choice == '2':
            print_statistics(sensor_data)
        elif choice == '3':
            save_to_pickle(sensor_data, "robot_data.pkl")
        elif choice == '4':
            sensor_data = load_pkl("robot_data.pkl")
            if sensor_data:
                print(f"Loaded {len(sensor_data)} readings.")
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()