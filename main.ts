input.onButtonPressed(Button.A, function () {
    running = !(running)
    if (running) {
        timeanddate.set24HourTime(0, 0, 0)
    } else {
        captured = timeanddate.time(timeanddate.TimeFormat.HHMMSS24hr)
        basic.showString(captured)
    }
})
input.onButtonPressed(Button.B, function () {
    if (!(running)) {
        basic.showString(captured)
    }
})
let dotLocation = 0
let xy = 0
let captured = ""
let running = false
running = false
let coords = [
11,
21,
31,
32,
33,
23,
13,
12
]
basic.forever(function () {
    if (running) {
        basic.clearScreen()
        xy = coords[dotLocation]
        led.toggle(Math.idiv(xy, 10), xy % 10)
        basic.pause(1000 / 8)
        dotLocation = (dotLocation + 1) % 8
    } else {
        basic.showIcon(IconNames.No)
    }
})
