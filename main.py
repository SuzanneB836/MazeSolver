leftSensor = 0
rightSensor = 0
sensorDifference = 0

def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    Kitronik_Move_Motor.stop()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_every_interval():
    basic.show_leds("""
        # . . . .
        # . . . .
        # . . . .
        # . . . .
        # # # # #
        """)
    basic.show_string("" + str((leftSensor)))
    basic.show_leds("""
        # # # # #
        # . . . #
        # # # # #
        # # . . .
        # . # . .
        """)
    basic.show_string("" + str((rightSensor)))
loops.every_interval(500, on_every_interval)

def on_forever():
    global rightSensor, leftSensor, sensorDifference
    rightSensor = Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.RIGHT)
    leftSensor = Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.LEFT)
    sensorDifference = abs(leftSensor - rightSensor)
    if leftSensor < 10 and rightSensor < 10:
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 30)
    else:
        if leftSensor > rightSensor:
            Kitronik_Move_Motor.motor_off(Kitronik_Move_Motor.Motors.MOTOR_LEFT)
            Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_RIGHT,
                Kitronik_Move_Motor.MotorDirection.FORWARD,
                30)
        else:
            Kitronik_Move_Motor.motor_off(Kitronik_Move_Motor.Motors.MOTOR_RIGHT)
            Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_LEFT,
                Kitronik_Move_Motor.MotorDirection.FORWARD,
                30)
basic.forever(on_forever)
