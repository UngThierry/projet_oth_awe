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

def negamaxAB(jeu,alpha,beta,color,p):
    if p == 0 or game.finJeu(jeu):
        return color*evaluation(jeu)
    bestScore = -math.inf
    copie = game.getCopieJeu(jeu)
    for coup in game.getCoupsValides(copie):
        game.joueCoup(copie,coup)
        game.changeJoueur(copie)
        test = game.getCopieJeu(copie)
        bestScore = max(bestScore,-negamaxAB(test,-beta,-alpha,-color,p-1))
        alpha = max(alpha,bestScore)
        if(alpha >= beta):
            break
    return bestScore

def negamaxABdecision(jeu):
    p = 6
    bestScore = -math.inf
    alpha = -math.inf
    beta = math.inf
    bestCoup = None
    for coup in game.getCoupsValides(jeu):
        score = negamaxAB(jeu,alpha,beta,1,p)
        if game.coupValide(jeu,coup):
            if score > bestScore:
                bestScore = score
                bestCoup = coup
    return bestCoup

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    coup = negamaxABdecision(jeu)
    return coup
