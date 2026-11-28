print('''
  @@@@@                                        @@@@@
 @@@@@@@                                      @@@@@@@
 @@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@
  @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@
      @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@
        @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@
          @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@
             @@@@@@@    @@@@@@    @@@@@@
             @@@@@@      @@@@      @@@@@
             @@@@@@      @@@@      @@@@@
              @@@@@@    @@@@@@    @@@@@
               @@@@@@@@@@@  @@@@@@@@@@
                @@@@@@@@@@  @@@@@@@@@
            @@   @@@@@@@@@@@@@@@@@   @@
            @@@@  @@@@ @ @ @ @ @@@@  @@@@
           @@@@@   @@@ @ @ @ @ @@@   @@@@@
         @@@@@      @@@@@@@@@@@@@      @@@@@
       @@@@          @@@@@@@@@@@          @@@@
    @@@@@              @@@@@@@              @@@@@
   @@@@@@@                                 @@@@@@@
    @@@@@                                   @@@@@
''')

print("\n--- Welcome to my island ---")
print("There are two doors in front of you. 🚪 A red door and 🚪 A blue door")

choice_1 = input("Which door do you want to open? ").lower()

if choice_1 == "red":
    print("Great! Now you entered a room.")
    print("You found three boxes: 🎁 A white, 🎁 A black, 🎁 A green")
    choice_2 = input("Which box do you want to open? ").lower()
    
    if choice_2 == "white":
        print("Oops! You opened 🎁 a box filled with 🐍 snakes!")
        print("💀 Game over!")
    elif choice_2 == "black":
        print("Oops! You opened 🎁 a box filled with 🕷️ spiders!")
        print("💀 Game over!")
    elif choice_2 == "green":
        print("🎉 Congratulations! You found the treasure 💰💰💰")
    else:
        print("❌ Invalid choice! 🤷‍♂️")
        
elif choice_1 == "blue":
    print("Oops! You chose the crocodile door 🐊.")
    print("💀 Game over!")
else:
    print("❌ Invalid choice! 🤷‍♂️")
