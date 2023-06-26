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

def desenhar_texto(texto, fonte, cor, posicao):
    texto_surface = fonte.render(texto, True, cor)
    texto_rect = texto_surface.get_rect()
    texto_rect.center = posicao
    display.blit(texto_surface, texto_rect)


def criar_circulo(circles, mouse_pos):
    nome_circulo = asknome()
    circles.append((mouse_pos, nome_circulo))
    desenhar_circle(circles)
    if len(circles) > 1:
        desenhar_lines(circles[-2][0], circles[-1][0])


def desenhar_circle(circles):
    global font
    display.blit(space, (0, 0))
    desenhar_texto("f9 para Apagar", font2, white, (745, 20))
    desenhar_texto("f10 para Salvar", font2, white, (745, 40))
    desenhar_texto("f11 para Carregar", font2, white, (745, 60))

    total_distance = 0 

    for i in range(len(circles)):
        pos, name = circles[i]
        pygame.draw.circle(display, (255, 255, 255), pos, 5)
        font = pygame.font.Font(None, 20)
        name_text = font.render(name, True, (255, 255, 255))
        display.blit(name_text, (pos[0], pos[1] + 10))

        if i > 0:
            distance = pygame.math.Vector2(pos).distance_to(circles[i - 1][0])
            total_distance += distance
    if len(circles) > 1:
        for i in range(len(circles) - 1):
            start_pos = circles[i][0]
            end_pos = circles[i + 1][0]
            desenhar_lines(start_pos, end_pos)
            line_distance = pygame.math.Vector2(end_pos).distance_to(start_pos)
            line_text = font.render(f"Distância: {line_distance:.2f}", True, (255, 255, 255))
            line_pos = (start_pos[0] + (end_pos[0] - start_pos[0]) // 2,
                        start_pos[1] + (end_pos[1] - start_pos[1]) // 2)
            display.blit(line_text, line_pos)
    total_text = font.render(f"Soma Total: {total_distance:.2f}", True, (255, 255, 255))
    total_pos = (10, 10)
    display.blit(total_text, total_pos)

    pygame.display.update()


def desenhar_lines(start_pos, end_pos):
    pygame.draw.line(display, white, start_pos, end_pos, 1)

def asknome():
    root = tk.Tk()
    root.withdraw()
    name = tk.simpledialog.askstring("espaço", "Digíte o nome da estrela: ")
    return name if name else "desconhecida"
def save_data(circles):
    with open("circles.txt", "w") as file:
        for pos, name in circles:
            file.write(f"{pos[0]},{pos[1]},{name}\n")


def load_data():
    circles = []
    try:
        with open("circles.txt", "r") as file:
            for line in file:
                x, y, name = line.strip().split(",")
                pos = (int(x), int(y))
                circles.append((pos, name))
        return circles
    except:
        with open('circles.txt', 'w') as file:
            pass


def desenhar_menu():
    display.blit(back, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    botao_load_rect = pygame.Rect(tamanho[0] - 200, tamanho[1] // 2 - 25, 150, 30)
    botao_start_rect = pygame.Rect(tamanho[0] - 200, tamanho[1] // 2 - 75, 150, 30)
    botao_quit_rect = pygame.Rect(tamanho[0] - 200, tamanho[1] // 2 - -25, 150, 30)
    if botao_load_rect.collidepoint(mouse_pos):
        pygame.draw.rect(display, black, botao_load_rect)
        desenhar_texto("Load", font, white, (botao_load_rect.center))
    else:
        pygame.draw.rect(display, menu_color, botao_load_rect)
        desenhar_texto("Load", font, pygame.Color('black'), (botao_load_rect.center))
    if botao_start_rect.collidepoint(mouse_pos):
        pygame.draw.rect(display, black, botao_start_rect)
        desenhar_texto("Start", font, white, (botao_start_rect.center))
    else:
        pygame.draw.rect(display, menu_color, botao_start_rect)
        desenhar_texto("Start", font, pygame.Color('black'), (botao_start_rect.center))
    if botao_quit_rect.collidepoint(mouse_pos):
        pygame.draw.rect(display, black, botao_quit_rect)
        desenhar_texto("Quit Game", font, white, (botao_quit_rect.center))
    else:
        pygame.draw.rect(display, menu_color, botao_quit_rect)
        desenhar_texto("Quit Game", font, black, (botao_quit_rect.center))


def verificar_botao(x, y, largura, altura):
    mouse_pos = pygame.mouse.get_pos()
    if x < mouse_pos[0] < x + largura and y < mouse_pos[1] < y + altura:
        return True