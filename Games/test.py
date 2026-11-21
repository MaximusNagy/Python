def game():
    print("\n--- Welcome to my game ---")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

game()
name_1 = input("Please player one enter your name: ")
name_2 = input("Please player two enter your name: ")   

try:
    while True:
        game()

        player_1 = int(input(f"Please {name_1} enter your play: "))
        player_2 = int(input(f"Please {name_2} enter your play: "))

        if player_1 == 4 and player_2 == 4:
            print("Exiting the game...")
            break
        elif player_1 == 1 and player_2 == 2:
            print(f"{name_2} wins!")
        elif player_1 == 1 and player_2 == 3:
            print(f"{name_1} wins!")
        elif player_1 == 2 and player_2 == 1:
            print(f"{name_1} wins!")
        elif player_1 == 2 and player_2 == 3:
            print(f"{name_2} wins!")
        elif player_1 == 3 and player_2 == 1:
            print(f"{name_2} wins!")
        elif player_1 == 3 and player_2 == 2:
            print(f"{name_1} wins!")
        elif player_1 == player_2:
            print("It's a tie!")
        else:
            print("Invalid input! Please choose between (1, 2, 3, 4).")

except ValueError:
    print("Please choose a valid number (1, 2, 3, 4).")
