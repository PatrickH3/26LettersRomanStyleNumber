import timeit

ROMAN_SYMBOLS = "IVXLCDMABEFGHJKNOPQRSTUWYZ"
ROMAN_NUMBER_MASK = "0000100002"
ROMAN_NUMBER_ORDER = "123212342"


def arabic_to_extended_roman_gpt(number):
    if number < 1 or number > 8_999_999_999_999:
        raise ValueError("Число повинно бути в діапазоні від 1 до 8,999,999,999,999")

    value_to_symbol = [
        (5000000000000, 'Z'),
        (1000000000000, 'Y'),
        (500000000000, 'X'),
        (100000000000, 'W'),
        (50000000000, 'V'),
        (10000000000, 'U'),
        (5000000000, 'T'),
        (1000000000, 'S'),
        (500000000, 'R'),
        (100000000, 'Q'),
        (50000000, 'P'),
        (10000000, 'O'),
        (5000000, 'N'),
        (1000000, 'M'),
        (500000, 'L'),
        (100000, 'K'),
        (50000, 'J'),
        (10000, 'I'),
        (5000, 'H'),
        (1000, 'G'),
        (500, 'F'),
        (100, 'E'),
        (50, 'D'),
        (10, 'C'),
        (5, 'B'),
        (1, 'A')
    ]

    roman_numeral = ''
    for value, symbol in value_to_symbol:
        while number >= value:
            roman_numeral += symbol
            number -= value
    return roman_numeral

# Тестування програми gpt
def arabic_to_extended_roman_gpt_test():
    test_numbers = [1, 58, 3999, 123456789, 1000000000000, 3000000000000, 8999999999999]
    for number in test_numbers:
        arabic_to_extended_roman_gpt(number)
        #print(f"{number} -> {arabic_to_extended_roman_gpt(number)}")


def turn_a_single_number_into_roman(arabic_single_symbol, arabic_single_symbol_class):

    #Identify start possition in ROMAN_NUMBER_MASK
    if int(ROMAN_NUMBER_ORDER[arabic_single_symbol-1]) < int(ROMAN_NUMBER_ORDER[arabic_single_symbol-2]):
        start_position = arabic_single_symbol-1
    else:
        start_position = (arabic_single_symbol//5)*4

    #Identify number of symbols we have to take from start_position in ROMAN_NUMBER_MASK
    number_of_symbols = start_position + int(ROMAN_NUMBER_ORDER[arabic_single_symbol-1])

    #Creating a mask for future number
    roman_symbol_mask = ROMAN_NUMBER_MASK[start_position: number_of_symbols]

    #Applying mask to ROMAN_SYMBOLS to get our roman number
    roman_symbol_result = ''.join(map(lambda index: ROMAN_SYMBOLS[int(index)+arabic_single_symbol_class*2], roman_symbol_mask))

    return roman_symbol_result


def arabic_to_roman(arabic_number):
    #Моя геніальна функція, взагалі то геніальність в функції turn_a_single_number_into_roman
    roman_result =""
    for i in range(len(arabic_number)-1, -1, -1):
        roman_result = turn_a_single_number_into_roman(int(arabic_number[i]), len(arabic_number)-i-1) + roman_result
    return roman_result

def arabic_to_roman_test():
    test_numbers = [1, 58, 3999, 123456789, 1000000000000, 3000000000000, 8999999999999]
    for number in test_numbers:
        arabic_to_roman(str(number))
        #print(f"{number} -> {arabic_to_roman(str(number))}")

#def print_all_roman():
#    for i in range(1, 4000):
#        print(f"{i} | {arabic_to_roman(str(i))}")

def main():
    #arabic_number = input("Give me an arabic number under 8,999,999,999,999: ")
    #print(f"{arabic_number} - {arabic_to_roman(arabic_number)}")
    execution_time_gpt = timeit.timeit(arabic_to_roman_test, number=10)
    print(f"gpt: {execution_time_gpt}")
    execution_time_me = timeit.timeit(arabic_to_extended_roman_gpt_test, number=10)
    print(f"Me: {execution_time_me}")
    print(f"gpt_alg_time/my_alg_time = {execution_time_gpt/execution_time_me}")

if __name__ == "__main__":
    main()