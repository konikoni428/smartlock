import pigpio

green_led_pin = 23
red_led_pin = 24


def green_led_on():
    pi = pigpio.pi()
    pi.set_mode(green_led_pin, pigpio.OUTPUT)
    pi.write(green_led_pin, 1)
    pi.stop()


def green_led_off():
    pi = pigpio.pi()
    pi.write(green_led_pin, 0)
    pi.stop()


def red_led_on():
    pi = pigpio.pi()
    pi.set_mode(red_led_pin, pigpio.OUTPUT)
    pi.write(red_led_pin, 1)
    pi.stop()


def red_led_off():
    pi = pigpio.pi()
    pi.write(red_led_pin, 0)
    pi.stop()
