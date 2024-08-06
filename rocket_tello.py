# -*- coding: utf-8 -*-
#!/usr/bin/python3


import threading
import socket
import sys
import time
import logger_config as log_cfg


log = log_cfg.setup_logger("tello.log")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1)
REC_MSG = 'OK'

def init(tello_ip='192.168.10.1',tello_port=8889):
    global tello_address
    tello_address = (tello_ip,tello_port)
    sock.bind(('',9000))
    if not send('command'):
        raise BizException('socker error')
    log.info(f'Tello init success! tello_address:{tello_address}')

def send(msg:str)->bool:
    bmsg = msg.encode(encoding="utf-8")
    sendNum = sock.sendto(bmsg, tello_address)
    try:
        data, server = sock.recvfrom(1518)
    except socket.timeout as e:
        log.error("An exception occurred", exc_info=True)
        return False
    recMsg = data.decode(encoding="utf-8")
    if recMsg != REC_MSG:
        log.error(f'send:{msg},sendNum:{sendNum},recive msg:{recMsg}')
    else :
        log.info(f'send:{msg},sendNum:{sendNum},recive msg:{recMsg}')
    time.sleep(1)
    return True

def close():
    log.info('start close . . . ')
    send("stop")
    sock.close()
    log.info('closed,bye bye')

class BizException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"BizException: {self.message}"
