moveMotorZIP = Kitronik_Move_Motor.create_move_motor_zipled(4)
headlight1 = moveMotorZIP.range(0, 1)
headlight2 = moveMotorZIP.range(1, 2)
rearlight1 = moveMotorZIP.range(2, 3)
rearlight2 = moveMotorZIP.range(3, 4)
rightSensor = Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.RIGHT)
leftSensor = Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.LEFT)
sensorDifference = abs(leftSensor - rightSensor)

def on_forever():
    basic.show_icon(IconNames.HAPPY)
    headlight1.show_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.BLUE))
    headlight2.show_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.PURPLE))
    rearlight1.show_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.BLUE))
    rearlight2.show_color(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.PURPLE))
    if sensorDifference > 10:
        if leftSensor > rightSensor:
            Kitronik_Move_Motor.motor_off(Kitronik_Move_Motor.Motors.MOTOR_RIGHT)
            Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_LEFT,
                Kitronik_Move_Motor.MotorDirection.FORWARD,
                30)
        else:
            Kitronik_Move_Motor.motor_off(Kitronik_Move_Motor.Motors.MOTOR_LEFT)
            Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_RIGHT,
                Kitronik_Move_Motor.MotorDirection.FORWARD,
                30)
    else:
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 30)
basic.forever(on_forever)
