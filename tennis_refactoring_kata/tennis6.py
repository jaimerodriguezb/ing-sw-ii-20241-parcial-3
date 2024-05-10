# -*- coding: utf-8 -*-

class TennisGame6:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def compute_tie_score(self):
        match self.player1_score:
            case 0:
                return "Love-All"
            case 1:
                return "Fifteen-All"
            case 2:
                return "Thirty-All"
            case _:
                return "Deuce"
    
    def compute_end_game_score(self):
        if (self.player1_score - self.player2_score == 1):
            return "Advantage " + self.player1_name
        elif (self.player1_score - self.player2_score == -1):
            return "Advantage " + self.player2_name
        elif (self.player1_score - self.player2_score >= 2):
            return "Win for " + self.player1_name
        else:
            return "Win for " + self.player2_name
    def number_to_words(self, score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        else:
            return "Forty"

    def compute_regular_score(self):
        score1 = self.number_to_words(self.player1_score)
        score2 = self.number_to_words(self.player2_score)
        regular_score = score1 + "-" + score2
        return regular_score

    def won_point(self, player_name):
        if (player_name == "player1"):
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score(self):
        result: str
        if (self.player1_score == self.player2_score):
            # tie score
            result = self.compute_tie_score()
        elif (self.player1_score >= 4 or self.player2_score >= 4):
            # end-game score
            result = self.compute_end_game_score()
        else:
            # regular score
            result = self.compute_regular_score()
        return result
