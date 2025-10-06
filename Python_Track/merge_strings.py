word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
l_1 = list(word1)
l_2 = list(word2)
l = []
n = 0
while True:
    l.append(l_1.pop(n))
    l.append(l_2.pop(n))
    n += 1  
    if len(l_1) == 0 or len(l_2) == 0:
        break
done = "".join(l)


