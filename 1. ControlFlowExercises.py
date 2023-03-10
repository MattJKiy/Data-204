# Tuesday 24/01/2023 - Morning Exercises
print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:

print(x[0:5])

print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
for i in x:
    if i % 2 == 0:
        print(i)


print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
for i in range(5):
    if x[i] % 2 == 0:
        print(x[i])

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:

names = [i.split(' ') for i in names]
for list in names:
    print(list[0][0])


print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:

words = ' '.join(names)
indices = [i for i, x in enumerate(words) if x == " "]
print(indices)

print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:

names = [i.split(' ') for i in names]
for list in names:
    ans_2c = [list[0][0] + list[1][0]]
    print(ans_2c)


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:

for n in list_of_lists:
    if len(set(n)) == len(n):
        print(n)



# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:

while True:
    number = int(input("Please enter number "))
    if number > 100:
        print("Done, your number is " + str(number))
        break
    else:
            print("try again")

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:
while True:
    number = int(input("Please enter number "))
    if number == 1:
        print(number, "is not a prime number")
    elif number > 1:
        # check for factors
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number")
                print(i, "times", number // i, "is", number)
                break
        else:
            print(number, "is a prime number")
            break



