import pygame, sys, os, configparser



class Window():
    config = configparser.ConfigParser()
    config.read("../settings/config.txt")
    DisplaySettings = config['Display Settings']
    screenWidth = int(DisplaySettings['resolution width'])
    screenHeight = int(DisplaySettings['resolution height'])
    displayScreen = pygame.display.set_mode((screenWidth, screenHeight))

enumerate