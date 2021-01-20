from functions import *
if __name__ == "__main__":
#welcomes user to application
#asks user to choose a team to view
    #calls display function using input as value to display corresponding info inside try block
    print(("-" * 50) + "\n" + (" " * int((50 - len("Welcome to the Basketball Stats Tool")) / 2) + "Welcome to the Basketball Stats Tool\n" + ("-" * 50) + "\n" + ("-" * 50) + "\n"))
    league_intro = "Here are the teams for the " + year + " season:"
    print((" " * int((50 - len(league_intro)) / 2)) + league_intro + "\n")

    clean_data(players)
    sort_experience(players, experience, no_experience)

    balance_teams(league_roster, experience)
    show_data()
    while True:

        go_again = input("Would you like to view another team?   Y/N  ")
        if go_again.lower() == 'y':
            show_data()
        else:
            print("See ya!")
            break