from collections import Counter

def count_with_freq_compr(my_list):
    counts = Counter(my_list)
    freq_dict = {item : counts[item] for item in set(my_list)}
    
    sorted_by_value = dict(sorted(freq_dict.items() , key=lambda item : item[1]))
    
    print(sorted_by_value)

def count_with_manul_loop(my_list):
    freq_dict = {}
    
    for item in my_list:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
            
    print(freq_dict)
        

def main():
    fruits = ["apple","banana","orange","grape","strawberry","papaya","banana",
              "apple","peach","banana","banana","lime","coconut","apple",
              ]
    
    count_with_freq_compr(fruits)
    print('-' * 50)
    count_with_manul_loop(fruits)
    
if __name__ == '__main__':
    main()