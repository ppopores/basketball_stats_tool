from constants import TEAMS, PLAYERS
import copy
from datetime import datetime


teams = copy.deepcopy(TEAMS)
players = copy.deepcopy(PLAYERS)

team_size = len(players)/len(teams)
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

def sort_data(*args):
    sort_experience(players, experience, no_experience)
    #idx = 0
    while len(experience) > 0:

        for player in experience:
            #idx = 1

            if len(league_roster[0]) == 0 or len(league_roster[0]) < 3:
                league_roster[0].append(player["name"])
                guardians[0].append(player["guardians"])
                average_heights[0].append(player["height"])
                team_experience[0][0].append(1)
                #idx += 1
                continue
            elif len(league_roster[1]) < 3:
                league_roster[1].append(player["name"])
                guardians[1].append(player["guardians"])
                average_heights[1].append(player["height"])
                team_experience[1][0].append(1)
                #idx += 1
                continue
            elif len(league_roster[2]) < 3:
                league_roster[2].append(player["name"])
                guardians[2].append(player["guardians"])
                average_heights[2].append(player["height"])
                team_experience[2][0].append(1)

        for player in no_experience:


            if len(league_roster[0]) == 0 or len(league_roster[0]) < 6:
                league_roster[0].append(player["name"])
                guardians[0].append(player["guardians"])
                average_heights[0].append(player["height"])
                team_experience[0][1].append(1)
                #idx += 1
                continue
            elif len(league_roster[1]) < 6:
                league_roster[1].append(player["name"])
                guardians[1].append(player["guardians"])
                average_heights[1].append(player["height"])
                team_experience[1][1].append(1)
                #idx += 1
                continue
            elif len(league_roster[2]) < 6:
                league_roster[2].append(player["name"])
                guardians[2].append(player["guardians"])
                average_heights[2].append(player["height"])
                team_experience[2][1].append(1)
        break
    return league_roster, guardians, average_heights, team_experience



def show_data(*args):
    while True:
        try:
            for team in teams_in_league:
               print(" " * 15 + (str(team))[1: -1])

            print("\nPlease select the team that you would like to view,")
            user_input = input("select the corresponding digit (ie 1, 2, 3...)")
            user_input = int(user_input)
            if user_input > 0 and user_input < len(teams):
                user_input -= 1

                print("\n" + (" " * 10) + "Presenting the " + year +  " {}.\n".format(team_names[user_input]))
                print((" " * int((50 - len("Players:")) / 2)) + "Players:")
                for item in league_roster[user_input]:
                    print(" " * int((50 - len(str(item))) / 2) + str(item))
                print("\n" + " " * int((50 - len("Guardians:")) / 2) + "Guardians:")
                for items in guardians[user_input]:
                    for item in items:
                        print(" " * int((50 - len(str(item))) / 2) + str(item))

                vet = sum(team_experience[user_input][0])
                newb = sum(team_experience[user_input][1])
                team_tots = vet + newb
                print("\nThe {} have {} players, of which {} have played before and {} have not.".format(team_names[user_input], team_tots, vet, newb))
                team_avg_height = float((sum(average_heights[user_input])) / len(average_heights[user_input]))
                print("\nThe average height of the {} is ".format(team_names[user_input]) + str(team_avg_height) + " inches.\n")
        except ValueError:
            print("SO SORRY!!! PLEASE ENTER A VALID INTEGER FOR YOUR TEAM!")
            continue


if __name__ == "__main__":
    clean_data()
    sort_experience()
    sort_data()
    show_data()
