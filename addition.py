import random
import time

mode = int(input("[1]+ or [2]+/- or [3]x or [4]/"))

if mode == 1 or mode == 2:
    if mode == 1:
        print ('addition selected')
    if mode == 2:
        print('addition and substraction selected')
    number_digits = int(input('enter number of digits per number'))
    number_sets = int(input('enter number sets'))
    smallest_number = int(1 * 10**(number_digits-1))
    largest_number = int(1 * 10**(number_digits))
    num_1 = (random.randint(smallest_number,largest_number))
    num_2 = (random.randint(smallest_number, largest_number))
    correct_answer = num_1 + num_2
    print(int(num_1))
    time.sleep(3)
    print(int(num_2))
    #print(int(correct_answer))
    for i in range(1, (number_sets - 1)):
        time.sleep(3)
        if mode == 1:
            num_2 = (random.randint(smallest_number, largest_number))
        if mode == 2:
            num_2 = (random.randint(-correct_answer, largest_number))
        correct_answer += num_2
        print(int(num_2))
        #print(int(correct_answer))

if mode == 3:
    print ('multiplication selected')
    num1_digits = int(input('Enter number of digits for 1st number'))
    num2_digits = int(input('Enter number of digits for 2nd number'))
    num1_smallest_number = int(1 * 10 ** (num1_digits - 1))
    num1_largest_number = int(1 * 10 ** (num1_digits))
    num2_smallest_number = int(1 * 10 ** (num2_digits - 1))
    num2_largest_number = int(1 * 10 ** (num2_digits))
    num_1 = (random.randint(num1_smallest_number, num1_largest_number))
    num_2 = (random.randint(num2_smallest_number, num2_largest_number))
    correct_answer = num_1 * num_2
    print (num_1, 'x' ,num_2)


if mode == 4:
    print('division selected')
    dividend_digits = int(input('Enter number of digits for dividend'))
    divider_digits = int(input('Enter number of digits for divider'))
    quotient_digits = int(dividend_digits-divider_digits)
    divider_smallest_number = int(1 * 10 ** (divider_digits - 1))
    divider_largest_number = int(1 * 10 ** (divider_digits))
    quotient_smallest_number = int(1 * 10 ** (quotient_digits - 1))
    quotient_largest_number = int(1 * 10 ** (quotient_digits))
    divider = (random.randint(divider_smallest_number, divider_largest_number))
    quotient = (random.randint(quotient_smallest_number, quotient_largest_number))
    correct_answer = quotient
    dividend = int(divider * quotient)
    print (dividend, '/'  ,divider)

guess = int(input('answer'))
print(correct_answer)

for r in range (1,10):

    if mode == 1 or mode == 2:
        num_1 = (random.randint(smallest_number, largest_number))
        num_2 = (random.randint(smallest_number, largest_number))
        correct_answer = num_1 + num_2
        print(int(num_1))
        time.sleep(3)
        print(int(num_2))
        # print(int(correct_answer))
        for i in range(1, (number_sets - 1)):
            time.sleep(3)
            if mode == 1:
                num_2 = (random.randint(smallest_number, largest_number))
            if mode == 2:
                num_2 = (random.randint(-correct_answer, largest_number))
            correct_answer += num_2
            print(int(num_2))

    if mode == 3:
        num_1 = (random.randint(num1_smallest_number, num1_largest_number))
        num_2 = (random.randint(num2_smallest_number, num2_largest_number))
        correct_answer = num_1 * num_2
        print(num_1, 'x', num_2)

    if mode == 4:
        divider = (random.randint(divider_smallest_number, divider_largest_number))
        quotient = (random.randint(quotient_smallest_number, quotient_largest_number))
        correct_answer = quotient
        dividend = int(divider * quotient)
        print(dividend, '/', divider)

    guess = int(input('answer'))
    print(correct_answer)



