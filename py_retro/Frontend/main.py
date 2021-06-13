import pygame, os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .display import Window
pygame.init()

def main():
    screen = Window.displayScreen
