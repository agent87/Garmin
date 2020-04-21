
from pyudev import Context, Monitor, MonitorObserver
import pyudev
import time
import configparser
from subprocess import Popen, PIPE
import os
from sync import synchronise

config = configparser.ConfigParser()
config.read('config.ini')

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by('block')
for device in iter(monitor.poll, None):
    if config['credential']['ID_FS_LABEL'] == device.get('ID_FS_LABEL'):
        if device.action == "add":
            time.sleep(1)
            garmin_path = os.popen('lsblk -n {} -p -o MOUNTPOINT'.format(device.device_node)).read().strip('\n') 
            if config['sync']['local_'] == 'True':
                synchronise.local_(garmin_path, "../data/raw/")
        else:
            pass

