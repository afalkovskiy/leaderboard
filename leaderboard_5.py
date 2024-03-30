class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display_details(self):
        print("Name:", self.name, "\tScore:", self.score)

def add_player(leaderboard):
     print("Function add_player called")
     input("Press any key ")  
     name = input("Player name:")   
     score = input("Player score:")  
     player = Player(name, score)
     player.display_details()

     leaderboard.append(player)

     print(leaderboard)



def main():

    player1 = Player('Max', 101)
    player2 = Player('Bob', 120)
    player1.display_details()
    player2.display_details()

    leaderboard = []
    choice = ''
    while choice != '5':
        print("\nLeaderboard 4 test\nMenu:")
        print("1. Add Player")
        print("2. Display Leaderboard")
        print("3. Display Highest Score")
        print("4. Save Leaderboard to File")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Add player
            add_player(leaderboard)                
        elif choice == '2':
            # Display Leaderboard
            print("Selected 2")
            choice = input("Press any key ")
        elif choice == '3':
           # Display Highest Score
           print("Selected 3")
           choice = input("Press any key ")
        elif choice == '4':
           # Save Leaderboard to File
           print("Selected 4")
           choice = input("Press any key ")
        elif choice == '5':
            print("Exiting...")
        else:
            print("Invalid choice. Please enter again.")
       
    


if __name__ == "__main__":
    main()
