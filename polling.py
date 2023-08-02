'''Host Polling Lib'''
import os
import sys
import platform
import subprocess
import socket

from multiprocessing.pool import ThreadPool

def poll_host(host, count=3):
    '''Poll host via ICMP ping to see if it is up/down'''

    if platform.system().lower() == 'windows':
        command = ['ping', '-n', str(count), '-w', '1000', host]
    else:
        command = ['ping', '-c', str(count), '-W', '1', host]

    response = subprocess.call(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return ('Up' if response == 0 else 'Down')