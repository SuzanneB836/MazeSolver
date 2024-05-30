let leftSensor = 0
let rightSensor = 0
let sensorDifference = 0
input.onButtonPressed(Button.A, function () {
	
})
input.onButtonPressed(Button.B, function () {
    Kitronik_Move_Motor.stop()
})
loops.everyInterval(500, function () {
    basic.showLeds(`
        # . . . .
        # . . . .
        # . . . .
        # . . . .
        # # # # #
        `)
    basic.showString("" + (leftSensor))
    basic.showLeds(`
        # # # # #
        # . . . #
        # # # # #
        # # . . .
        # . # . .
        `)
    basic.showString("" + (rightSensor))
})
basic.forever(function () {
    rightSensor = Kitronik_Move_Motor.readSensor(Kitronik_Move_Motor.LfSensor.Right)
    leftSensor = Kitronik_Move_Motor.readSensor(Kitronik_Move_Motor.LfSensor.Left)
    sensorDifference = Math.abs(leftSensor - rightSensor)
    if (leftSensor < 10 && rightSensor < 10) {
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Forward, 20)
    } else {
        if (leftSensor > rightSensor) {
            Kitronik_Move_Motor.motorOff(Kitronik_Move_Motor.Motors.MotorRight)
            Kitronik_Move_Motor.motorOn(Kitronik_Move_Motor.Motors.MotorLeft, Kitronik_Move_Motor.MotorDirection.Forward, 20)
        } else {
            Kitronik_Move_Motor.motorOff(Kitronik_Move_Motor.Motors.MotorLeft)
            Kitronik_Move_Motor.motorOn(Kitronik_Move_Motor.Motors.MotorRight, Kitronik_Move_Motor.MotorDirection.Forward, 20)
        }
    }
})
