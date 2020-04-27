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

def MaxAlphaBeta(jeu, alpha, beta,p):
    if p == 0 or game.finJeu(jeu):
        return evaluation(jeu)
    bestScore = -math.inf
    copie = game.getCopieJeu(jeu)
    for coup in game.getCoupsValides(copie):
        game.joueCoup(copie,coup)
        game.changeJoueur(copie)
        test = game.getCopieJeu(copie) 
        bestScore = max(bestScore, MinAlphaBeta(test,alpha,beta,p-1)) 
        alpha = max(alpha, bestScore)
        if beta <= alpha:
            break
    return bestScore


def MinAlphaBeta(jeu, alpha, beta,p):
    if p == 0 or game.finJeu(jeu):
        return evaluation(jeu)
    bestScore = math.inf
    copie = game.getCopieJeu(jeu)
    for coup in game.getCoupsValides(copie):
        game.joueCoup(copie,coup)
        game.changeJoueur(copie)
        test = game.getCopieJeu(copie)
        bestScore = min(bestScore, MaxAlphaBeta(test, alpha, beta,p-1)) 
        beta = min(beta, bestScore)
        if beta <= alpha:
            break
    return bestScore
    
def Alphabetadecision(jeu):
    p = 8
    alpha = -math.inf
    beta = math.inf
    bestScore = -math.inf
    bestCoup = None
    for coup in game.getCoupsValides(jeu):
        score = MaxAlphaBeta(jeu,alpha,beta,p)
        if score > bestScore:
            bestScore = score
            bestCoup = coup
    return bestCoup

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    coup = Alphabetadecision(jeu)
    return coup
