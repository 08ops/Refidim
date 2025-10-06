def split_string(input_string: str):
    input_string = input_string.split(" ")
    jointed_string = "-".join(input_string)
    return jointed_string

string = split_string("This is a test string")
print(string)