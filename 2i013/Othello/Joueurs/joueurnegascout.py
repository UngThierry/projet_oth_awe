#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append("../..")
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
import game
import math

def evaluation(jeu):
    res = 0
    score = game.getScores(jeu) 
    if jeu[1] == 1:
        res = score[0] - score[1]
    else:
        res = score[1] - score[0]
    for coup in game.getCoupsValides(jeu):
        if game.coupValide(jeu,coup):
            if (coup[0] == 0 or coup[0] == 7) and (coup[1] == 0 or coup[1] == 7):
                res += 4
            elif (coup[0] == 0 or coup[0] == 7) or (coup[1] == 0 or coup[1] == 7):
                res += 2
            else:
                res += 1
    return res

def negascout(jeu,alpha,beta,color,p):
    if p == 0 or game.finJeu(jeu):
        return color*evaluation(jeu)
    firstChild = True
    copie = game.getCopieJeu(jeu)        
    for coup in game.getCoupsValides(copie):
        game.joueCoup(copie,coup)
        game.changeJoueur(copie)
        test = game.getCopieJeu(copie)
        if firstChild:
            firstChild = False
            score = -negascout(test,-beta,-alpha,-color,p-1)
        else:
            score = -negascout(test,-alpha-1,-alpha,-color,p-1)
            if (alpha < score and score < beta):
                score = -negascout(test,-beta,-score,-color,p-1)
        alpha = max(alpha,score)
        if (alpha >= beta):
            break
    return alpha

def negascoutdecision(jeu):
    p = 8
    bestScore = -math.inf
    alpha = -math.inf
    beta = math.inf
    bestCoup = None
    for coup in game.getCoupsValides(jeu):
        score = negascout(jeu,p, alpha, beta,1)
        if score > bestScore:
            bestScore = score
            bestCoup = coup
    return bestCoup

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    coup = negascoutdecision(jeu)
    return coup
