import random

def numberguess(low, high, attempts):
    guess_number = 0
    exact_number = random.randint(low,high)
    while True:
        try:
            number = int(input(f"Guess the number from {low}-{high} : "))
            guess_number += 1

            if number > exact_number:
                print("Too high")
            elif number < exact_number:
                print("Too low")
            else:
                if guess_number <= attempts:
                    print(f"You guess it at {guess_number} tries. You are lucky!")
                    break
                else:
                    print(f"You guess it at {guess_number} times. You are unlucky.")
                    break
        except ValueError:
            print("Invalid Input!")

guess = 0
while True:
    print("\nChoose Difficulty")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")
    print("4. Exit")

    choice = input("Choose an option (enter the number): ")

    if choice == "1":
       numberguess(1,10,4)
    elif choice == "2":
       numberguess(1,50,6)
    elif choice == "3":
        numberguess(1,100,7)
    elif choice == "4":
        print("Goodbye.")
        break
    else:
        print("Invalid Input! Try again")

