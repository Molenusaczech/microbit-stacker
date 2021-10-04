def on_button_pressed_a():
    global buttonPressSinceLastUpdate, showDifficulty
    buttonPressSinceLastUpdate = 1
    showDifficulty = 0
    for index in range(6):
        led.unplot(index, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Difficulty
    if showDifficulty == 1:
        if Difficulty == 4:
            Difficulty = 0
        else:
            Difficulty += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

direction = 0
lastFloorPos = 0
CurrentPos = 0
showDifficulty = 0
Difficulty = 0
buttonPressSinceLastUpdate = 0
currentFloor = 4
buttonPressSinceLastUpdate = 0
Difficulty = 0
showDifficulty = 1

def on_forever():
    global buttonPressSinceLastUpdate, lastFloorPos, currentFloor, CurrentPos, direction
    if showDifficulty == 1:
        for index2 in range(6):
            led.unplot(index2, 0)
        index3 = 0
        while index3 <= Difficulty:
            led.plot(index3, 0)
            index3 += 1
    if buttonPressSinceLastUpdate == 1:
        buttonPressSinceLastUpdate = 0
        if not (currentFloor == 4):
            if not (CurrentPos == lastFloorPos):
                basic.clear_screen()
                while True:
                    basic.show_string("Game Over")
        lastFloorPos = CurrentPos
        currentFloor += -1
        if currentFloor == -1:
            while True:
                basic.show_string("You win")
    else:
        led.unplot(CurrentPos, currentFloor)
        if direction == 0:
            if not (CurrentPos == 4):
                CurrentPos += 1
            else:
                direction = 1
        elif not (CurrentPos == 0):
            CurrentPos += -1
        else:
            direction = 0
        led.plot(CurrentPos, currentFloor)
        basic.pause(120 - Difficulty * 20)
basic.forever(on_forever)
