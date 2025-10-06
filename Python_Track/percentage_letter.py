s = input("Enter s: ")
letter_choose = input("Choose letter: ")
def percentange(letter : str):
    n = 0
    list_s = list(s)
   #h print(list_s)
    for i in list_s:
        if i == letter:
            n += 1
        else:
            pass
    
    percentange_word = float(n/len(s))*100 
    print(percentange_word)
    return percentange_word
    

done = percentange(letter_choose)