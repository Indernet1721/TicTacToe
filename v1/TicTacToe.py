import pygame
from pygame.locals import *
import time

pygame.init()
#Ccreate Window 
screen_width = 600 
screen_height = 600
line_colour = (255,255,255)
icon = pygame.image.load('./assets/Icon.png')
pygame.display.set_icon(icon)
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TicTacToe")

tile_size = 200

bg = pygame.image.load("./assets/Background.jpg")
bg = pygame.transform.scale(bg, (screen_width, screen_height))

#Create Win_lines
line_img = pygame.image.load("./assets/line.png")
line_img = pygame.transform.scale(line_img, (screen_width-20, 130))
scaled_line = pygame.transform.scale(line_img, (screen_width+90, 130))
diag1_image = pygame.transform.rotate(scaled_line, 45)
diag2_image = pygame.transform.rotate(scaled_line, 135)
col_image = pygame.transform.rotate(line_img, 90)

#Create images
x_img = pygame.image.load('./assets/x.png')
o_img = pygame.image.load('./assets/o.png')

# updated on win
win_row = None 

class World:
    def __init__(self, data):
        self.tile_list = []
        global x_img, o_img



#Darw world_data
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(x_img, (tile_size-50, tile_size-50))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size+30
                    img_rect.y = row_count * tile_size+25
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(o_img, (tile_size-50, tile_size-50))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size+30
                    img_rect.y = row_count * tile_size+25
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    def draw(self):
        for tile in self.tile_list:
            window.blit(tile[0], tile[1])


#The game world
world_data = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


world = World(world_data)
#(Position; size)
area_rect1 = pygame.Rect(0, 0, 200, 200)
area_rect2 = pygame.Rect(200, 0, 200, 200)
area_rect3 = pygame.Rect(400, 0, 200, 200)
area_rect4 = pygame.Rect(0, 200, 200, 200)
area_rect5 = pygame.Rect(200, 200, 200, 200)
area_rect6 = pygame.Rect(400, 200, 200, 200)
area_rect7 = pygame.Rect(0, 400, 200, 200)
area_rect8 = pygame.Rect(200, 400, 200, 200)
area_rect9 = pygame.Rect(400, 400, 200, 200)
run = True

xTurn = True

xWin_data = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
]

oWin_data = [
    [2, 2, 2],
    [2, 2, 2],
    [2, 2, 2]
]

run_checkwin = True

def checkwin():
    
    global xWin_data, oWin_data, world_data, run_checkwin, win_row
    if run_checkwin:
    
        print("check")

        # rows -
        for row in world_data:
            if(row[0] == row[1] == row[2] == 1):
                print("X hat gewonnen!")
                win_row = world_data.index(row)
                if win_row == 0:
                    window.blit(line_img, (0, 75))
                if win_row == 1:
                    window.blit(line_img, (0, 75*(win_row+2.3)))
                if win_row == 2:
                    window.blit(line_img, (0, 75*(win_row+4)))
                run_checkwin = False
                return
            if(row[0] == row[1] == row[2] == 2):
                win_row = world_data.index(row)
                if win_row == 0:
                    window.blit(line_img, (0, 75))
                if win_row == 1:
                    window.blit(line_img, (0, 75*(win_row+1)))
                if win_row == 2:
                    window.blit(line_img, (0, 75*(win_row+4)))
                run_checkwin = False
                return


        # cols |
        rotated_world_data = list(reversed(list(zip(*world_data)))) # rotate 90deg
        for row in rotated_world_data:
            if(row[0] == row[1] == row[2] == 1):
                print("X hat gewonnen!")
                win_row = rotated_world_data.index(row)
                if win_row == 0:
                    window.blit(col_image, (450, 0))
                if win_row == 1:
                    window.blit(col_image, (250, 0))
                if win_row == 2:
                    window.blit(col_image, (75, 0))
                    print("Test")
                run_checkwin = False
                return
            if(row[0] == row[1] == row[2] == 2):
                print("O hat gewonnen!")
                win_row = rotated_world_data.index(row)
                if win_row == 2:
                    window.blit(col_image, (75, 0))
                    print("Test")
                if win_row == 1:
                    window.blit(col_image, (250, 0))
                if win_row == 0:
                    window.blit(col_image, (450, 0))
                run_checkwin = False
                return


        # diag /
        if world_data[0][2] == world_data[1][1] == world_data[2][0] != 0: 
            if world_data[0][2] == 1:
                print("X hat gewonnen!")
                
                window.blit(diag1_image, (50, 0))
                run_checkwin = False
                return

            else:
                print("O hat gewonnen!")
                
                return True



        # diag \
        if rotated_world_data [0][2] == rotated_world_data[1][1] == rotated_world_data[2][0] != 0: # diag /
            if rotated_world_data[0][2] == 1:
                print("X hat gewonnen!")
                
                window.blit(diag2_image, (25, 10))
                return True
            else:

                print("O hat gewonnen!")
                
                window.blit(diag2_image, (25, 10))
                return True

    
        



window.blit(bg, (0, 0))
while run:

    

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if area_rect1.collidepoint(mouse_x, mouse_y):
                if world_data[0][0] == 0:
                    if xTurn:
                    
                        world_data[0][0] = 1
                        xTurn = False
                    
                    elif not xTurn:
                        world_data[0][0] = 2
                        xTurn = True
                    
            if area_rect2.collidepoint(mouse_x, mouse_y):
                if world_data[0][1] == 0:
                    if xTurn:
                        world_data[0][1] = 1 
                        xTurn = False
                    
                    elif not xTurn:
                        world_data[0][1] = 2
                        xTurn = True
            if area_rect3.collidepoint(mouse_x, mouse_y):
                if world_data[0][2] == 0:
                    if xTurn:
                        world_data[0][2] = 1 
                        xTurn = False

                    elif not xTurn:
                        world_data[0][2] = 2
                        xTurn = True
                    
            if area_rect4.collidepoint(mouse_x, mouse_y):
                if world_data[1][0] == 0:
                    if xTurn:
                        world_data[1][0] = 1 
                        xTurn = False

                    elif not xTurn:
                        world_data[1][0] = 2
                        xTurn = True
                    
            if area_rect5.collidepoint(mouse_x, mouse_y):
                if world_data[1][1] == 0:
                    if xTurn:
                        world_data[1][1] = 1 
                        xTurn = False

                    elif not xTurn:
                        world_data[1][1] = 2
                        xTurn = True
                    
            if area_rect6.collidepoint(mouse_x, mouse_y):
                if world_data[1][2] == 0:
                    if xTurn:
                        world_data[1][2] = 1 
                        xTurn = False

                    elif not xTurn:
                        world_data[1][2] = 2
                        xTurn = True
                    
            if area_rect7.collidepoint(mouse_x, mouse_y):
                if world_data[2][0] == 0:
                    if xTurn:
                        world_data[2][0] = 1 
                        xTurn = False

                    elif not xTurn:
                        world_data[2][0] = 2
                        xTurn = True
                    
            if area_rect8.collidepoint(mouse_x, mouse_y):
                if world_data[2][1] == 0:
                    if xTurn:
                        world_data[2][1] = 1 
                        xTurn = False

                    elif not xTurn:
                        world_data[2][1] = 2
                        xTurn = True
                    
            if area_rect9.collidepoint(mouse_x, mouse_y):
                if world_data[2][2] == 0:
                    if xTurn:
                        world_data[2][2] = 1 
                        xTurn = False

                    elif not xTurn:
                        world_data[2][2] = 2
                        xTurn = True
            checkwin()
                    
                    





    world = World(world_data) 
    world.draw()  
    pygame.display.update()

pygame.quit()
