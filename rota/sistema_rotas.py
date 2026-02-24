continue_calc = 'yes'

while continue_calc == 'yes' or continue_calc =="no":

    

    distance = float(input('Enter the distance between the two companies in kilometers(km): '))
    cost = (abs(distance)*5)
    is_correct = input('Is the distance correct? (YES/NO) ')
    
    if is_correct.casefold() == 'yes':
        print(f'The delivery cost is R${cost:.2f}')

    elif is_correct.casefold() == 'no':
        distance = float(input('Enter the correct distance between the two companies in km: '))
        cost = (abs(distance)*5)
        print(f'The delivery cost is R${cost:.2f}')

    else: print('Invalid input. Please enter YES or NO.')

    continue_calc = input('Do you want to recalculate the delivery cost? (YES/NO) ')
    if continue_calc.casefold() == 'no':
        print('Thank you for using the delivery cost calculator. Goodbye!')
        break
