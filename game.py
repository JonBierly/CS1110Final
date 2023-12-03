""" 
Jonathan Bierly, dnz4an
Anshul Chiranth, hmf6av

1v1 combat game! Players are able to move freely throughout the map, they have a ## set weapon, there are obstacles/coverage throughout the screen.

Basic Features
1) Users control players through the keyboard. They can move around within the bounds of the maps, around obstacles. This will be done through the is_pressing() method for game boxes.

2) Game is over when 1 player runs out of health. Players lose health when they are hit by the other's weapon/bullets. This will be implemented using the touches() method. The bullets will be deleted after hitting a player.

3) We will find sprite sheets for the characters. There will be a moving animation, and the character will flip when it changes directions. Sprite sheets will keep track of the frame and alternate through a list based on the current frame.


Additional Features
1) 2 players simultaneously. Two players will move their characters simultaneously and shoot/fight with each other. One will control with w/a/s/d and the other with the arrow keys. Each character will have a shoot button as well.

2) Multiple maps/levels. Players will be able to select multiple maps from the start menu.

3) Health Bar. The health bar will decrease as players are hit by the other player. This will be implemented as a gamebox in the top left/right of the map.

4) Restart from Game Over. After one player lose's all of their health After a player dies, it will say "YOU DIED" and will take you give you the option to go back to the main menu. This will be done through a alive_true variable.

Changes from original features: Levels are no longer unlocked, but are instead playable from the start. A player can select any of the 3 playable maps. Each player will only be able to shoot their gun straight.
There also will not be the option to replay a level, and instead just an option to go back to the main menu after a playe dies.
"""



import uvage

camera = uvage.Camera(800, 600)
##OBJECTS


MAP1_TRUE = False
MAP2_TRUE = False
MAP3_TRUE = False
HOME_MENU = True
DEAD_MENU = False
environment = []
background = 0



def home_menu():
    global HOME_MENU
    global camera
    global MAP1_TRUE
    global MAP2_TRUE
    global MAP3_TRUE
    global DEAD_MENU
    global player1_alive
    global player2_alive
    global player1_health
    global player2_health
    if HOME_MENU:
        DEAD_MENU = False
        player1_health = 5
        player2_health = 5
    if HOME_MENU:
        screen = uvage.from_text(400, 100, "Welcome to GunFight!", 100, 'red')
        map_choose = uvage.from_text(400, 150, 'Click the number under a map to choose it!', 40, 'blue')
        map_1_option_1 = uvage.from_color(100, 300, "red", 100, 150)
        map_1_option_2 = uvage.from_text(100, 410, '1',50, 'red')
        map_2_option_1 = uvage.from_color(400, 300, "blue", 100, 150)
        map_2_option_2 = uvage.from_text(400, 410, '2', 50, 'blue')
        map_3_option_1 = uvage.from_color(700, 300, "green", 100, 150)
        map_3_option_2 = uvage.from_text(700, 410, '3', 50, 'green')

        if uvage.is_pressing('1'):
            MAP1_TRUE = True
            HOME_MENU = False
            player1_alive = True
            player2_alive = True
            player1.x, player1.y = 100, 370
            player2.x, player2.y = 700, 370
        if uvage.is_pressing('2'):
            HOME_MENU = False
            MAP2_TRUE = True
            player1_alive = True
            player2_alive = True
            player1.x, player1.y = 200, 100
            player2.x, player2.y = 600, 100
        if uvage.is_pressing('3'):
            HOME_MENU = False
            MAP3_TRUE = True
            player1_alive = True
            player2_alive = True
            player1.x, player1.y = 200, 100
            player2.x, player2.y = 600, 100

        camera.draw(map_3_option_1)
        camera.draw(map_3_option_2)
        camera.draw(map_2_option_1)
        camera.draw(map_2_option_2)
        camera.draw(map_1_option_1)
        camera.draw(map_1_option_2)
        camera.draw(screen)
        camera.draw(map_choose)

def dead_menu():
    global DEAD_MENU
    global HOME_MENU
    global player1_alive
    global player2_alive
    if DEAD_MENU == True:
        HOME_MENU = False
    if DEAD_MENU == True:
        died_text = uvage.from_text(400, 100, "YOU DIED!", 100, 'red')
        restart_text = uvage.from_text(400, 200, "Press T to return to the home menu", 50, 'red')
        camera.draw(died_text)
        camera.draw(restart_text)
        if uvage.is_pressing('t'):
            HOME_MENU = True
            DEAD_MENU = False
            player1_alive = False
            player2_alive = False



def map_1_environment():
    global environment
    global background
    if MAP1_TRUE:
        background = uvage.from_image(400,300, 'Everest.png')
        background.scale_by(0.5)
        environment = [uvage.from_color(400, 500, 'brown', 500, 20),
                       uvage.from_color(100, 400, 'green', 100, 20),
                       uvage.from_color(700, 400, 'green', 100, 20),
                       uvage.from_color(400, 300, 'brown', 500, 20),
                       uvage.from_color(400, 425, 'yellow', 100, 20),
                       uvage.from_color(400, 200, 'yellow', 100, 20)
        ]
        camera.draw(background)
        for x in environment:
            camera.draw(x)
        camera.draw(uvage.from_text(400,100, 'MAP ONE', 50, 'green'))

moving_platform = uvage.from_color(0,570, 'brown', 100, 20)
def map_2_environment():
    global environment
    global background
    global moving_platform
    if MAP2_TRUE:
        background = uvage.from_image(400, 300, 'Space Image.jpeg')
        background.scale_by(0.5)
        if moving_platform.x == 0:
            moving_platform.speedx = 8
        if moving_platform.x == 800:
            moving_platform.speedx = -8
        moving_platform.move_speed()
        environment = [uvage.from_color(200, 100, 'green', 75, 20),
                       uvage.from_color(200, 200, 'green', 75, 20),
                       uvage.from_color(200, 300, 'green', 75, 20),
                       uvage.from_color(200, 400, 'green', 75, 20),
                       uvage.from_color(200, 500, 'green', 75, 20),
                       uvage.from_color(400, 100, 'yellow', 75, 20),
                       uvage.from_color(400, 200, 'yellow', 75, 20),
                       uvage.from_color(400, 300, 'yellow', 75, 20),
                       uvage.from_color(400, 400, 'yellow', 75, 20),
                       uvage.from_color(400, 500, 'yellow', 75, 20),
                       uvage.from_color(600, 100, 'blue', 75, 20),
                       uvage.from_color(600, 200, 'blue', 75, 20),
                       uvage.from_color(600, 300, 'blue', 75, 20),
                       uvage.from_color(600, 400, 'blue', 75, 20),
                       uvage.from_color(600, 500, 'blue', 75, 20),
                       moving_platform]
        camera.draw(background)
        for x in environment:
            camera.draw(x)
        camera.draw(uvage.from_text(400, 50, 'MAP TWO', 50, 'green'))


def map_3_environment():
    global environment
    global background
    global moving_platform
    if MAP3_TRUE:
        background = uvage.from_image(400, 300, 'Tilted_season_8.jpeg')
        background.scale_by(0.5)

        if moving_platform.x == 0:
            moving_platform.speedx = 8
        if moving_platform.x == 800:
            moving_platform.speedx = -8
        moving_platform.move_speed()



        environment = [uvage.from_color(100, 100, 'green', 200, 20),
                       uvage.from_color(700, 100, 'green', 200, 20),
                       uvage.from_color(550, 200, 'yellow', 75, 20),
                       uvage.from_color(250, 200, 'yellow', 75, 20),
                       uvage.from_color(400, 300, 'blue', 200, 20),
                       uvage.from_color(550, 400, 'yellow', 75, 20),
                       uvage.from_color(250, 400, 'yellow', 75, 20),
                       uvage.from_color(100, 500, 'green', 200, 20),
                       uvage.from_color(700, 500, 'green', 200, 20)
                       ]
        camera.draw(background)
        for x in environment:
            camera.draw(x)
        camera.draw(uvage.from_text(400, 50, 'MAP TWO', 50, 'green'))


# PLAYER DEFAULTS
player1_images = uvage.load_sprite_sheet("pixel_character_pale_yellow.png", 8, 8)
player1 = uvage.from_image(100, 400, player1_images[40])
player1_alive = False
player2_images = uvage.load_sprite_sheet("pixel_character_dark_red.png", 8, 8)
player2 = uvage.from_image(400, 400, player2_images[32])
player2_alive = False
player1_speed = 7
player1_frame = 24
player1_right = True
player1_jump = False


player2_speed = 7
player2_frame = 16
player2_right = False
player2_jump = False
def move_player1():
    global player1_alive
    global player1_frame
    global player1_right
    global environment
    global player1_jump
    if player1_alive == True:
        is_walking = False
        if uvage.is_pressing("a"):
            if player1_right:
                player1.flip()
                player1_right = False
            player1.speedx = -player1_speed
            is_walking = True
        elif uvage.is_pressing("d"):
            if not player1_right:
                player1.flip()
                player1_right = True
            player1.speedx = player1_speed
            is_walking = True
        if is_walking:
            player1_frame += 0.3
            if player1_frame >= 31:
                player1_frame = 24
            player1.image = player1_images[int(player1_frame)]
        else:
            player1.image = player1_images[40]
            player1.speedx = 0



        for x in environment:
            if player1.bottom_touches(x):
                player1_jump = True
        if player1_jump == True:
            if uvage.is_pressing('w'):
                player1.speedy = -15
                player1_jump = False
        if player1.speedy < 5:
            player1.speedy += 1
        elif player1.speedy == 10:
            player1.speedy = 5
        if uvage.is_pressing('s'):
            player1.speedy = 10

        for x in environment:
            player1.move_to_stop_overlapping(x, -10, -10)
        player1.move_speed()
        for x in environment:
            player1.move_to_stop_overlapping(x, -10, -10)
        camera.draw(player1)

def move_player2():
    global player2_frame
    global player2_right
    global player2_jump
    is_walking = False

    if player2_alive == True:
        if uvage.is_pressing("left arrow"):
            if player2_right:
                player2.flip()
                player2_right = False
            player2.x -= player1_speed
            is_walking = True
        elif uvage.is_pressing("right arrow"):
            if not player2_right:
                player2.flip()
                player2_right = True
            player2.x += player1_speed
            is_walking = True
        if is_walking:
            player2_frame += 0.3
            if player2_frame >= 23:
                player2_frame = 16
            player2.image = player2_images[int(player2_frame)]
        else:
            player2.image = player2_images[32]


        for x in environment:
            if player2.bottom_touches(x):
                player2_jump = True
        if player2_jump == True:
            if uvage.is_pressing('up arrow'):
                player2.speedy = -15
                player2_jump = False
        if player2.speedy < 5:
            player2.speedy += 1
        elif player2.speedy == 10:
            player2.speedy = 5
        if uvage.is_pressing('down arrow'):
            player2.speedy = 10

        for x in environment:
            player2.move_to_stop_overlapping(x, -10, -10)
        player2.move_speed()
        for x in environment:
            player2.move_to_stop_overlapping(x, -10, -10)
        camera.draw(player2)


# GUN DEFAULTS
player1_bulletlist =[]
player1_shoot = True
player1_timer = 0
player2_bulletlist =[]
player2_shoot = True
player2_timer = 0
def make_bullet(player, player_right):
    bullet = uvage.from_color(player.x, player.y - 10, "yellow", 10, 4)
    if player_right == True:
        bullet.speedx = 40
    else:
        bullet.speedx = -40
    return bullet
def gun_player1():
    global player1_bulletlist
    global player1_right
    global player1_alive
    global player1_shoot
    global player1_timer
    global environment
    if player1_alive == True:
        if player1_timer <=0:
            player1_shoot = True
        else:
            player1_shoot = False


        if player1_shoot == True:
            if uvage.is_pressing('space'):
                player1_bulletlist.append(make_bullet(player1, player1_right))
                player1_timer = 10
        for bullet in player1_bulletlist:
            if (bullet.x > 810) or (bullet.x < -10):
                player1_bulletlist.remove(bullet)
            for x in environment:
                if bullet.touches(x):
                    player1_bulletlist.remove(bullet)
            bullet.move_speed()
            camera.draw(bullet)
    player1_timer -= 1

def gun_player2():
    global player2_bulletlist
    global player2_right
    global player2_alive
    global player2_shoot
    global player2_timer
    global environment
    if player2_alive == True:
        if player2_timer <=0:
            player2_shoot = True
        else:
            player2_shoot = False


        if player2_shoot == True:
            if uvage.is_pressing('m'):
                player2_bulletlist.append(make_bullet(player2, player2_right))
                player2_timer = 10
        for bullet in player2_bulletlist:
            if (bullet.x > 810) or (bullet.x < -10):
                player2_bulletlist.remove(bullet)
            for x in environment:
                if bullet.touches(x):
                    player2_bulletlist.remove(bullet)
            bullet.move_speed()
            camera.draw(bullet)
    player2_timer -= 1

player1_health = 5
player2_health = 5
def health_player1():
    global player1_health
    global player1_alive
    global player2_bulletlist
    global DEAD_MENU
    global MAP1_TRUE
    global MAP2_TRUE
    global MAP3_TRUE
    player1_health_background = uvage.from_color(50, 40, "black", 100 ,50)
    player1_healthbar = uvage.from_color(50, 40, "red", player1_health *16,30)
    for bullet in player2_bulletlist:
        if player1.touches(bullet):
            player2_bulletlist.remove(bullet)
            player1_health -= 1
    if player1.y > 610:
        player1_health -= 1
    if player2_alive == True:
        camera.draw(player1_health_background)
        camera.draw(player1_healthbar)
    if player1_health == 0:
        player1_alive = False
        DEAD_MENU = True
        MAP1_TRUE = False
        MAP2_TRUE = False
        MAP3_TRUE = False

def health_player2():
    global player2_health
    global player2_alive
    global player1_bulletlist
    global DEAD_MENU
    global MAP1_TRUE
    global MAP2_TRUE
    global MAP3_TRUE
    player2_healthbar = uvage.from_color(750, 40, "red", player2_health *16,30)
    player2_health_background = uvage.from_color(750, 40, "black", 100, 50)
    for bullet in player1_bulletlist:
        if player2.touches(bullet):
            player1_bulletlist.remove(bullet)
            player2_health -= 1
    if player2.y > 610:
        player2_health -= 1
    if player1_alive == True:
        camera.draw(player2_health_background)
        camera.draw(player2_healthbar)
    if player2_health == 0:
        player2_alive = False
        DEAD_MENU = True
        MAP1_TRUE = False
        MAP2_TRUE = False
        MAP3_TRUE = False
def tick():
    camera.clear("black")
    home_menu()
    dead_menu()
    map_1_environment()
    map_2_environment()
    map_3_environment()
    move_player1()
    move_player2()
    gun_player1()
    gun_player2()
    health_player1()
    health_player2()
    camera.display()

uvage.timer_loop(30, tick)
