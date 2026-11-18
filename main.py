Jarak = 0
servos.P0.set_angle(90)

def on_forever():
    global Jarak
    Jarak = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS)
    if Jarak < 15 and Jarak > 0:
        basic.show_icon(IconNames.YES)
        servos.P0.set_angle(0)
    else:
        basic.show_icon(IconNames.NO)
    basic.pause(5000)
basic.forever(on_forever)
