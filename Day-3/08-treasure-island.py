print('''                                         .       .
                                                    .     .
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    .     .
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            ssssssss.
                      sssssssSSSSssssssssss.
                 sssssSSSSSSSSSSSSSSSssssssssssss.             
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
''')
print("\n")

print("Welcome to the treasure island.")
print("Your misson is to find the treasure.\n")

print("You are at a cross road. Where do you want to go?")
ch1 = input("Type \"left\" or \"right\" : ")
ch1 = ch1.lower()
if(ch1 == "left"):
    print("\nYou come to a lake. There is an island in the middle of the lake.")
    ch2 = input(
        "Type \"wait\" to wait for a boat.Type \"swim\" to swim across : ")
    ch2 = ch2.lower()
    if(ch2 == "wait"):
        print("\nYou arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue.")
        ch3 = input("Which one do you choose? : ")
        ch3 = ch3.lower()
        if(ch3 == "blue"):
            print("\nYou enter a room of beasts, Wrong Choice. Game Over!")
        elif(ch3 == "red"):
            print("\nYou enter a room of flames, Wrong Choice. Game Over!")
        elif(ch3 == "yellow"):
            print("\nCongratulations, You win!!")
        else:
            print("\nSorry, Wrong Choice. Game Over!")
    else:
        print("\nSorry, Wrong Choice. Game Over!")
else:
    print("\nSorry, Wrong Choice. Game Over!")
