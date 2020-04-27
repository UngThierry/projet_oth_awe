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

def horizon1decision(jeu):
    bestScore = -math.inf
    bestCoup = None
    for coup in game.getCoupsValides(jeu):       
        copie = game.getCopieJeu(jeu)
        game.joueCoup(copie,coup)
        score = evaluation(copie)
        game.changeJoueur(copie)
        if score > bestScore:
            bestScore = score
            bestCoup = coup
    return bestCoup

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    coup = horizon1decision(jeu)
    return coup
