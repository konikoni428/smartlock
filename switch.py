# -*- coding: utf-8 -*-
import time
import pigpio
from door import Door
import slack
import database
import subprocess
import led


class Switch:
    switch_pin = 22

    def __init__(self, pi, servo):
        self.pi = pi
        self.door = Door(pi)
        self.time_old = time.time()
        self.servo = servo
        pi.set_mode(Switch.switch_pin, pigpio.INPUT)
        pi.set_pull_up_down(Switch.switch_pin, pigpio.PUD_DOWN)

        self._cb = pi.callback(Switch.switch_pin, pigpio.RISING_EDGE, self._cbf1)

    def _cbf(self, gpio, level, tick):
        if time.time() - self.time_old < 1:
            return
        else:
            self.servo.open_lock()
            database.button_info_insert()
            slack.button()
            time.sleep(5)
            while self.door.door_status() == self.door.OPEN:
                time.sleep(0.5)
            self.servo.close_lock()
        self.time_old = time.time()

    def _cbf1(self, gpio, level, tick):
        # 長押しでリスタートの機能追加版
        if time.time() - self.time_old < 1:
            return
        else:
            counter = 0
            while True:
                status = self.pi.read(Switch.switch_pin)
                if status == 1:
                    counter += 1
                    if counter >= 60:
                        led.red_led_on()
                        led.green_led_on()
                        time.sleep(2)
                        led.green_led_off()
                        led.red_led_off()
                        self.time_old = time.time()
                        subprocess.Popen("sudo systemctl restart badegg.service", shell=True)
                        break
                else:
                    self.servo.open_lock()
                    database.button_info_insert()
                    slack.button()
                    time.sleep(5)
                    while self.door.door_status() == self.door.OPEN:
                        time.sleep(0.5)
                    self.servo.close_lock()
                    self.time_old = time.time()
                    break
                time.sleep(0.05)
