#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append("../..")
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
import game
import math

def evaluation(jeu):
    tot = 0
    score = game.getScores(jeu) 
    if jeu[1] == 1:
        tot = score[0] - score[1]
    else:
        tot = score[1] - score[0] 
    return tot

def Maxestimation(jeu,p):
    if p == 0 or game.finJeu(jeu):
        return evaluation(jeu)
    bestScore = -math.inf
    copie = game.getCopieJeu(jeu)        
    for coup in game.getCoupsValides(copie):
        game.joueCoup(copie,coup)
        game.changeJoueur(copie)
        test = game.getCopieJeu(copie)
        score = Minestimation(test,p-1)
        bestScore = max(bestScore,score)
    return bestScore

def Minestimation(jeu,p):
    if p == 0 or game.finJeu(jeu):
        return evaluation(jeu)
    bestScore = math.inf
    copie = game.getCopieJeu(jeu)        
    for coup in game.getCoupsValides(copie):
        game.joueCoup(copie,coup)
        game.changeJoueur(copie)
        test = game.getCopieJeu(copie)
        score = Maxestimation(test,p-1)
        bestScore = min(bestScore,score)
    return bestScore

def Minimaxdecision(jeu):
    p = 8
    bestScore = -math.inf
    bestCoup = None
    for coup in game.getCoupsValides(jeu):
        score = Maxestimation(jeu,p)
        if score > bestScore:
            bestScore = score
            bestCoup = coup
    return bestCoup
                
def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    coup = Minimaxdecision(jeu)
    return coup