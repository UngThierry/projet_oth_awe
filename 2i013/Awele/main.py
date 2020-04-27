#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import awele
sys.path.append("../..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
import joueur_aleatoire
import joueur_premier_coup_valide
import joueurminimax
import joueuralphabeta
import joueurnegascout
import joueurnegamax
import joueur_horizon1
game.joueur1=joueurnegascout
game.joueur2=joueur_horizon1
j1=0
j2=0
n1=0
n=5
for i in range(n):
    jeu=game.initialiseJeu()
    it=0
    jeu[3] = []
    jeu[3].append((None,None))
    game.affiche(jeu)
    while(it < 100) and (not game.finJeu(jeu)):
        jeu[2]=game.getCoupsValides(jeu)
        if jeu[1] == 1:
            coup = game.joueur1.saisieCoup(jeu)
            while(game.coupValide(jeu,coup) == False):
                print("\nVeuillez resaissir une autre case valide : ")
                coup = game.joueur1.saisieCoup(jeu)
        else:
            coup = game.joueur2.saisieCoup(jeu)
            while(game.coupValide(jeu,coup) == False):
                print("\nVeuillez resaissir une autre case valide : ")
                coup = game.joueur2.saisieCoup(jeu)
        game.joueCoup(jeu,coup)
        game.affiche(jeu)
        if game.finJeu(jeu) == True:
            break 
        it+=1
    print("Gagnant: "+str(game.getGagnant(jeu))+"\n")
    if(game.getGagnant(jeu)==1):
        j1+=1
    elif((game.getGagnant(jeu)==2)):
        j2+=1
    else:
        n1+=1

j1= (j1/n)  
j2= (j2/n) 
n1= (n1/n) 
print("Le joueur 1 a gagné : "+str(j1)+"% fois, le joueur 2 a gagné : "+str(j2)+"% fois et il y a eu : "+str(n1)+"% de matchs nuls")
