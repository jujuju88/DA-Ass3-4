"""
Remember Adventure? Well, we’re going to build a more basic version of that. A complete text
game, the program will let users move through rooms based on user input and get descriptions
of each room. To create this, you’ll need to establish the direction in which the user can move, a
way to track how far the user has moved (and therefore which room he/she is in), and to print
out a description. You’ll also need to set limits for how far the user can move. In other words,
create “walls” around the rooms that tell the user, “You can’t move further in this direction.”
Concepts to keep in mind:
"""

House=("Kitchen","Living Room","bedroom","Dining Room")
position = 0

print(f"Welcome to our adventure game. We are in a house with 4 rooms. Horizontally aligned. \n You are now in the {House[position]}")
while position > -1:
    move = input("Do you wanna move (y/n) or exit(exit) ")
    ## check if user want to move
    if move == "y":
        print(f"You are currently in the {House[position]}")
        
        if position == 0:
            ## if the use is the initial position 0, which can only be moved forward
            print("You can only go forward")
            steps = int(input("How many steps would you wanna move?(a number): "))
            if steps > 0 and steps < (5 - position):
                ## check if the steps wanted to move is in the limit
                position += steps
                print(f"You took {steps} steps, you are now in {House[position]} \n")
            elif steps == 0:
                print(f"You have not moved, You are still in the {House[position]} \n")
            else:
                print(f"You can’t move {steps} steps in this direction, you would hit the wall")
                print(f"You are currently in {House[position]} \n")
        

        else:
            direction = input("which way would you wanna go? (f for forward/ b for backward): ")
            if direction == "f":
                ## if the user wanna move forward
                steps = int(input("How many steps would you wanna move?(a number): "))
                if steps > 0 and steps < (5 - position):
                    position += steps
                    print(f"You took {steps} steps, you are now in {House[position]} \n")
                elif steps == 0:
                    print(f"You have not moved, You are still in the {House[position]} \n")
                else:
                    print(f"You can’t move {steps} steps in this direction, you would hit the wall")
                    print(f"You are currently in {House[position]} \n")
            
            elif direction == "b":
                ## if the user wanna move backward
                steps = int(input("How many steps would you wanna move?(a number): "))
                if steps > 0 and steps < (5 - position):
                    if (position - steps) < 0:
                        ## Check if users can move that many steps
                        print(f"You cant move that many steps, you would go over the wall")
                    else:
                        position -= steps
                        print(f"You took {steps} steps, you are now in {House[position]} \n")
                
                elif steps == 0:
                    print(f"You have not moved, You are still in the {House[position]} \n")
                else:
                    print(f"You can’t move {steps} steps in this direction, you would hit the wall")
                    print(f"You are currently in {House[position]} \n")
            
            
            else:
                ## Error message if user inputed words other than forward/backward
                print ("please input only forward or backward \n")

    elif move == "n":
        ## if user chose to not move
        print(f"You have not moved, You are still in the {House[position]} \n")
    elif move == "exit":
        print("You have now left the house, Goodbye")
        break
    
    
    else:
        print(f"Please input either y or n")
