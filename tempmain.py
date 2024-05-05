
from gpiozero import Motor
import pygame

motor1 = Motor(forward=27, backward=17)
motor2 = Motor(forward=22, backward=23)

# Initialize pygame
pygame.init()
pygame.display.set_mode((100, 100))  # Initialize pygame window (not needed for input handling)

def forward():
    motor1.forward(speed=1)
    motor2.forward(speed=1)

def backward():
    motor1.backward(speed=1)
    motor2.backward(speed=1)

def right():
    motor1.forward(speed=1)
    motor2.backward(speed=1)

def left():
    motor1.backward(speed=1)
    motor2.forward(speed=1)

def stop():
    motor1.stop()
    motor2.stop()

def diagonal_up_left():
    motor1.forward(speed=0.4)
    motor2.forward(speed=0.7)

def diagonal_up_right():
    motor1.forward(speed=0.4)
    motor2.forward(speed=0.7)

def diagonal_down_left():
    motor1.backward(speed=0.4)
    motor2.backward(speed=0.7)

def diagonal_down_right():
    motor1.backward(speed=0.4)
    motor2.backward(speed=0.7)

try:
    while True:
        #Check for events in the event queue
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if pygame.key.get_pressed()[pygame.K_a]:
                        diagonal_up_left()
                    elif pygame.key.get_pressed()[pygame.K_d]:
                        diagonal_up_right()
                    else:
                        forward()
                elif event.key == pygame.K_s:
                    if pygame.key.get_pressed()[pygame.K_a]:
                        diagonal_down_left()
                    elif pygame.key.get_pressed()[pygame.K_d]:
                        diagonal_down_right()
                    else:
                        backward()
                elif event.key == pygame.K_a:
                    if pygame.key.get_pressed()[pygame.K_w]:
                        diagonal_up_left()
                    elif pygame.key.get_pressed()[pygame.K_s]:
                        diagonal_down_left()
                    else:
                        left()
                elif event.key == pygame.K_d:
                    if pygame.key.get_pressed()[pygame.K_w]:
                        diagonal_up_right()
                    elif pygame.key.get_pressed()[pygame.K_s]:
                        diagonal_down_right()
                    else:
                        right()
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
                    stop()
except KeyboardInterrupt:
    pass
finally:
    stop()
    pygame.quit()