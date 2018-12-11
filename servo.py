from time import sleep
import led


class Servo:
    servo_pin = 18

    def __init__(self, pi):
        self.pi = pi

    def servo_rotate(self, degree):
        motor_pulse = ((degree * 100 / 9) + 500)
        self.pi.set_servo_pulsewidth(Servo.servo_pin, motor_pulse)
        sleep(0.5)
        self.pi.set_servo_pulsewidth(Servo.servo_pin, 0)

    def open_lock(self):
        self.pi.set_servo_pulsewidth(Servo.servo_pin, 2250)
        led.green_led_on()
        sleep(0.2)
        self.pi.set_servo_pulsewidth(Servo.servo_pin, 0)

    def close_lock(self):
        sleep(1)
        self.pi.set_servo_pulsewidth(Servo.servo_pin, 1300)
        led.green_led_off()
        sleep(0.2)
        self.pi.set_servo_pulsewidth(Servo.servo_pin, 0)
        sleep(1)
