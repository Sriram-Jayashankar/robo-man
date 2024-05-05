from gpiozero import Motor
import pygame

motor1 = Motor(forward=27, backward=17)
motor2 = Motor(forward=22, backward=23)

# Initialize pygame
pygame.init()
pygame.display.set_mode((500, 500))  # Initialize pygame window (not needed for input handling)

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
    

try:
    while True:
        # Check for events in the event queue
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    forward()
                elif event.key == pygame.K_s:
                    backward()
                elif event.key == pygame.K_d:
                    right()
                elif event.key == pygame.K_a:
                    left()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    stop()
                if event.key == pygame.K_s:
                    stop()
                if event.key == pygame.K_d:
                    stop()
                if event.key == pygame.K_a:
                    stop()
except KeyboardInterrupt:
    pass
finally:
    stop()
    pygame.quit()