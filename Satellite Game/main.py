import pgzrun
import random
from time import time 

HEIGHT = 500
WIDTH = 800

satellite_list = [""]
lines_list = [""]
next_satellite = 0
number_of_satellite = 10

start_time = 0
end_time = 0
total_time = 0



def create_satellites():
    global start_time
    for i in range(0,number_of_satellite):
        satellite = Actor("satellite")

        satellite.pos = random.randint(20,780), random.randint(20,480)
        satellite_list.append(satellite)
    start_time = time()
        

def draw():
    global total_time
    screen.blit("starysky",(0,0))
    number = 1
    for satellite in satellite_list():
        screen.draw.text(str(number),(satellite.pos[0],satellite.pos[1]+20))
        satellite.draw()
        number +=1
    for line in lines_list():
        screen.draw.line(line[0],line[1],(255,255,255))
    if next_satellite < number_of_satellite:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize = 30)
    else:
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize = 30)
   
def update():
    pass

def on_mouse_down(pos):
    pass
create_satellites()
pgzrun.go()