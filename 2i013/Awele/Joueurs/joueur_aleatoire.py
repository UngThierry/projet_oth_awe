#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append("../..")
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
import game
import random

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    jeu[2] = game.getCoupsValides(jeu)
    return random.choice(jeu[2])