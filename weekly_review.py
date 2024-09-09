from award_player import AwardPlayer
from award_points import AwardPoints
from weekly_team import WeeklyTeam


class WeeklyReview:
    def __init__(self, league, week):
        self.year = league.year
        self.week = week
        self.league = league
        self.box_scores = league.box_scores(week)

        self.results = []

        self.highest_bench = None
        self.highest_score = None
        self.lowest_score = None
        self.largest_difference = None
        self.worst_luck = None
        self.best_luck = None

        self.bestQB = None
        self.bestWR = None
        self.bestRB = None
        self.bestTE = None
        self.bestKI = None
        self.bestDE = None

        self.worstQB = None
        self.worstWR = None
        self.worstRB = None
        self.worstTE = None
        self.worstKI = None
        self.worstDE = None

        self._get_data()

        for result in self.results:
            self._set_luck(result)

    def _get_data(self):
        for box_score in self.box_scores:
            self._get_score_data(box_score)
            for player in box_score.home_lineup:
                self._set_awards(box_score.home_team, player)
            for player in box_score.away_lineup:
                self._set_awards(box_score.away_team, player)

    def _set_awards(self, team_name, player):
        if player.slot_position == "QB":
            self._set_qb_award(team_name, player)

        if player.slot_position == "WR" or player.slot_position == "RB/WR/TE":
            self._set_wr_award(team_name, player)

        if player.slot_position == "RB" or player.slot_position == "RB/WR/TE":
            self._set_rb_award(team_name, player)

        if player.slot_position == "TE" or player.slot_position == "RB/WR/TE":
            self._set_te_award(team_name, player)

        if player.slot_position == "K":
            self._set_k_award(team_name, player)

        if player.slot_position == "D/ST":
            self._set_de_award(team_name, player)

        if player.slot_position == "BE":
            if player.position == "WR" or player.position == "RB" or player.position == "TE":
                self._set_bench_award(team_name, player)

    def _set_qb_award(self, team_name, player):
        if player.position != "QB":
            return None
        # Initialize the best and worst QB lists if they are empty
        if not self.bestQB:
            self.bestQB = AwardPlayer(team_name, player)
            self.worstQB = self.bestQB
            return

        # Update the best QB list if the current player has more points
        if player.points > self.bestQB.points:
            self.bestQB = AwardPlayer(team_name, player)

        # Update the worst QB list if the current player has fewer points
        if player.points < self.worstQB.points:
            self.worstQB = AwardPlayer(team_name, player)

    def _set_wr_award(self, team_name, player):
        if player.position != "WR":
            return None

        if not self.bestWR:
            self.bestWR = AwardPlayer(team_name, player)
            self.worstWR = self.bestWR
            return

        if player.points > self.bestWR.points:
            self.bestWR = AwardPlayer(team_name, player)

        if player.points < self.worstWR.points:
            self.worstWR = AwardPlayer(team_name, player)

    def _set_rb_award(self, team_name, player):
        if player.position != "RB":
            return None

        if not self.bestRB:
            self.bestRB = AwardPlayer(team_name, player)
            self.worstRB = self.bestRB
            return

        if player.points > self.bestRB.points:
            self.bestRB = AwardPlayer(team_name, player)

        if player.points < self.worstRB.points:
            self.worstRB = AwardPlayer(team_name, player)

    def _set_te_award(self, team_name, player):
        if player.position != "TE":
            return None

        if not self.bestTE:
            self.bestTE = AwardPlayer(team_name, player)
            self.worstTE = self.bestTE
            return

        if player.points > self.bestTE.points:
            self.bestTE = AwardPlayer(team_name, player)

        if player.points < self.worstTE.points:
            self.worstTE = AwardPlayer(team_name, player)

    def _set_k_award(self, team_name, player):
        if player.position != "K":
            return None

        if not self.bestKI:
            self.bestKI = AwardPlayer(team_name, player)
            self.worstKI = self.bestKI
            return

        if player.points > self.bestKI.points:
            self.bestKI = AwardPlayer(team_name, player)

        if player.points < self.worstKI.points:
            self.worstKI = AwardPlayer(team_name, player)

    def _set_de_award(self, team_name, player):
        if player.position != "D/ST":
            return None

        if not self.bestDE:
            self.bestDE = AwardPlayer(team_name, player)
            self.worstDE = self.bestDE
            return

        if player.points > self.bestDE.points:
            self.bestDE = AwardPlayer(team_name, player)

        if player.points < self.worstDE.points:
            self.worstDE = AwardPlayer(team_name, player)

    def _set_bench_award(self, team_name, player):
        if not self.highest_bench or player.points > self.highest_bench.points:
            self.highest_bench = AwardPlayer(team_name, player)

    def _get_score_data(self, box_score):
        if not self.highest_score or box_score.home_score > self.highest_score.points:
            self.highest_score = AwardPoints(box_score.home_team, box_score.home_score)
        if not self.lowest_score or box_score.home_score < self.lowest_score.points:
            self.lowest_score = AwardPoints(box_score.home_team, box_score.home_score)
        if not self.highest_score or box_score.away_score > self.highest_score.points:
            self.highest_score = AwardPoints(box_score.away_team, box_score.away_score)
        if not self.lowest_score or box_score.away_score < self.lowest_score.points:
            self.lowest_score = AwardPoints(box_score.away_team, box_score.away_score)

        home_win = round(box_score.home_score - box_score.away_score,2)

        if not self.largest_difference or abs(home_win) > self.largest_difference.points:
            if home_win > 0:
                self.largest_difference = AwardPoints(box_score.home_team, home_win)
            else:
                self.largest_difference = AwardPoints(box_score.home_team, -home_win)


        self.results.append([box_score.home_team, home_win > 0, box_score.home_score])
        self.results.append([box_score.away_team, not home_win > 0, box_score.away_score])

    def _set_luck(self, result):
        if result[1]:
            self._set_best_luck(result)
        else:
            self._set_worst_luck(result)

    def _set_worst_luck(self, result):
        total_wins = 0

        for opponent_result in self.results:
            if result[2] > opponent_result[2]:
                total_wins += 1

        if not self.worst_luck or total_wins > self.worst_luck.points:
            self.worst_luck = AwardPoints(result[0], total_wins)

    def _set_best_luck(self, result):
        total_losses = -1

        for opponent_result in self.results:
            if result[2] < opponent_result[2]:
                total_losses += 1

        if not self.best_luck or total_losses > self.best_luck.points:
            self.best_luck = AwardPoints(result[0], total_losses)
