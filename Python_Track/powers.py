n = int(input("Enter a n: "))
empyty_list = []
while n > 0:
    n -= 1
    empyty_list.append(n)

for i in reversed(empyty_list):
    print(i*i)