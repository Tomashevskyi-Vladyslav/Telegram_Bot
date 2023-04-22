import random ## import the library random
list_to_store_random_numbers1 = 0
def random_number_enerator():
    'This function fills the list with completely random numbers in the range from 0 to 9 that cannot be repeated.'
    global list_to_store_random_numbers1
    list_to_store_random_numbers = []## list to collect random values ​​of type(int)
    while len(list_to_store_random_numbers)!=4:## loop to fill the list with random values ​​in the range from 0 to 9. When the list is filled with the required number of elements, the loop will end.
        s = random.randint(0,9)## selection of a random element from one to 9
        if not s in list_to_store_random_numbers:
            list_to_store_random_numbers.append(s)
        else :
            continue
    list_to_store_random_numbers1 = []
    for i in list_to_store_random_numbers:
        list_to_store_random_numbers1.append(str(i))
    list_to_store_random_numbers1 = ''.join(list_to_store_random_numbers1)
    return list_to_store_random_numbers
