import pygame
from pygame.locals import *
import time

pygame.init()

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

line_img = pygame.image.load("./assets/line.png")
line_img = pygame.transform.scale(line_img, (screen_width-20, 130))
diag1_image = pygame.transform.rotate(line_img, 45)
diag2_image = pygame.transform.rotate(line_img, 135)
diag2_image = pygame.transform.rotate(line_img, 135)

x_img = pygame.image.load('./assets/x.png')
o_img = pygame.image.load('./assets/o.png')

win_row = None # updated on win


class World:
    def __init__(self, data):
        self.tile_list = []
        global x_img, o_img



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

world_data = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


world = World(world_data)
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
                
                window.blit(line_img, (0, 75*(win_row+1)))
                run_checkwin = False
                return
            if(row[0] == row[1] == row[2] == 2):
                print("O hat gewonnen!")
                window.blit(line_img, (0, 75))
                run_checkwin = False
                win_row = world_data.index(row)
                return


        # cols |
        rotated_world_data = list(reversed(list(zip(*world_data)))) # rotate 90deg
        for row in rotated_world_data:
            if(row[0] == row[1] == row[2] == 1):
                print("X hat gewonnen!")
                
                run_checkwin = False
                return (True, world_data.index(row))
            if(row[0] == row[1] == row[2] == 2):
                print("O hat gewonnen!")
                
                run_checkwin = False
                return (True, world_data.index(row))


        # diag /
        if world_data[0][2] == world_data[1][1] == world_data[2][0] != 0: 
            if world_data[0][2] == 1:
                print("X hat gewonnen!")
                
                return True

            else:
                print("O hat gewonnen!")
                
                return True



        # diag \
        if rotated_world_data [0][2] == rotated_world_data[1][1] == rotated_world_data[2][0] != 0: # diag /
            if rotated_world_data[0][2] == 1:
                print("X hat gewonnen!")
                
                return True
            else:

                print("O hat gewonnen!")
                
                return True

        return (False, None)
        


# def draw_line():
#     start = None
#     end = None
    
#     if win_row == 0:
#         start = (area_rect1.width/2,area_rect1.height/2)
#         end = (area_rect3.width/2, area_rect3.height/2)
        
#     elif win_row == 1:
#         start = (area_rect4.width/2,area_rect4.height/2)
#         end = (area_rect6.width/2, area_rect6.height/2)
#     else:
#         return
        
#     pygame.draw.line(window, line_colour, start, end, width=5000)
    
    
        



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
                    
                    
    # draw_line()



    print(run_checkwin)
    print(world_data)
    world = World(world_data) 
    world.draw()  
    pygame.display.update()

pygame.quit()
