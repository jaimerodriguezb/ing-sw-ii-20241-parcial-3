# -*- coding: utf-8 -*-

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
            result = self.puntuacion_empate()

        elif (self.player_1_score >= 4 or self.player_2_score >= 4):      #40 - 40 
            # end-game score
           result=self.fin_juego_score()

        else:
            # regular score
            result=self.puntaje_regular()

        return result

    def puntuacion_empate(self):
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
    
    def fin_juego_score(self):
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

    def puntaje_regular(self):
            
        puntuacion1=self.cantidad_puntos(self.player_1_score )
        puntuacion2=self.cantidad_puntos(self.player_2_score )
             
        return  puntuacion1 + "-" + puntuacion2  

    def cantidad_puntos(self, puntaje):
        
        match (puntaje): 
    
            case 0:   
                puntaje = "Love" 
            case 1:
                puntaje= "Fifteen"
            case 2:
                puntaje= "Thirty"
            case _:
                puntaje= "Forty"

        return puntaje
