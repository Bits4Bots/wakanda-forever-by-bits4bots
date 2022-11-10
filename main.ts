sprites.onOverlap(SpriteKind.Guard, SpriteKind.Enemy, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    info.changeScoreBy(1)
    Namor.setPosition(0, 0)
    controller.moveSprite(Namor, 148, 2)
})
info.onScore(20, function on_on_score() {
    Namor.destroy()
    scene.setBackgroundImage(assets.image`
        boston-bridge
    `)
    game.over(true)
    effects.confetti.startScreenEffect()
    game.showLongText("We are safe!", DialogLayout.Bottom)
    Shuri.sayText("Wakanda Forever", 5000, false)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap2(sprite2: Sprite, otherSprite2: Sprite) {
    info.changeLifeBy(-1)
    Namor.setPosition(148, 2)
})
let Namor : Sprite = null
let Shuri : Sprite = null
game.showLongText("Bits4Bots friends...", DialogLayout.Bottom)
game.showLongText("Help Shuri, Okoye and Riri escape Namor. Press \"A\" to go to the next screen.", DialogLayout.Full)
game.showLongText("When the game begins, press the Arrow Keys to move Shuri, Okoye and Riri. If Namor catches you, you will lose points!", DialogLayout.Full)
game.showLongText("Earn 20 points to win and to stay alive you must keep your heart(s).", DialogLayout.Full)
scene.setBackgroundImage(assets.image`
    wakanda
`)
Shuri = sprites.create(assets.image`
    shuri
`, SpriteKind.Player)
controller.moveSprite(Shuri)
Shuri.setStayInScreen(true)
Namor = sprites.create(assets.image`
    namor
`, SpriteKind.Enemy)
Namor.setPosition(148, 2)
Namor.follow(Shuri, 30)
let Riri = sprites.create(assets.image`
    riri
`, SpriteKind.Guard)
let Okoye = sprites.create(assets.image`
    riri
`, SpriteKind.Guard)
controller.moveSprite(Riri, 34, -53)
controller.moveSprite(Okoye, -68, -58)
info.setLife(2)
