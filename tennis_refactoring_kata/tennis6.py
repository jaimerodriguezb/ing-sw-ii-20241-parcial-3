# -*- coding: utf-8 -*-

class TennisGame6:
    def __init__(self, player_1_name, player_2_name):
        self.player_1_n = player_1_name
        self.player_2_n = player_2_name
        self.player_1_score = 0
        self.player_2_score = 0

    def won_point(self, player_name):
        if (player_name == "player1"):
            self.player_1_score += 1
        else:
            self.player_2_score += 1
    
    def score(self):
        result = ""    
        if self.player_1_score == self.player_2_score:
            result = self.get_tie_score()
        elif self.player_1_score >= 4 or self.player_2_score >= 4:
            result = self.get_end_game_score()
        else:
            result = self.get_regular_score()

        return result

    def get_tie_score(self):
        tie_score = ""
        match self.player_1_score:
            case 0:
                tie_score = "Love-All"
            case 1:
                tie_score = "Fifteen-All"
            case 2:
                tie_score = "Thirty-All"
            case _:
                tie_score = "Deuce"
        return tie_score

    def get_end_game_score(self):
        end_game_score = ""
        if self.player_1_score - self.player_2_score == 1:
            end_game_score = "Advantage " + self.player_1_n
        elif self.player_1_score - self.player_2_score == -1:
            end_game_score = "Advantage " + self.player_2_n
        elif self.player_1_score - self.player_2_score >= 2:
            end_game_score = "Win for " + self.player_1_n
        else:
            end_game_score = "Win for " + self.player_2_n
        return end_game_score

    def get_regular_score(self):
        scores = ["Love", "Fifteen", "Thirty", "Forty"]
        score1 = scores[self.player_1_score] if self.player_1_score < 4 else "Forty"
        score2 = scores[self.player_2_score] if self.player_2_score < 4 else "Forty"
        return f"{score1}-{score2}"