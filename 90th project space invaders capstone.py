import math
import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load(r"C:\Users\Navraj- PC\Downloads\amog us background.jpg")
pygame.display.set_caption('SPACE INVADERS')
icon = pygame.image.load(r"C:\Users\Navraj- PC\OneDrive\Pictures\Screenshots\DAREALICCCCCCCCCOOOOOOOOOONNNNNN.png")
pygame.display.set_icon(icon)

player_img = pygame.image.load(r"C:\Users\Navraj- PC\Downloads\player.png")
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
