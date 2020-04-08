import pyudev
from source.sync import *
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

secret_key = config['DEFAULT']['SECRET_KEY'] # 'secret-key-of-myapp'
ci_hook_url = config['CI']['HOOK_URL'] # 'web-hooking-url-from-ci-service'

watch_name = "GARMIN"
context = pyudev.Context()
forra = context.list_devices()
def port_scan(watch_name):
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by('block')
    for device in iter(monitor.poll, None):
        if device.action == "add":
            if device.get('ID_FS_LABEL') == watch_name :
                print("Watch detected")
                return True
        elif device.action == "remove":
            if device.get('ID_FS_LABEL') == watch_name :
                print("Watch Removed!")
                break




if port_scan(watch_name) == True:
    sync.cloud_(watch_name)



