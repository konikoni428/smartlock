import pigpio
import time


pi = pigpio.pi()
h = pi.spi_open(0, 200000, 0)
while True:
    (count, rx_data) = pi.spi_xfer(h, [0x68, 0x00])
    value = ((rx_data[0] & 3) << 8) + rx_data[1]
    print value
    print bin(value)
    time.sleep(0.5)
