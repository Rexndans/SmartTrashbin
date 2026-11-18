let Jarak = 0
servos.P0.setAngle(90)
basic.forever(function () {
    Jarak = sonar.ping(
    DigitalPin.P0,
    DigitalPin.P1,
    PingUnit.Centimeters
    )
    if (Jarak < 15 && Jarak > 0) {
        basic.showIcon(IconNames.Yes)
        servos.P0.setAngle(0)
    } else {
        basic.showIcon(IconNames.No)
    }
    basic.pause(5000)
})
