# -*- coding: utf-8 -*-
class Door:
    MINIMUM_VALIE = 250
    CLOSE = 0
    OPEN = 1

    def __init__(self, pi):
        self.pi = pi
        self.h = pi.spi_open(0, 200000, 0) # 0ch 200kHz(5V) mode0

    def door_status(self):
        (count, rx_data) = self.pi.spi_xfer(self.h, [0x68, 0x00])
        value = ((rx_data[0] & 3) << 8) + rx_data[1]
        if value >= Door.MINIMUM_VALIE:
            return Door.CLOSE
        else:
            return Door.OPEN
