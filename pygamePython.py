import pygame
from pygame.locals import *
import random

#Variables of the games
size =width,height=(800,800)
road_w= int(width/1.6)
roadmark_w=int(width/80)
right_lane=width/2 + road_w/4
left_lane=width/2 - road_w/4
speed =1


pygame.init()

running=True

screen=pygame.display.set_mode(size)
pygame.display.set_caption("TESTING PYGAME")

#set background color
screen.fill((60,220,0))

 #Apply changes
pygame.display.update()
#Insert Our Vehicles

car=pygame.image.load("favicon.ico")
car_loc=car.get_rect()
car_loc.center=right_lane, height *0.8
#Insert the enemy Vehicles
car2=pygame.image.load("rkb.jpg")
car2_loc=car.get_rect()
car2_loc.center=left_lane, height *0.2

counter =0
#Game Loop
while running:
    counter +=1
    if counter ==5000:
        speed += 0.15
        counter =0
        print("Level Up", speed)
    #animate enemy vehicles
    car2_loc[1] +=speed
    if car2_loc[1] > height:
        if random.randint(0,1)==0:
            car2_loc.center=right_lane, -200
        else:
            car2_loc.center=left_lane, -200
    #End game Logic
    if car_loc[0] ==car2_loc[0] and car2_loc[1] > car_loc[1] -250:
        print("Game Over!! You Lose.")
        break
    #Event listeners
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
            
        if event.type ==KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc =car_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car2_loc =car2_loc.move([int(road_w/2), 0])
                
                
                
    #draw graphics
    pygame.draw.rect(
    screen,
    (50,50,50),
    (width/2-road_w/2, 0, road_w, height)
    )
    #Yellow Line on the roads
    pygame.draw.rect(
    screen,
    (255,240,60),
    (width/2 - roadmark_w/2, 0, roadmark_w, height)
    )
       #White lines on the roads at the ends
    pygame.draw.rect(
    screen,
    (255,255,255),
    (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height)
    )
    #Another white lines of the roads
    pygame.draw.rect(
    screen,
    (255,255,255),
    (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height)
    )
    #Load the images of vehicles with this code 
    screen.blit(car,car_loc)
    screen.blit(car2,car2_loc)
    pygame.display.update()
pygame.quit()