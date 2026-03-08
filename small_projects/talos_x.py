import pickle
import sys
from datetime import datetime

# --- Ορισμός Κλάσης ---

class SensorReading:
    """
    Κλάση που αναπαριστά μια μεμονωμένη καταγραφή από έναν αισθητήρα.
    """
    def __init__(self, sensor_id, timestamp, value, reading_type):
        """
        Αρχικοποίηση της καταγραφής.
        :param sensor_id: Η ταυτότητα του αισθητήρα (str)
        :param timestamp: Η χρονική στιγμή καταγραφής (str)
        :param value: Η τιμή της μέτρησης (float ή int)
        :param reading_type: Ο τύπος της μέτρησης (π.χ. TEMP, VOLT, INTR, ACC)
        """
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.value = value
        self.reading_type = reading_type

    def __str__(self):
        """
        Επιστρέφει μια συμβολοσειρά αναπαράστασης της καταγραφής.
        """
        return f"Ταυτότητα αισθητήρα: {self.sensor_id} τη χρονική στιγμή: {self.timestamp} , με τιμή της μέτρησης: {self.value} και τύπο μέτρησης: {self.reading_type}"

# --- Συναρτήσεις Λειτουργικότητας ---
def read_log_file(filename):
    """
    Διαβάζει το αρχείο καταγραφής και επιστρέφει μια λίστα με αντικείμενα SensorReading.
    """

    print(f"\n--- Ανάγνωση αρχείου: {filename} ---")
    readings = []
    valid_types = {"TEMP" , "VOLT" , "INTR" , "ACC"}
    valid_sensors = {
        "TEMP" : {"Motor_L" , "Motor_R" , "CPU_Core"},
        "VOLT" : {"Bat_Main" , "Bat_Backup"},
        "INTR" : {"Case_Back" , "Case_Front"},
        "ACC"  : {"IMU_Main"}
    }

    try:
        with open(filename , "r" , encoding="utf-8", newline='\n') as file:   
            for line , raw in enumerate(file , start=1):
                try:
                    original = raw.rstrip("\n")
                    line = original.strip()
                    if not line: continue

                    parts = [p.strip() for p in line.split(",")]

                    if len(parts) != 4: 
                        print(f"Error in reading line{line}")   # λείπουν απαραίτητα πεδία
                        continue
                    
                    timestamp , reading_type , sensor_id , raw_value = parts
                    
                    # reading_type check
                    if reading_type not in valid_types:
                        print(f"Line {line} : 'Αγνωστος τύπος '{reading_type} - Αγνοηθηκε. -> Line {original}'")
                        continue
                    
                    # sensor_id check for this reading_type
                    if sensor_id not in valid_sensors[reading_type]:
                        print(f"Line {line} : 'Αγνωστος Sensor_ID '{sensor_id} για τύπο {reading_type}'")
                        continue

                    times = timestamp.split(":")
                    if len(times) != 3:
                        print(f"Error reading line {line} : λάθος time_stamp format > Line ' {original}'")
                        continue

                    hour , minute , second = map(int , times)
                    if not (0 <= hour <=23 and 0<= minute <= 59 and 0<= second <= 59):
                        print(f"Error reading line {line} : λάθος time_stamp τιμή -> Line' {original}'")
                        continue
                    
                     # value check
                    try:
                        value = float(raw_value)
                    except ValueError as ex:
                        print(f"Error reading line {line}: {ex} -> Line: '{original}'")
                        continue

                    # INTR check
                    if reading_type == "INTR" and value not in (0, 1, 0.0, 1.0):
                        print(f"Line {line}: Μη έγκυρη τιμή INTR '{raw_value}' - Αγνοήθηκε. -> Line: '{original}'")
                        continue

                    reading = SensorReading (
                    timestamp = parts[0],
                    reading_type = parts[1],
                    sensor_id = parts[2],
                    value = float(parts[3])
                    )
                    readings.append(reading)
                    
                except  (ValueError , IndexError) as ex:
                    print(f"Error reading line {line} : {ex} --> Line : {line.rstrip()}")
                    continue
                
    except FileNotFoundError:
        print(f"File with name {filename} not found")
        return []
    print(f"Ολοκληρώθηκε. Φορτώθηκαν {len(readings)} έγκυρες εγγραφές")
    return readings
    

def print_statistics(data_list):
    """
    Εμφανίζει πλήθος καταγραφών ανά τύπο και Min/Max τιμές.
    :param data_list: Η λίστα με τα αντικείμενα SensorReading
    """
    types = ["TEMP" , "VOLT" , "INTR" , "ACC"]
    
    print("\n--- Στατιστικά Καταγραφών ---")
    if not data_list:
        print("Δεν υπάρχουν δεδομένα προς επεξεργασία.")
        return
    
    print("\n Ανιχνεύθηκαν (Πλήθος ανα τύπο): ")
    counts = {t: 0 for t in types}
    for r in data_list:
        if r.reading_type in counts:
            counts[r.reading_type] += 1
            
    for t in types:
        print(f" - {t} : {counts[t]}")
      
    print("\n Αναλυτικά Στατιστικά Μετρήσεων ")
    
    for t in types:
        type_readings = [r for r in data_list if r.reading_type == t]
        if not type_readings:
            continue
        
        values = [r.value for r in type_readings]
        t_min = min(values)
        t_max = max(values)
        
        print(f"[ΤΥΠΟΣ: {t}]")
        print(f" >> GLOBAL {t} : Min {t_min:.2f} , Max {t_max:.2f}")
        
        # Min/Max sensor_id
        sen_id = {}
        for r in type_readings:
            sen_id.setdefault(r.sensor_id , []).append(r.value)
        
        for s_id in sorted(sen_id.keys()):
            s_id_min = min(sen_id[s_id])
            s_id_max = max(sen_id[s_id])
            print(f"    * ID '{s_id}' : Min : {s_id_min:.2f} , Max : {s_id_max:.2f}")
            
        print()

def save_to_pickle(data_list, filename="robot_data.pkl"):
    """
    Αποθηκεύει τη λίστα δεδομένων σε δυαδικό αρχείο.
    """
    try:
        with open(filename , 'wb') as f:
            pickle.dump(data_list , f)
        print(f"Επιτυχής αποθήκευση στο {filename}")        
    except (OSError , pickle.PickleError ) as ex:
        print(f"Σφάλμα αποθήκευσης στο {filename} : {ex}")
    

def load_pkl(filename):
    """
    Φορτώνει δεδομένα από ένα αρχείο pickle και τα επιστρέφει σε λίστα.
    """
    print(f"\n--- Φόρτωση από {filename} ---")
    
    data_list = []
    
    try:
        with open(filename , 'rb') as input_file:
            data_list = pickle.load(input_file)
        print(f"Επιτυχής φόρτωση απο το {filename} σε λίστα")
        return data_list    
    except FileNotFoundError as ex1:
        print(f"Το αρχείο {filename} δεν βρέθηκε : {ex1}")
        return data_list
    except (OSError , pickle.PickleError ) as ex2:
        print(f"Σφάλμα φόρτωσης απο το {filename} : {ex2}")
    


# --- Κύριο Μενού ---
def main():
    # Η τοπική λίστα που θα κρατάει τα δεδομένα μας κατά την εκτέλεση
    sensor_data = []

    while True:
        print("\n=== MENOY ΔΙΑΧΕΙΡΙΣΗΣ ROBOT TALOS-X ===")
        print("1. Read Log File")
        print("2. Print Statistics")
        print("3. Save to Binary (Pickle)")
        print("4. Load from Binary (Pickle)")
        print("9. Exit")

        choice = input("Επιλογή: ")

        if choice == '1':
            sensor_data = read_log_file("sensors_log.txt")
        elif choice == '2':
            print_statistics(sensor_data)
        elif choice == '3':
            save_to_pickle(sensor_data, "robot_data.pkl")
        elif choice == '4':
            sensor_data = load_pkl("robot_data.pkl")
            if sensor_data:
                print(f"Φορτώθηκαν {len(sensor_data)} καταγραφές.")
        elif choice == '9':
            print("Έξοδος...")
            break
        else:
            print("Λάθος επιλογή, προσπαθήστε ξανά.")

if __name__ == "__main__":
    main()