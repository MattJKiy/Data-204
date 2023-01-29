# Tuesday 24/01/2023 - Afternoon Exercises
print("\nQ1a\n")


# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def divisors(x):
    num = int(input("enter: "))  # asking for an input, input type is int. got a prompt which says enter.
    a = []  # create list

    for i in range(1, num + 1):  # for loop. i = 1 to the number you entered

        if num % i == 0:  # if number is modulus of i, then print it, otherwise go to next number, until you get to num.
            a.append(i)
    print(a)  # print list

#divisors(12)


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:

def factor(x,y):
    if x % y == 0:
        print(True)
    elif y % x == 0:
        print(True)
    else:
        print(False)

#factor(7,7)


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:

def positionAlphabet():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z", " "]
    letter = str(input("enter a letter: "))
    postion = alphabet.index(letter) + 1
    print(postion)

#positionAlphabet()


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

def nameID():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z", " "]
    id_name=""
    name = str(input("enter a name: "))
    for i in name:
        id_name += str(alphabet.index(i))
    print (id_name)

#nameID()

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:

def password():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z", " "]
    id_name = ""
    name = str(input("enter a name: "))
    for i in name:
        id_name += str(alphabet.index(i))


    total = 0
    for i in range(0,len(id_name)):
        total = total + int(id_name[i])
    print(int(id_name) - total)

#password()

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def prime():
        number = int(input("Please enter a number: "))
        for i in range(2, number):
            if number == 1:
                print(number, "is not a prime number")
            elif number % i == 0:
                print(' False, not prime')
                break
            else:
                print("True, is a prime number")
                break

#prime()

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:

def prime_error():
        try:
            number = int(input("Please enter a number: "))
            for i in range(1, number):
                if number == 1:
                    print(number, "is not a prime number")
                elif number % i == 0:
                    print(number, "is not a prime number")
                    break
                else:
                    print(number, "is a prime number")
                    break
        except ValueError:
            print('This is not a number')

prime_error()

# -------------------------------------------------------------------------------------- #
