from encoded_motor_driver import EncodedMotorDriver
from time import sleep
from machine import Pin

# SETUP
left_motor = EncodedMotorDriver((15,13,14), (10, 11))
right_motor = EncodedMotorDriver((16,18,17), (19, 20))
stby = Pin(12, Pin.OUT)
stby.on()

# LOOP

start = True
Checkpoint_1 = False
Checkpoint_2 = False
Checkpoint_3 = False
Checkpoint_4 = False
Finish = False
FinishPart2 = False
right_motor_distance = 0
left_motor_distance = 0

#axel distance is 134 mm
#center point is at 134 / 2 = 67 mm


def motor_in_range(distance, current_distance):
    
    inRange = current_distance - 15 < distance < current_distance + 15
    return inRange
    
    

while start == True:
    right_motor_distance = (right_motor.encoder_counts / (98.5 * 28)) * 168
    left_motor_distance = (left_motor.encoder_counts/ (98.5 * 28)) * 168
    print(f"left_distance = {left_motor_distance}, right_distance = {right_motor_distance}")
    if motor_in_range(750, right_motor_distance) and motor_in_range(750, left_motor_distance):
        start = False
        Checkpoint_1 = True
        right_motor.stop() 
        left_motor.stop()
        sleep(3)
        break
    right_motor.forward(.25)
    left_motor.forward(.265)
    
while Checkpoint_1 == True:
    right_motor_distance = (right_motor.encoder_counts / (98.5 * 28)) * 168
    left_motor_distance = (left_motor.encoder_counts/ (98.5 * 28)) * 168
    print(f"left_distance = {left_motor_distance}, right_distance = {right_motor_distance}")
    if motor_in_range(750 + 105, right_motor_distance) and motor_in_range(750 - 105, left_motor_distance):
         Checkpoint_1 = False
         Checkpoint_2 = True 
         right_motor.stop() 
         left_motor.stop()
         sleep(1)
         break
    right_motor.forward(.25)
    left_motor.backward(.265)
while Checkpoint_2 == True:
    right_motor_distance = (right_motor.encoder_counts / (98.5 * 28)) * 168
    left_motor_distance = (left_motor.encoder_counts/ (98.5 * 28)) * 168
    print(f"left_distance = {left_motor_distance}, right_distance = {right_motor_distance}")
    if motor_in_range(750 + 105 + 500, right_motor_distance) and motor_in_range(750 - 105 + 500, left_motor_distance):
        Checkpoint_2 = False
        Checkpoint_3 = True
        right_motor.stop() 
        left_motor.stop()
        sleep(3)
        break
    right_motor.forward(.25)
    left_motor.forward(.265)
while Checkpoint_3 == True:
    right_motor_distance = (right_motor.encoder_counts / (98.5 * 28)) * 168
    left_motor_distance = (left_motor.encoder_counts/ (98.5 * 28)) * 168
    print(f"left_distance = {left_motor_distance}, right_distance = {right_motor_distance}")
    if motor_in_range(750 + 105 + 500 - 316, right_motor_distance) and motor_in_range(750 - 105 + 500 + 316, left_motor_distance):
        Checkpoint_3 = False
        Checkpoint_4 = True
        right_motor.stop() 
        left_motor.stop()
        sleep(1)
        break
    right_motor.backward(.25)
    left_motor.forward(.265)
while Checkpoint_4 == True:
    right_motor_distance = (right_motor.encoder_counts / (98.5 * 28)) * 168
    left_motor_distance = (left_motor.encoder_counts/ (98.5 * 28)) * 168
    print(f"left_distance = {left_motor_distance}, right_distance = {right_motor_distance}")
    if motor_in_range(750 + 105 + 500 - 316 + 500, right_motor_distance) and motor_in_range(750 - 105 + 500 + 316 + 500, left_motor_distance):
        Checkpoint_4 = False
        Finish = True
        right_motor.stop() 
        left_motor.stop()
        sleep(3)
        break
    right_motor.forward(.25)
    left_motor.forward(.265)
while Finish == True:
    right_motor_distance = (right_motor.encoder_counts / (98.5 * 28)) * 168
    left_motor_distance = (left_motor.encoder_counts/ (98.5 * 28)) * 168
    print(f"left_distance = {left_motor_distance}, right_distance = {right_motor_distance}")
    if motor_in_range( 750 + 105 + 500 - 316 + 500 + 78, right_motor_distance) and motor_in_range(750 - 105 + 500 + 316 + 500 - 72, left_motor_distance):
        Finish = False
        FinishPart2 = True
        right_motor.stop() 
        left_motor.stop()
        sleep(1)
        break
    right_motor.forward(.25)
    left_motor.backward(.265)
while FinishPart2 == True:
    right_motor_distance = (right_motor.encoder_counts / (98.5 * 28)) * 168
    left_motor_distance = (left_motor.encoder_counts/ (98.5 * 28)) * 168
    print(f"left_distance = {left_motor_distance}, right_distance = {right_motor_distance}")
    if motor_in_range( 750 + 105 + 500 - 316 + 500 + 78 + 559, right_motor_distance) and motor_in_range(750 - 105 + 500 + 316 + 500 - 78 + 559, left_motor_distance):
        right_motor.stop()
        left_motor.stop()
        right_motor.stop() 
        left_motor.stop()
        sleep(3)
        break
    right_motor.forward(.25)
    left_motor.forward(.265)