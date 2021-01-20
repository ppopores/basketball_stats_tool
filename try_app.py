from functions import *




all_teams = [[], [], []]


def balance_teams(all_teams, experience):
    while True:
         num_teams = len(teams)
         for num in range(len(experience)):
             league_roster[num % num_teams].append(experience[num])
             continue
         for num in range(len(no_experience)):
             league_roster[num % num_teams].append(no_experience[num])
             continue
         break

clean_data(players)
sort_experience(players, experience, no_experience)

balance_teams(all_teams, experience)

print("=" * 30)
#print(league_roster[0])
player_roster = [player["name"] for player in league_roster[0]]
player_roster = str(player_roster)[1: -1]
player_roster = player_roster.replace("'", "")
print(player_roster)
team_guardians = [item['guardians'] for item in league_roster[0]]
print_guardians = str([item for x in team_guardians for item in x])[1: -1]
print_guardians = print_guardians.replace("'", "")
print(print_guardians)
#print(team_guardians)
#for items in team_guardians:
#    list2 = []
#    for item in items:
#        item = str(item)
#        list2.append(item)
#team_guardians = str(team_guardians)

#print(", ".join(team_guardians))
#guardians_d = str(guardians_d)
#print(guardians_d[1: -1])
avg_height = sum([sub["height"] for sub in league_roster[0]]) / len(league_roster[0])
print(str(avg_height))
experience = [sub["experience"] for sub in league_roster[0]]
experienced = [item for item in experience if item is True]
num_exp = len(experienced)
print(f"The {team_names[0]} have {team_size} players, of which {num_exp} have played before and {team_size - num_exp} have not.")
#print(len(league_roster[0]))
#print("=" * 30)
#print(league_roster[1])
#print("=" * 30)
#print(league_roster[2])
#show_data()