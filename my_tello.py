# -*- coding: utf-8 -*-
#!/usr/bin/python3

import rocket_tello as Tello
import time
import logger_config as log_cfg

if __name__ == '__main__':
    try:
        Tello.init(tello_ip='10.57.240.147')
        Tello.send("123")
        Tello.send('bbb')
    except Exception as e:
        Tello.log.error("An exception occurred", exc_info=True)
    finally :
        Tello.close()

