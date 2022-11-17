# Angelo Smith
# 11/3/2022
# This code shows each number that are supposed to be divisble by 3 but it only shows the message of numbers divisible by 3 and 5
for n in range(1, 51):
    if n % 15 == 0:
        print("Divisible by both 3&5")
    elif n % 3 == 0:
        print("Divisible by 3")
    elif n % 5 == 0:
        print("Divisible by 5")

    else:
        print(n)
