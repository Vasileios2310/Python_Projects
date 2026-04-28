import pandas as pd
import matplotlib.pyplot as plt
import os


# ================== ΦΟΡΤΩΣΗ ΔΕΔΟΜΕΝΩΝ ==================
def load_movies(filename):
    """
    Διαβάζει το csv και δημιουργεό ενα dataframe
    Καθαρίζει τα δεδεομένα και κρατάει συγκεκριμένες στήλες
    """
    
    try:
        df = pd.read_csv(filename , na_values=["null"])
        print(f"Successfully loaded {filename} into a dataframe")
    except FileNotFoundError:
        print('Please insert a valid file')
        return None
    except Exception as ex:
        print("Error in reading file" , ex)
        return None
    
    df = df.filter(["Title" , "Genre"  , "IMDB rating" , "Rating count"])
        
    df["IMDB rating"] = pd.to_numeric(df["IMDB rating"], errors="coerce")
    df["Rating count"] = pd.to_numeric(df["Rating count"], errors="coerce")
    
    df = df.dropna()
    return df

# ================== 10 ΤΑΙΝΙΕΣ ΜΕ ΜΕΓΑΛΥΤΕΡΗ ΒΑΘΜΟΛΟΓΙΑ ==================
def top_10_by_rating(df):
    """
    Βρίσκει τις 10 καλύτερες ταινίες
    """
    
    data_top10_IMDB_rating = df.nlargest(10 , ["IMDB rating"])
    print(data_top10_IMDB_rating[["Title", "Genre", "IMDB rating"]])



# ================== ΜΕΣΗ ΒΑΘΜΟΛΟΓΙΑ ΑΝΑ ΕΙΔΟΣ ==================
def average_rating_by_genre(df):
    """
    Υπολογίζει μέση βαθμολογία ανα είδος και ταξινομεί κατα φθίνουσα σειρά
    """
    
    data_mean_score = df.groupby('Genre')['IMDB rating'].mean().sort_values(ascending=False)
    print(data_mean_score)


# # ================== ΠΛΗΘΟΣ ΤΑΙΝΙΩΝ ΜΕ ΨΗΦΟΥΣ ΠΑΝΩ ΑΠΟ ΤΟΝ ΜΕΣΟ ΟΡΟ ==================
def count_movies_above_avg_votes(df):
    """
    Υπολογίζει το μέσο όρο των φήφων και μετρά τις ταινίες με τις περισσότερες ψήφους
    """
    
    data_mean_rating = df['Rating count'].mean()

    count_movies = (df["Rating count"] > data_mean_rating).sum()
    print("Μέσος όρος ψήφων:", data_mean_rating)
    print("Πλήθος ταινιών πάνω από μέσο όρο:", count_movies)


# ================== ΔΙΑΦΟΡΑ ΜΕΓΙΣΤΗΣ - ΕΛΑΧΙΣΤΗΣ ΒΑΘΜΟΛΟΓΙΑΣ ==================
def rating_range(df):
    """
    Βρίσκει μέγιστη και ελάχιστη βαθμολογία, υπολογίζει τη διαφορά τους
    """
    
    data_min = df["IMDB rating"].min()
    data_max = df["IMDB rating"].max()
    final_range = (data_max - data_min)
    print(f"Διαφορά μέγιστης - ελάχιστης:, {final_range:.2f}")


# # ================== ΔΙΑΓΡΑΜΜΑ ΓΡΑΜΜΗΣ (TOP 5 ΒΑΘΜΟΛΟΓΙΑ) ==================
def line_chart_top5_by_rating(df):
    """"
    Παίρνει τις 5 καλύτερες ταινίες και εμφανίζει γράφημα
    """
    top_5 = df.nlargest(5 , "IMDB rating")
    y_vals = top_5["IMDB rating"]
    x_vals = top_5["Title"]

    plt.plot(x_vals , y_vals , marker= 'o')
    plt.xlabel('Top5 ταινίες')
    plt.ylabel('βαθμολογία ταινάις')
    plt.title('Βαθμολογία')
    plt.legend(loc='upper center')  
    plt.show()


 # ================== ΡΑΒΔΟΓΡΑΜΜΑ ΠΛΗΘΟΥΣ ΑΝΑ ΕΙΔΟΣ ==================
def bar_chart_top5_genres(df):
    """
    Διαχωρίζει τα είδη ταινιών , τα μετρά και εμφανίζει τα 5 πιο συχνά
    """
    genres = df["Genre"].str.split(" | ", regex=False)
    genres = genres.explode()
    genres_count = genres.value_counts()
    top_5 = genres_count.head(5)

    plt.bar(top_5.index , top_5.values)
    plt.xlabel("Είδη ταινιών")
    plt.ylabel("Πλήθος ταινιών")
    plt.title("Top 5 Genres")
    plt.show()


# ================== ΚΥΡΙΟ ΠΡΟΓΡΑΜΜΑ ==================
if __name__ == '__main__':
    filename = 'imdb_top_250.csv'
    df = load_movies(filename)

    # Απλό μενού επιλογών για τον χρήστη
while True:
        print('\n=== Μενού Επιλογών ===')
        print('1. Top 10 ταινίες με τη μεγαλύτερη βαθμολογία')
        print('2. Μέση βαθμολογία ανά είδος')
        print('3. Πλήθος ταινιών με ψήφους πάνω από τον μέσο όρο')
        print('4. Διαφορά μέγιστης - ελάχιστης βαθμολογίας')
        print('5. Διάγραμμα γραμμής (Top 5 ταινίες με καλύτερη βαθμολογία)')
        print('6. Ραβδόγραμμα πλήθους ανά είδος (Top 5 είδη)')
        print('7. Έξοδος')

        choice = input('Επιλέξτε ενέργεια: ')

        if choice == '1':
            top_10_by_rating(df)
        elif choice == '2':
            average_rating_by_genre(df)
        elif choice == '3':
            count_movies_above_avg_votes(df)
        elif choice == '4':
            rating_range(df)
        elif choice == '5':
            line_chart_top5_by_rating(df)
        elif choice == '6':
            bar_chart_top5_genres(df)
        elif choice == '7':
            print('Έξοδος...')
            break
        else:
            print('Μη έγκυρη επιλογή!')
