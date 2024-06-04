leftSensor = 0
rightSensor = 0
moveMotorZIP = Kitronik_Move_Motor.create_move_motor_zipled(4)
headlight1 = moveMotorZIP.range(0, 1)
headlight2 = moveMotorZIP.range(1, 2)
rearlight1 = moveMotorZIP.range(2, 3)
rearlight2 = moveMotorZIP.range(3, 4)

def on_every_interval():
    basic.show_string("59")
loops.every_interval(1000, on_every_interval)

def on_forever():
    global rightSensor, leftSensor
    headlight1.show_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.RED))
    headlight2.show_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.WHITE))
    rearlight1.show_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.RED))
    rearlight2.show_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.WHITE))
    rightSensor = Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.RIGHT)
    leftSensor = Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.LEFT)
    if leftSensor < 10 and rightSensor < 10:
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 22)
    elif leftSensor > 90 and rightSensor > 90:
        Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_LEFT,
            Kitronik_Move_Motor.MotorDirection.FORWARD,
            20)
        Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_RIGHT,
            Kitronik_Move_Motor.MotorDirection.REVERSE,
            20)
    else:
        if leftSensor > rightSensor:
            Kitronik_Move_Motor.motor_off(Kitronik_Move_Motor.Motors.MOTOR_RIGHT)
            Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_LEFT,
                Kitronik_Move_Motor.MotorDirection.FORWARD,
                15)
        else:
            Kitronik_Move_Motor.motor_off(Kitronik_Move_Motor.Motors.MOTOR_LEFT)
            Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_RIGHT,
                Kitronik_Move_Motor.MotorDirection.FORWARD,
                15)
basic.forever(on_forever)
