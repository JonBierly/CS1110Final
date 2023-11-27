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
        if uvage.is_pressing('2'):
            HOME_MENU = False
            MAP2_TRUE = True
        if uvage.is_pressing('3'):
            HOME_MENU = False
            MAP3_TRUE = True

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
    if DEAD_MENU:
        died_text = uvage.from_text(400, 100, "YOU DIED!", 100, 'red')
        restart_text = uvage.from_text(400, 200, "Press SPACE to return to the home menu", 50, 'red')
        camera.draw(died_text)
        camera.draw(restart_text)
        if uvage.is_pressing('space'):
            HOME_MENU = True
            DEAD_MENU = False


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

"""
def map_2_environment():

def map_3_environment():
"""
def tick():
    camera.clear("black")
    home_menu()
    dead_menu()
    map_1_environment()
    camera.display()

uvage.timer_loop(30, tick)
