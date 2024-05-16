basic.forever(function on_forever() {
    basic.showNumber(Kitronik_Move_Motor.readSensor(Kitronik_Move_Motor.LfSensor.Left))
    basic.pause(100)
})
