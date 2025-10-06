def swap_case(test_string: str) :
    test_string = list(test_string)
    for i in range(len(test_string)):
        if test_string[i].isupper():
            test_string[i] = test_string[i].lower()
        elif test_string[i].islower():
            test_string[i] = test_string[i].upper()

    return ''.join(test_string) 


string = swap_case("OpPs")
print(string)