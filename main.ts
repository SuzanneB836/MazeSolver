let sensorDifference = 0
let leftSensor = 0
let rightSensor = 0
let moveMotorZIP = Kitronik_Move_Motor.createMoveMotorZIPLED(4)
let headlight1 = moveMotorZIP.range(0, 1)
let headlight2 = moveMotorZIP.range(1, 2)
let rearlight1 = moveMotorZIP.range(2, 3)
let rearlight2 = moveMotorZIP.range(3, 4)
basic.forever(function () {
    basic.showIcon(IconNames.Happy)
    headlight1.showColor(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Blue))
    headlight2.showColor(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Purple))
    rearlight1.showColor(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Blue))
    rearlight2.showColor(Kitronik_Move_Motor.colors(Kitronik_Move_Motor.ZipLedColors.Purple))
    rightSensor = Kitronik_Move_Motor.readSensor(Kitronik_Move_Motor.LfSensor.Right)
    leftSensor = Kitronik_Move_Motor.readSensor(Kitronik_Move_Motor.LfSensor.Left)
    sensorDifference = Math.abs(leftSensor - rightSensor)
    if (sensorDifference > 10) {
        if (leftSensor > rightSensor) {
            Kitronik_Move_Motor.motorOff(Kitronik_Move_Motor.Motors.MotorRight)
            Kitronik_Move_Motor.motorOn(Kitronik_Move_Motor.Motors.MotorLeft, Kitronik_Move_Motor.MotorDirection.Forward, 30)
        } else {
            Kitronik_Move_Motor.motorOff(Kitronik_Move_Motor.Motors.MotorLeft)
            Kitronik_Move_Motor.motorOn(Kitronik_Move_Motor.Motors.MotorRight, Kitronik_Move_Motor.MotorDirection.Forward, 30)
        }
    } else {
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Forward, 30)
    }
})
