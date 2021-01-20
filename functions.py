from constants import TEAMS, PLAYERS
import copy
from datetime import datetime


teams = copy.deepcopy(TEAMS)
players = copy.deepcopy(PLAYERS)

team_size = len(players)/len(teams)
team_size = int(team_size)
experience = []
no_experience = []
league_roster = [[] for item in teams]
guardians = [[] for item in teams]
teams_in_league = list(enumerate(teams, 1))
team_names = [item for item in teams]
average_heights = [[] for item in teams]
team_experience = [[[],[]] for item in teams]
this_year = datetime.now()
year = this_year.strftime("%Y")

def clean_data(players):
    for player in players:
        player["height"] = int(player["height"][:2])
        player["guardians"] = player["guardians"].split(" and ")
        if player.get("experience") == "NO":
            player["experience"] = False
        elif player.get("experience") == "YES":
            player["experience"] = True


def sort_experience(players, experience, no_experience):
	for player in players:
		if player.get("experience") == True:
			experience.append(player)
		else:
			no_experience.append(player)
	return experience, no_experience

def balance_teams(*args):
    while True:
         num_teams = len(teams)
         for num in range(len(experience)):
             league_roster[num % num_teams].append(experience[num])
             continue
         for num in range(len(no_experience)):
             league_roster[num % num_teams].append(no_experience[num])
             continue
         break

def show_data(*args):
    while True:
        try:
            for team in teams_in_league:
               print(" " * 15 + (str(team))[1: -1])

            print("\nPlease select the team that you would like to view,")
            user_input = input("select the corresponding digit (ie 1, 2, 3...)\n")
            user_input = int(user_input)
            if user_input > 0 and user_input <= len(teams):
                user_input -= 1

                print("\n" + (" " * 10) + "Presenting the " + year +  " {}.\n".format(team_names[user_input]))
                print((" " * int((50 - len("Players:")) / 2)) + "Players:\n".upper())
                player_roster = [player["name"] for player in league_roster[user_input]]
                player_roster = str(player_roster)[1: -1]
                player_roster = player_roster.replace("'", "")
                print(player_roster)
                print("\n" + " " * int((50 - len("Guardians:")) / 2) + "Guardians:\n".upper())
                team_guardians = [item['guardians'] for item in league_roster[user_input]]
                print_guardians = str([item for x in team_guardians for item in x])[1: -1]
                print_guardians = print_guardians.replace("'", "")
                print(print_guardians)
                avg_height = sum([sub["height"] for sub in league_roster[user_input]]) / len(league_roster[user_input])
                avg_height = round(avg_height, 2)
                experience = [sub["experience"] for sub in league_roster[user_input]]
                experienced = [item for item in experience if item is True]
                num_exp = len(experienced)
                print(f"\nThe {team_names[user_input]} have {team_size} players, of which {num_exp} have played before and {team_size - num_exp} have not.".upper())

                print(f"\nThe average height of the {team_names[user_input]} is {str(avg_height)} inches.\n".upper())
        except ValueError:
            print("\nSO SORRY!!! PLEASE ENTER A VALID INTEGER FOR YOUR TEAM!\n\n")
            continue
        break

if __name__ == "__main__":
    balance_teams()
    clean_data()
    sort_experience()
    sort_data()
    show_data()
