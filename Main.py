import pygame
import sys
import random
pygame.init() #test
rocks = pygame.image.load("rocks.png")
goldore = pygame.image.load("goldore.png")

def main():
    click = False
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("the great mine")
    p1_deck = deck()

    while True:
        screen.fill((200, 170, 49))
        pygame.draw.lines(screen, (0,0,0), True, [(50,50),(50, 750),(950,750),(950,50)], 4)

        def draw_wheel(xpos, ypos, width, height):
            pygame.draw.rect(screen, (255,255,255), (xpos, ypos, width, height), 0, 10)
            pygame.draw.rect(screen, (0,0,0), (xpos, ypos, width, height), 4, 10)
            spacing = 10
            cell_height = (height-8 - (spacing * (6))) / 5
            cell_width = (width-8 - (spacing * (6))) / 5
            for gridx in range(5):
                for gridy in range(5):
                    #realgridx = gridx*(width/5)+xpos+spacing/2
                    #realgridy = gridy*(height/5)+ypos+spacing/2
                    #pygame.draw.rect(screen, (120,80,10), (realgridx, realgridy, width/5 -spacing, height/5 - spacing), 0, 10)
                    cell_x = xpos+4 + spacing + gridx*(spacing+cell_width)
                    cell_y = ypos+4 + spacing + gridy*(spacing+cell_height)
                    cell_center_x = cell_x + cell_width/2
                    cell_center_y = cell_y + cell_height/2
                    pygame.draw.rect(screen, (120,80,10), (cell_x, cell_y, cell_width, cell_height), 0, 10)
                    screen.blit(p1_deck.get_cell(gridx, gridy), goldore.get_rect(center=(cell_center_x, cell_center_y)))
            for row in range(5):
                    cell_x = xpos - spacing -40
                    cell_y = ypos+4 + spacing + row*(spacing+cell_height)
                    cell_center_y = cell_y + cell_height/2
                    if button(screen, (cell_x, cell_center_y-20, 40, 40)) and click:
                        p1_deck.reroll_row(row)
            for col in range(5):
                    cell_y = ypos - spacing -40
                    cell_x = xpos+4 + spacing + col*(spacing+cell_width)
                    cell_center_x = cell_x + cell_width/2
                    if button(screen, (cell_center_x-20, cell_y, 40, 40)) and click:
                        p1_deck.reroll_col(col)
        draw_wheel(300, 400, 400, 350)


        pygame.display.flip() #displays next frame once everythong is ready behind the scenes
        click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.QUIT:
                sys.exit()

def button(screen, rect):
    rect = pygame.Rect(rect)
    pygame.draw.rect(screen, (0,0,0), rect, 0, 10)
    if rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (80,80,80), rect, 0, 10)
        return True
    else:
        return False

class deck:
    def __init__(self) -> None:
        self.deck = [rocks]*30 + [goldore]*10
        random.shuffle(self.deck)
    def shuffle(self):
        random.shuffle(self.deck)
    def __iter__(self):
        return iter(self.deck)
    def get_cell(self, xpos, ypos):
        return self.deck[xpos + ypos*5]
    def reroll_cell(self, xpos, ypos):
        swapee = random.randrange(25, len(self.deck))
        swaper = xpos + ypos*5
        self.deck[swapee], self.deck[swaper] = self.deck[swaper], self.deck[swapee]
    def reroll_row(self, row):
        for num in range(5):
            self.reroll_cell(num, row)
    def reroll_col(self, col):
        for num in range(5):
            self.reroll_cell(col, num)

           
main()