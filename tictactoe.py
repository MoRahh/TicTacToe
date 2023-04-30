import sys
import pygame
from constants import *

# PyGame
pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('TICTACTOE-AI')
screen.fill(BG_COLOR)

class Game:
    def __init__(self):
        self.show_lines() 

    def show_lines(self):
        # VERTICAL
        pygame.draw.line(screen, LINE_COLOR, (SQ_SIZE, 0), (SQ_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQ_SIZE, 0), (WIDTH - SQ_SIZE, HEIGHT), LINE_WIDTH)
        # HORIZONTAL
        pygame.draw.line(screen, LINE_COLOR, (0 , SQ_SIZE), (WIDTH , SQ_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQ_SIZE), (WIDTH, HEIGHT - SQ_SIZE), LINE_WIDTH)


def main():

    # Game Object
    game = Game()

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

main()