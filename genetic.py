"""bit-bang a picture until you guess it(veery slow)"""
import os
import pygame
import random
from pygame import gfxdraw
from random import randint
from sys import argv


size = (400, 400)
screen = pygame.display.set_mode(size)
grass = pygame.image.load("textures/grass2.png")

guesser = lambda: int(random.random()*255)

def guess(x, y):
    entry = guesses["{}x{}".format(x, y)]
    while True:
        g = guesser(), guesser(), guesser()
        if g in entry["E"]:
            pass
        else:        
            entry["E"].append(g)
            break
    return g

def verify(guess, pic, x, y):
    actual = pic.get_at((x, y))
    first = actual[0] == guess[0]
    second = actual[1] == guess[1]
    third = actual[2] == guess[2]
    return first and second and third

def guess_all(w, h):
    for i in xrange(w):
        for k in xrange(h):
            if guesses["{}x{}".format(i, k)]["g"]:
                continue
            col = guess(i, k)
            screen.set_at((i,k), col)
            if verify(col, grass, i, k):
                guesses["{}x{}".format(i, k)]["g"] = True

pic_size = grass.get_size()

guesses = {}
for x in xrange(pic_size[0]):
    for y in xrange(pic_size[1]):
        guesses["{}x{}".format(x, y)] = {"g": False, "E": []} 

clock = pygame.time.Clock()
while(True):
    # clock.tick(60)
    guess_all(*pic_size)
    pygame.display.flip()
