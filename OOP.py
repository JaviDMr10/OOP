from player import Player
from NFLteam import NFLteam

def main():
    player1 = Player("Joe Montana", "QB")
    player2 = Player("Barry Sanders", "RB")
    player3 = Player("Jerry Rice", "WR")
    player4 = Player("Graham Gano", "K")

    player_list = [player1, player2, player3, player4]

    team = NFLteam("Ravenclaw Eagles")
    for individual in player_list:
        team.add_player(individual)
    print(f"Team Name: {team.team_name}")
    print(f"Players:")
    for individual in team.players:
        print(f"{individual.player_name} - {individual.player_position}")


main()




