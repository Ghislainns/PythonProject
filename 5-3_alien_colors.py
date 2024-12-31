alien = {"green":10 , "yellow":5 ,"blue":3 ,"red":1}
total_points = 0
play = True

def kill_alien(alien):
        
    while True:

        alien_color = input("Type the color of the alien you want to kill (or q to quit): ")

        if alien_color == 'q':
            return 0

        for color, points in alien.items():
            if alien_color == color :
                print(f"You have just earned {points} new points.")
                return points

        print("This alien color are not valid...")

def play_again(total_points):

    while True:
        play_again = input("Would you like to play again(Y/N)?")
        if play_again == "Y":
            return True
        elif play_again == "N":
            print(f"Your final score are: {total_points} !")
            return False
        else:
            print("We did not understood your answer...")

while play:

    total_points += kill_alien(alien)
    play = play_again(total_points)



