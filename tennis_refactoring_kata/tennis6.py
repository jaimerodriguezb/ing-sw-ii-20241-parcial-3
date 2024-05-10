# -*- coding: utf-8 -*---

class TennisGame6:
    def __init__(self, player_1_name, player_2_name):
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.player_1_score = 0
        self.player_2_score = 0

    def won_point(self, player_name):
        if (player_name == "player1"):
            self.player_1_score += 1
        else:
            self.player_2_score += 1

    def score(self):
        result: str

        if (self.player_1_score == self.player_2_score):
           result=self.calculate_tie_score()
        elif (self.player_1_score >= 4 or self.player_2_score >= 4):
            result=self.calculate_final_score()
        else:
            result=self.calculate_regular_score()

        return result
    
    def calculate_tie_score(self):
     # tie score
        tie_score: str
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

    def calculate_final_score(self):
        # end-game score
        end_game_score: str

        if (self.player_1_score - self.player_2_score == 1):
            end_game_score = "Advantage " + self.player_1_name
        elif (self.player_1_score - self.player_2_score == -1):
            end_game_score = "Advantage " + self.player_2_name
        elif (self.player_1_score - self.player_2_score >= 2):
            end_game_score = "Win for " + self.player_1_name
        else:
            end_game_score = "Win for " + self.player_2_name

        return end_game_score
    
    def calculate_regular_score(self):
        # regular score
            score1=self.match_score(self.player_1_score)
            score2=self.match_score(self.player_2_score)
            return score1 + "-" + score2
    
    def match_score (self,player_score):
            score=""
            match (player_score):
                    case 0:
                        score = "Love"
                    case 1:
                        score = "Fifteen"
                    case 2:
                        score = "Thirty"
                    case _:
                        score = "Forty"

            return score