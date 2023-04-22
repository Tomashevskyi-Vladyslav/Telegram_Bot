import sus
function_temporary_variable = sus.random_number_enerator()
print(*function_temporary_variable,sep = '')
def function_to_check_sequence_of_numbers(sequence_check_sheet):## function creation
    'A function to check the elements of a list for convergent numbers'
    global function_temporary_variable
    counter = 0
    dictionary_for_numbering_correct_numbers = {0:'First', 1:'Second', 2:'Third ', 3:'Fourth'}## create a dictionary with a sequence of numbers
    count_element = 0
    for i in range(4):
        if int(sequence_check_sheet[counter])==function_temporary_variable[counter] :
            print(f'''{dictionary_for_numbering_correct_numbers[counter]} element in place''')
            count_element+=1
        elif int(sequence_check_sheet[counter]) in function_temporary_variable:
            print(f'''{dictionary_for_numbering_correct_numbers[counter]} the element is not in place, but it is in the hidden number''')
        else :
            print(f'''{dictionary_for_numbering_correct_numbers[counter]} the element is not in the cryptic number''')
        counter+=1
    if count_element==4:
        return 'Сongratulations you guessed the number'
sequence_check_sheet = list(input('Enter 4 digit number :'))
while True:
    if len(sequence_check_sheet)==4 and not sequence_check_sheet[0].isalpha() and not sequence_check_sheet[1].isalpha() and not sequence_check_sheet[2].isalpha() and not sequence_check_sheet[3].isalpha():
        if 'Сongratulations you guessed the number' == function_to_check_sequence_of_numbers(sequence_check_sheet):
            print('Congratulations you guessed the number')
            d = str(input('Do you want to continue :'))
            d = d.upper()
            if d=='YES':
                function_temporary_variable = sus.random_number_enerator()
                print(*function_temporary_variable,sep = '')
                sequence_check_sheet = list(input('Enter 4 digit number :'))
                d = 0
                continue
            else :
                break
    sequence_check_sheet = list(input('Enter 4 digit number :'))
    