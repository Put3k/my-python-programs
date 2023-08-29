def get_number_of_teams():
    
    while True:
        result = input("Enter the number of teams in the tournament: ")
        if result.isdigit() and int(result) >= 2:
            return int(result)
        print("The minimum number of teams is 2, try again.")


def get_team_names(num_teams):

    team_list = []

    for i in range(num_teams):
        while True:
            name = input(f"Enter the name for team #{i+1}: ")

            if len(name) < 2:
                print("Team names must have at least 2 characters, try again.")
                continue
            elif len(name.split()) > 2:
                print("Team names may have at most 2 words, try again.")
                continue
            team_list.append(name)
            break

    return team_list


def get_number_of_games_played(num_teams):
    
    while True:
        result = int(input("Enter the number of games played by each team: "))

        if result < num_teams-1:
            print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
        else:
            break
    
    return result


def get_team_wins(team_names, games_played):
    
    team_stats = []
    for i, j in enumerate(team_names):
        team_stats.append({"name":j, "wins":0})
        while True:
            wins = int(input(f"Enter the number of wins Team {j} had: "))
            if wins > games_played:
                print(f"The maximum number of wins is {games_played}, try again.")
                continue
            elif wins < 0:
                print("The minimum number of wins is 0, try again.")
                continue
            team_stats[i]['wins'] = wins
            break
            

    return team_stats


def team_generator(team_wins):
    new_lst = sorted(team_wins, key=lambda d: d['wins'])
    
    for i in range(len(new_lst)//2):
        print(f"Home: {new_lst[i]['name']} VS Away: {new_lst[-1-i]['name']}")

num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)

print("Generating the games to be played in the first round of the tournament...")

team_generator(team_wins)
print("/nEnd")

#Change due to git tutorial.
