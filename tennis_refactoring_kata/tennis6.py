# -*- coding: utf-8 -*-

class TennisGame6:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if (player_name == "player1"):
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score(self):
        result: str

        if (self.player1_score == self.player2_score):
            result = self.tie_score_function()

        elif (self.player1_score >= 4 or self.player2_score >= 4):
            result = self.end_game_score_function()

        else:
            result = self.regular_score_function()

        return result

    def tie_score_function(self):
        tie_score: str 
        match self.player1_score:
            case 0:
                tie_score = "Love-All"
            case 1:
                tie_score = "Fifteen-All"
            case 2:
                tie_score = "Thirty-All"
            case _:
                tie_score = "Deuce"  

        return tie_score

    def end_game_score_function(self):
        # end-game score
        end_game_score: str

        if (self.player1_score - self.player2_score == 1):
            end_game_score = "Advantage " + self.player1_name
        elif (self.player1_score - self.player2_score == -1):
            end_game_score = "Advantage " + self.player2_name
        elif (self.player1_score - self.player2_score >= 2):
            end_game_score = "Win for " + self.player1_name
        else:
            end_game_score = "Win for " + self.player2_name

        return end_game_score
                
    def regular_score_function(self):

        score1 = self.score_name(self.player1_score)
        score2 = self.score_name(self.player2_score)

        return score1 + "-" + score2
    
    def score_name(self, score):
        match (score):
            case 0:
                score = "Love"
            case 1:
                score = "Fifteen"
            case 2:
                score = "Thirty"
            case _:
                score = "Forty"

        return score
    