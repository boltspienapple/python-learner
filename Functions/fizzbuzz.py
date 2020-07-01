for n in range(30):
    if n % 3 == 0:
        print("Fizz")
    if n % 5 ==0:
        print("Buzz")
    if n % 3 == 0 and n % 5 == 0:
        print("Fizz Buzz")
    else:
        print(n)