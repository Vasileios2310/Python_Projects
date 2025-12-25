def total(initial = 5 , *numbers , **keywords):
    """_summary_
                Όταν δηλώνουμε μια παράμετρο με αστερίσκο, όπως το *param, τότε όλα τα ορίσματα των οποίων η θέση
                βρίσκεται από αυτό το σημείο μέχρι το τέλος, συγκεντρώνονται σαν λίστα που ονομάζεται 'param'. Παρόμοια
                όταν δηλώνουμε παράμετρο διπλό αστερίσκο όπως το **param, τότε όλα τα ορίσματα με λέξεις κλειδιά, από
                αυτό το σημείο μέχρι το τέλος συγκεντρώνονται σαν λεξικό που ονομάζεται 'param'.
                    Args:
        initial (int, optional): _description_. Defaults to 5.

    Returns:
        _type_: _description_
    """
    count = initial
    for number in numbers:
        count = count + number
    for keyword in keywords:
        count = count + keywords[keyword]
    return count

print(total(10, 1 , 2 , 3 , vegetables = 50 , fruits = 100))


