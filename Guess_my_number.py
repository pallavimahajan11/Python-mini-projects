
import random

secret_number=random.randint(1,100)
num=int(input("Enter a guess between 1 to 100"))
while num != secret_number:

    if num>secret_number:
        print("Your guess is tooo high")
    else:
        print("Your guess is very low")
    print(" ")
    num=int(input("Enter a guess"))
print("Congrats ! The number you choose " +str(num)+"is an secret number")