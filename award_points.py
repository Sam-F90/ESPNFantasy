class AwardPoints:
    def __init__(self, team, points):
        self.team = team
        self.team_name = team.team_name
        self.points = points

    def __str__(self):
        return f"{self.team_name}, {self.points}"
