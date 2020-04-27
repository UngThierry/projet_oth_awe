#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import os
import sys
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
    maxPoints = -math.inf
    bestCoup = None
    for coup in game.getCoupsValides(jeu):       
        copie = game.getCopieJeu(jeu)
        game.joueCoup(copie,coup)
        game.changeJoueur(copie)
        points = evaluation(copie)
        if points > maxPoints:
            maxPoints = points
            bestCoup = coup
    return bestCoup

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    coup = horizon1decision(jeu)
    return coup
