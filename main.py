def on_button_pressed_a():
    global running, captured
    running = not (running)
    if running:
        timeanddate.set24_hour_time(0, 0, 0)
    else:
        captured = timeanddate.time(timeanddate.TimeFormat.HHMMSS2_4HR)
        basic.show_string(captured)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if not (running):
        basic.show_string(captured)
input.on_button_pressed(Button.B, on_button_pressed_b)

dotLocation = 0
xy = 0
captured = ""
running = False
running = False
coords = [11, 21, 31, 32, 33, 23, 13, 12]

def on_forever():
    global xy, dotLocation
    if running:
        basic.clear_screen()
        xy = coords[dotLocation]
        led.toggle(Math.idiv(xy, 10), xy % 10)
        basic.pause(1000 / 8)
        dotLocation = (dotLocation + 1) % 8
    else:
        basic.show_icon(IconNames.NO)
basic.forever(on_forever)
