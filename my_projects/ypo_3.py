import pandas as pd
import matplotlib.pyplot as plt
import os


# ================== ΦΟΡΤΩΣΗ ΔΕΔΟΜΕΝΩΝ ==================
#def load_movies(filename):
filename = 'imdb_top_250.csv'
try:
    with open(filename , "rb") as input_file:
        data = pd.read_csv(filename , na_values=["null"])
        print(f"Successfully loaded {filename} into a dataframe")
except FileNotFoundError:
    print('Please insert a valid file')
    

data_movies = data.filter(["Title" , "Genre"  , "IMDB rating" , "Rating count"])
### https://www.geeksforgeeks.org/data-analysis/working-with-missing-data-in-pandas/
#print(data_movies.dropna(inplace=True)) ## remove missing values
#print(data_movies.fillna(66666 , inplace=True)) ## no replace happened
# print(data_movies["Title"].notnull())
# print(data_movies["Genre"].notnull())
# print(data_movies["IMDB rating"].notnull())
# print(data_movies["Rating count"].notnull())

data_movies["IMDB rating"].astype(int)
data_movies["Rating count"].astype(float)

# ================== 10 ΤΑΙΝΙΕΣ ΜΕ ΜΕΓΑΛΥΤΕΡΗ ΒΑΘΜΟΛΟΓΙΑ ==================
# def top_10_by_rating(df):
## https://www.geeksforgeeks.org/python/pandas-drop-column/
##data_top10_IMDB_rating = data_movies.nlargest(10 , ["IMDB rating"])
##print(data_top10_IMDB_rating.drop('Rating count' , axis=1))



# # ================== ΜΕΣΗ ΒΑΘΜΟΛΟΓΙΑ ΑΝΑ ΕΙΔΟΣ ==================
# def average_rating_by_genre(df):
# data_mean_score = data_movies.groupby('Genre')['IMDB rating'].mean().sort_values(ascending=False)
# print(data_mean_score)






# # ================== ΠΛΗΘΟΣ ΤΑΙΝΙΩΝ ΜΕ ΨΗΦΟΥΣ ΠΑΝΩ ΑΠΟ ΤΟΝ ΜΕΣΟ ΟΡΟ ==================
# def count_movies_above_avg_votes(df):
## https://stackoverflow.com/questions/31037298/pandas-get-column-average-mean
data_mean_rating = data_movies.loc[:, 'Rating count'].mean()
# print(data_mean_rating)
# all_data = []
# for data in data_movies["Rating count"]:
#     if data > data_mean_rating:
#         all_data.append(data)
# print(len(all_data))

#count_movies = (data_movies["Rating count"] > data_mean_rating).sum()
#print(count_movies)


# # ================== ΔΙΑΦΟΡΑ ΜΕΓΙΣΤΗΣ - ΕΛΑΧΙΣΤΗΣ ΒΑΘΜΟΛΟΓΙΑΣ ==================
# def rating_range(df):
    
#     data_min = df["IMDB rating"].min()
#     data_max = df["IMDB rating"].max()
#     final_range = data_max - data_min
#     return final_range


# # ================== ΔΙΑΓΡΑΜΜΑ ΓΡΑΜΜΗΣ (TOP 5 ΒΑΘΜΟΛΟΓΙΑ) ==================
# def line_chart_top5_by_rating(df):
# top_5 = data_movies.nlargest(5 , "IMDB rating")
# y_vals = top_5["IMDB rating"]
# x_vals = top_5["Title"]

# plt.plot(x_vals , y_vals)
# plt.xlabel('Top5 ταινίες')
# plt.ylabel('βαθμολογία ταινάις')
# plt.title('Βαθμολογία')
# plt.legend(loc='upper center')  
# plt.show()


# # ================== ΡΑΒΔΟΓΡΑΜΜΑ ΠΛΗΘΟΥΣ ΑΝΑ ΕΙΔΟΣ ==================
# def bar_chart_top5_genres(df):

genres = data_movies["Genre"].str.split(" | ", regex=False)

genres = genres.explode()
print(genres)

genres_count = genres.value_counts()

top_5 = genres_count.head(5)

plt.bar(top_5.index , top_5.values)
plt.xlabel("Είδη ταινιών")
plt.ylabel("Πλήθος ταινιών")
plt.title("Top 5 Genres")
plt.show()


# ================== ΚΥΡΙΟ ΠΡΟΓΡΑΜΜΑ ==================
# if __name__ == '__main__':
#     filename = 'imdb_top_250.csv'
#     df = load_movies(filename)

#     # Απλό μενού επιλογών για τον χρήστη
#     while True:
#         print('\n=== Μενού Επιλογών ===')
#         print('1. Top 10 ταινίες με τη μεγαλύτερη βαθμολογία')
#         print('2. Μέση βαθμολογία ανά είδος')
#         print('3. Πλήθος ταινιών με ψήφους πάνω από τον μέσο όρο')
#         print('4. Διαφορά μέγιστης - ελάχιστης βαθμολογίας')
#         print('5. Διάγραμμα γραμμής (Top 5 ταινίες με καλύτερη βαθμολογία)')
#         print('6. Ραβδόγραμμα πλήθους ανά είδος (Top 5 είδη)')
#         print('7. Έξοδος')

#         choice = input('Επιλέξτε ενέργεια: ')

#         if choice == '1':
#             top_10_by_rating(df)
#         elif choice == '2':
#             average_rating_by_genre(df)
#         elif choice == '3':
#             count_movies_above_avg_votes(df)
#         elif choice == '4':
#             rating_range(df)
#         elif choice == '5':
#             line_chart_top5_by_rating(df)
#         elif choice == '6':
#             bar_chart_top5_genres(df)
#         elif choice == '7':
#             print('Έξοδος...')
#             break
#         else:
#             print('Μη έγκυρη επιλογή!')
