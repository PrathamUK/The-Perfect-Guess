import random
n = random.randint(1,50)
guesses = 0
a = -1
while(a!= n):
    a = int(input("Enter a number between 1 and 50: "))
    guesses += 1
    if(a < n):
        print("Too low!")
    elif(a > n):
        print("Too high!")

print(f"Congratulations! You've guessed the number {n} in {guesses} tries.")
if a == n:
    print("You guessed it right!")
else:
    print("Better luck next time!")
print("Game Over!")
print("Thank you for playing!")

