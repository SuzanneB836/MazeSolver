def on_forever():
    basic.show_number(Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.LEFT))
    basic.pause(100)
basic.forever(on_forever)
