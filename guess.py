import random
print("welcome to guessy wessy. You have 5 chances.")
chances=5
n=random.randint(1,9)
print("Guess a number between 0 and 10 not including 0 or 10: ")
while chances <=5:
    guess=int(input("Enter Your Guessy Wessy: - "))
    if guess == n:
        print("You Win")
        break
    elif guess < n:
        print("go lower than ", guess)
    else:
        print("go higher than ", guess)
    chances=chances-1
    if chances==1:
        print("you are a loser. how can you not figure it out. The number is ", n," Have basic logic you little idiot")
