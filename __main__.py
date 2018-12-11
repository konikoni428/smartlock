import hashlib
import time
from logging import DEBUG, Formatter, StreamHandler, getLogger

# from reader import Reader
import database
from servo import Servo
import led
from switch import Switch
from door import Door
import pigpio
import slack

logger = getLogger(__name__)
handler = StreamHandler()
handler.setFormatter(Formatter("[%(levelname)s] %(message)s"))
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False


def main():
    pi = pigpio.pi()
    srv = Servo(pi)
    swi = Switch(pi, srv)
    door = Door(pi)

    try:
        while True:
            logger.debug("waiting id card")
            # ここでカード読み込み
            if database.confirm("番号"), "IDm"):
                srv.open_lock()
                slack.send_slack(name)
                time.sleep(10)
                while door.door_status() == door.OPEN:
                    time.sleep(0.5)
                srv.close_lock()
            else:
                led.red_led_on()
                print("Can't confirm.")
                time.sleep(3)
                led.red_led_off()
    except:
        pi.stop()
        r.close()
        main()


if __name__ == "__main__":
    main()
