class AwardPlayer:
    def __init__(self,team,player):
        self.team = team
        self.team_name = team.team_name
        self.player = player
        self.points = player.points

    def __str__(self):
        return f"{self.team_name}, {self.player.name}, {self.points}"
