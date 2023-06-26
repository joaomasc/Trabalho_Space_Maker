import pygame
import tkinter as tk
from tkinter import simpledialog

pygame.init()
pygame.mixer.init()
tamanho = (800, 600)
pontos = []
display = pygame.display.set_mode(tamanho)
pygame.display.set_caption('SPACE MAKER')
icone = pygame.image.load('art.jpg')
pygame.display.set_icon(icone)
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
menu_color = (127, 172, 219)
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 20)
clock = pygame.time.Clock()
space = pygame.image.load('SPACE.jpg')
back = pygame.image.load('telescopio.jpg')
back = pygame.transform.scale(back, tamanho)
space = pygame.transform.scale(space, tamanho)
pygame.mixer.music.load('stws.mp3')
pygame.mixer.music.play(-1)