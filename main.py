def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    Namor.set_position(0, 0)
    controller.move_sprite(Namor, 148, 2)
sprites.on_overlap(SpriteKind.guard, SpriteKind.enemy, on_on_overlap)

def on_on_score():
    Namor.destroy()
    scene.set_background_image(assets.image("""
        boston-bridge
    """))
    game.over(True)
    effects.confetti.start_screen_effect()
    game.show_long_text("We are safe!", DialogLayout.BOTTOM)
    Shuri.say_text("Wakanda Forever", 5000, False)
info.on_score(20, on_on_score)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_life_by(-1)
    Namor.set_position(148, 2)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

Namor: Sprite = None
Shuri: Sprite = None
game.show_long_text("Bits4Bots friends...", DialogLayout.BOTTOM)
game.show_long_text("Help Shuri, Okoye and Riri escape Namor. Press \"A\" to go to the next screen.",
    DialogLayout.FULL)
game.show_long_text("When the game begins, press the Arrow Keys to move Shuri, Okoye and Riri. If Namor catches you, you will lose points!",
    DialogLayout.FULL)
game.show_long_text("Earn 20 points to win and to stay alive you must keep your heart(s).",
    DialogLayout.FULL)
scene.set_background_image(assets.image("""
    wakanda
"""))
Shuri = sprites.create(assets.image("""
    shuri
"""), SpriteKind.player)
controller.move_sprite(Shuri)
Shuri.set_stay_in_screen(True)
Namor = sprites.create(assets.image("""
    namor
"""), SpriteKind.enemy)
Namor.set_position(148, 2)
Namor.follow(Shuri, 30)
Riri = sprites.create(assets.image("""
    riri
"""), SpriteKind.guard)
Okoye = sprites.create(assets.image("""
    riri
"""), SpriteKind.guard)
controller.move_sprite(Riri, 34, -53)
controller.move_sprite(Okoye, -68, -58)
info.set_life(2)