# -*- coding: utf-8 -*-
import hashlib
import time
from logging import DEBUG, Formatter, StreamHandler, getLogger

# from reader import Reader
import database
import slack

logger = getLogger(__name__)
handler = StreamHandler()
handler.setFormatter(Formatter("[%(levelname)s] %(message)s"))
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False


def main():
    name = raw_input("追加するユーザー名を入力してください（英数字のみ）:")

    #　ここでカード読み込み

    database.make_info("番号", name, "IDm")
    print ("追加完了しました。")
    slack.add_user("番号", name)
    time.sleep(1)


if __name__ == "__main__":
    main()
