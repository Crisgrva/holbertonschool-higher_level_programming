#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if x % 15 == 0:
            print("{}".format("FizzBuzz"), end="")
        elif x % 5 == 0:
            print("{}".format("Buzz"), end="")
        elif x % 3 == 0:
            print("{}".format("Fizz"), end="")
        else:
            print("{:d}".format(x), end="")

        if x != 100:
            print("{}".format(" "), end="")
