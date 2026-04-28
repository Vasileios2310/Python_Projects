import numpy as np
import tkinter as tk
from tkinter import messagebox

class RainData:
    def __init__(self):
        """
        Αρχικοποιεί δεδομένα έντασης και διάρκειας βροχής
        """
        self.rain_intesity = np.array(
            [0.0, 1.6, 4.0, 0.0, 0.0, 2.3, 3.6, 0.0, 0.7, 1.5,
             0.0, 2.1, 0.0, 3.2, 0.0, 0.0, 3.7, 1.9, 0.0, 0.0,
             8.5, 5.2, 0.0, 0.0, 3.3, 3.6, 0.0, 0.5, 1.2, 0.0])
        ## πίνακας διάρκειας
        self.rain_duration = np.array(
            [0, 3, 4, 0, 0, 2, 1, 0, 5, 3,
             0, 3, 0, 2, 0, 0, 1, 4, 0, 0,
             18, 12, 0, 0, 4, 4, 0, 1, 2, 0])

        ## πίνακας με 3 δεκαήμερα
        self.intesity_by_ten = self.rain_intesity.reshape(3,10)
        
        
    def total_rain(self):
        """
        Υπολογίζει συνολική διάρκεια βροχής.
        Υπολογίζει συνολικό ύψος βροχής για τον μήνα
        """
        
        total_duration = np.sum(self.rain_duration)
            
        ## ύψος βροχής ανα ημέρα
        rain_height_per_day = self.rain_intesity * self.rain_duration
            
        ## συνολικό ύψος βροχής
        rain_height_total_month = np.sum(rain_height_per_day)
            
        return total_duration , rain_height_total_month
                         
    def min_max_rain_by_10(self):
        """
        Βρίσκει ελάχιστη και μέγιστη ένταση ανά δεκαήμερο
        """
        
        results = []
        for i in range(3):
            ten_days = self.intesity_by_ten[i]
            
            min_result = np.min(ten_days)
            max_result = np.max(ten_days)
            
            results.append((min_result , max_result))
        return results
        
    def moving_average(self):
        """
        Υπολογίζει κινητό μέσο όρο 5 ημερών
        """
        
        results = []
        
        for i in range(23,30):
            window_size = self.rain_intesity[i - 4 : i + 1]
            
            average = np.mean(window_size)
            
            results.append((i + 1, average))
        return results
    
    def sorted_numpy(self):
        """
        Ταξινομεί τον πίνακα με χρήση NumPy
        """
        
        sorted_array = np.sort(self.rain_intesity)
        return sorted_array
    
    def bubble_sort(self):
        """
        Υλοποιεί χειροκίνητη ταξινόμηση bubble sort
        """
        
        copy_array = self.rain_intesity.copy()
        len_array = len(copy_array)
        
        for i in range(len_array):
            for j in range(0 , len_array - i - 1):
                
                if copy_array[j] > copy_array[j + 1]:
                    temp = copy_array[j]
                    copy_array[j] = copy_array[j+1]
                    copy_array[j + 1] = temp
                    
        return copy_array

class RainUI:
    def __init__(self):
        """
        Αρχικοποιεί δεδομένα και GUI
        """
        
        self.data = RainData()

        self.root = tk.Tk()
        self.root.title("Ανάλυση Βροχόπτωσης")
        self.root.geometry("420x380")
        self.root.configure(bg="#e6f2ff")

        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        """
        Δημιουργεί κουμπιά και τίτλο στο παράθυρο
        """
        title = tk.Label(
            self.root,
            text="Ανάλυση Βροχόπτωσης",
            font=("Arial", 16, "bold"),
            bg="#e6f2ff"
        )
        title.pack(pady=10)

        tk.Button(self.root, text="1. Συνολικά Στατιστικά", width=30,
          command=self.show_total_stats).pack(pady=5)

        tk.Button(self.root, text="2. Min/Max ανά δεκαήμερο", width=30,
                command=self.show_min_max).pack(pady=5)

        tk.Button(self.root, text="3. Κινητός Μέσος Όρος", width=30,
                command=self.show_moving_avg).pack(pady=5)

        tk.Button(self.root, text="4. Ταξινόμηση", width=30,
                command=self.show_sorting).pack(pady=5)

        tk.Button(self.root, text="5. Έξοδος", width=30,
                command=self.root.quit).pack(pady=15)

    def show_total_stats(self):
        """
        Εμφανίζει συνολικά στατιστικά βροχής
        """
        
        duration, height = self.data.total_rain()

        message = f"Συνολική διάρκεια: {duration} ώρες\n"
        message += f"Συνολικό ύψος βροχής: {height:.2f} mm"

        self.show_text_window("Συνολικά Στατιστικά", message)

    def show_min_max(self):
        """
        Εμφανίζει min/max ανά δεκαήμερο
        """
        
        results = self.data.min_max_rain_by_10()

        message = ""
        for i, (mn, mx) in enumerate(results, start=1):
            message += f"{i}ο δεκαήμερο:\n"
            message += f"  Ελάχιστη: {mn}\n"
            message += f"  Μέγιστη: {mx}\n\n"

        self.show_text_window("Min / Max ανά δεκαήμερο", message)

    def show_moving_avg(self):
        """
        Εμφανίζει κινητό μέσο όρο
        """
        
        results = self.data.moving_average()

        message = ""
        for day, avg in results:
            start_day = day - 4
            message += f"Ημέρα {day} (από {start_day} έως {day}): {avg:.2f} mm/h\n"

        self.show_text_window("Κινητός Μέσος Όρος", message)

    def show_sorting(self):
        """
        Συγκρίνει ταξινόμηση NumPy και bubble sort
        """
        
        sorted_np = self.data.sorted_numpy()
        sorted_bubble = self.data.bubble_sort()

        message = "Ταξινόμηση με NumPy:\n"
        message += str(sorted_np) + "\n\n"

        message += "Ταξινόμηση με Bubble Sort:\n"
        message += str(sorted_bubble)

        self.show_text_window("Ταξινόμηση", message)
        
    def show_text_window(self, title, content):
        """
        Δημιουργεί νέο παράθυρο για εμφάνιση κειμένου
        """
        
        window = tk.Toplevel(self.root)
        window.title(title)
        window.geometry("500x350")

        frame = tk.Frame(window)
        frame.pack(fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")

        text = tk.Text(frame, yscrollcommand=scrollbar.set, wrap="word")
        text.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=text.yview)

        text.insert("end", content)
        text.config(state="disabled")

  
if __name__ == "__main__":
    app = RainUI() 
           
                    
# data = RainData()
# print(data.rain_intesity)  
# print(data.rain_duration)
# print(data.intesity_by_ten)

# duration , height = data.total_rain()
# print("Συνολική διάρκεια:", duration)
# print("Συνολικό ύψος βροχής:", height)

# result = data.min_max_rain_by_10()

# for i, (min , max) in enumerate(result , start=1):
#     print(f"{i} δεκαήμερο η ελάχιστη τιμη ειναι : {min}  και  η μέγιστη είναι {max}")

# results_moveing = data.moving_average()
# for day , avg in results_moveing:
#     print(f"Ημέρα {day} --> {avg:.2f} mm/h")


# sorted_np = data.sorted_numpy()
# sorted_bubble = data.bubble_sort()

# print("Numpy sort:")
# print(sorted_np)

# print("\nBubble sort:")
# print(sorted_bubble)