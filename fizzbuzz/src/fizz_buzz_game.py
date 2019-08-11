def fizz_buzz(i):
    if type(i) == str or type(i) == float or i <= 0:
        return "only positive integers are allowed"
    if i % 3 == 0 and i % 5 == 0:
        return "Fizz Buzz"
    elif i % 3 == 0 and i % 5 != 0 or '3' in str(i):
        return "Fizz"
    elif i % 5 == 0 and i % 3 != 0 or '5' in str(i):
        return "Buzz"
    else:
        return i



def main():
    for i in range(1, 101):
        result = fizz_buzz(1.5)
        print(result)

#main()


