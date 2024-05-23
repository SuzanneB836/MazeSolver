

# Function to read line sensor (assuming it returns values 0 or 1 for black or white)
def read_line_sensor():
    left_sensor = pin0.read_digital()  # Replace with your sensor pin
    right_sensor = pin1.read_digital()  # Replace with your sensor pin
    return left_sensor, right_sensor

# Function to move forward
def move_forward(speed=50):
    motor_driver.motor_on(kitronik_motor_driver.MOTOR_LEFT, kitronik_motor_driver.MOTORDIRECTION_FORWARD, speed)
    motor_driver.motor_on(kitronik_motor_driver.MOTOR_RIGHT, kitronik_motor_driver.MOTORDIRECTION_FORWARD, speed)

# Function to stop
def stop():
    motor_driver.motor_off(kitronik_motor_driver.MOTOR_LEFT)
    motor_driver.motor_off(kitronik_motor_driver.MOTOR_RIGHT)

# Function to turn left
def turn_left():
    motor_driver.motor_on(kitronik_motor_driver.MOTOR_LEFT, kitronik_motor_driver.MOTORDIRECTION_REVERSE, 50)
    motor_driver.motor_on(kitronik_motor_driver.MOTOR_RIGHT, kitronik_motor_driver.MOTORDIRECTION_FORWARD, 50)
    sleep(300)  # Adjust timing as necessary
    stop()

# Function to turn right
def turn_right():
    motor_driver.motor_on(kitronik_motor_driver.MOTOR_LEFT, kitronik_motor_driver.MOTORDIRECTION_FORWARD, 50)
    motor_driver.motor_on(kitronik_motor_driver.MOTOR_RIGHT, kitronik_motor_driver.MOTORDIRECTION_REVERSE, 50)
    sleep(300)  # Adjust timing as necessary
    stop()

# Main loop to solve the maze
while True:
    left_sensor, right_sensor = read_line_sensor()

    if left_sensor == 1 and right_sensor == 1:
        # Both sensors on the line, move forward
        move_forward()
    elif left_sensor == 1 and right_sensor == 0:
        # Left sensor on the line, turn left
        turn_left()
    elif left_sensor == 0 and right_sensor == 1:
        # Right sensor on the line, turn right
        turn_right()
    else:
        # Both sensors off the line, stop and decide next move
        stop()
        sleep(100)
        # Basic strategy for maze solving could be added here
        # This example stops the robot if both sensors are off the line

    sleep(100)  # Short delay to prevent overwhelming the sensors
