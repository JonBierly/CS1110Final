import uvage
camera = uvage.Camera(800, 600)

player1_images = uvage.load_sprite_sheet("pixel_character_pale_yellow.png", 8, 8)
player1 = uvage.from_image(100, 400, player1_images[40])
player2_images = uvage.load_sprite_sheet("pixel_character_dark_red.png", 8, 8)
player2 = uvage.from_image(400, 400, player2_images[32])

player1_speed = 3
player1_frame = 24
player1_right = True

player2_speed = 3
player2_frame = 16
player2_right = False

def move_player1():
    global player1_frame
    global player1_right
    is_walking = False
    if uvage.is_pressing("a"):
        if player1_right:
            player1.flip()
            player1_right = False
        player1.x -= player1_speed
        is_walking = True
    elif uvage.is_pressing("d"):
        if not player1_right:
            player1.flip()
            player1_right = True
        player1.x += player1_speed
        is_walking = True
    if is_walking:
        player1_frame += 0.3
        if player1_frame >= 31:
            player1_frame = 24
        player1.image = player1_images[int(player1_frame)]
    else:
        player1.image = player1_images[40]
    camera.draw(player1)

def move_player2():
    global player2_frame
    global player2_right
    is_walking = False
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
    camera.draw(player2)

def tick():
    camera.clear("white")
    move_player1()
    move_player2()
    camera.display()

uvage.timer_loop(30, tick)