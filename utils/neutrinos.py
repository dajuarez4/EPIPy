import pygame
import random
from utils.config import r,vx
class Neutrino:
    def __init__(self):
        self.x = 0 #left side generator
        self.y = random.randint(100, 600) # randomly
        self.radius = r #radius neutrinos
        self.color = (0, 255, 255) # color
        self.vx = vx # velocity 

    def move(self):
        self.x += self.vx

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
