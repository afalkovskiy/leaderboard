class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display_details(self):
        print("Name:", self.name, "\tScore:", self.score)


def compare_players(a, b):
    return a.score > b.score


def add_player(leaderboard):
    name = input("Enter player name: ")
    score = int(input("Enter score: "))

    new_player = Player(name, score)
    leaderboard.append(new_player)

    leaderboard.sort(key=lambda x: x.score, reverse=True)


def display_leaderboard(leaderboard):
    print("Leaderboard:")
    for player in leaderboard:
        player.display_details()


def highest_score(leaderboard):
    if leaderboard:
        print("Highest Score:")
        leaderboard[0].display_details()
    else:
        print("No players in the leaderboard.")


def save_leaderboard_to_file(leaderboard, filename):
    with open(filename, 'w') as outFile:
        for player in leaderboard:
            outFile.write(player.name + " " + str(player.score) + "\n")
    print("Leaderboard saved to file.")


def cleanup_memory(leaderboard):
    del leaderboard[:]


def main():
    leaderboard = []
    try:
        with open("leaderboard.txt") as inFile:
            for line in inFile:
                name, score = line.split()
                score = int(score)
                loaded_player = Player(name, score)
                leaderboard.append(loaded_player)
    except FileNotFoundError:
        pass

    choice = ''
    while choice != '5':
        print("\nMenu:")
        print("1. Add Player")
        print("2. Display Leaderboard")
        print("3. Display Highest Score")
        print("4. Save Leaderboard to File")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_player(leaderboard)
        elif choice == '2':
            display_leaderboard(leaderboard)
        elif choice == '3':
            highest_score(leaderboard)
        elif choice == '4':
            save_leaderboard_to_file(leaderboard, "leaderboard.txt")
        elif choice == '5':
            print("Exiting...")
        else:
            print("Invalid choice. Please enter again.")

    cleanup_memory(leaderboard)


if __name__ == "__main__":
    main()
