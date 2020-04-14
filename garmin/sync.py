from dirsync import sync
from os import system 
import configparser
import pyudev
import psutil

#configuration file
config = configparser.ConfigParser()
config.read('config.ini')



class synchronise():
    def local_(garmin, back_folder_name): #Include Garmin watch mount point, back-up folder location
        sync(garmin+"/GARMIN", back_folder_name, 'sync', purge = True, create=True)
        os.system("find . -type d | cpio -pdvm ../converted/")

    def cloud_(self):
        print("This is the cloud sync function")
    
    def rasp_(self):
        print("This is the raspberyy sync function")

class mountpoint:
    def mount_point(device_node):
        for partitions in psutil.disk_partitions():
            if partitions.device == device_node:
                return partitions.mountpoint

    def get():   #asynchronous port scan
        context = pyudev.Context()
        for device in context.list_devices(subsystem='block'):
            if device.get('ID_FS_LABEL') == config['credential']['ID_FS_LABEL']:
                return mountpoint.mount_point(device.device_node)
            else:
                break

if __name__ == "__main__":
    if mountpoint.get() == None:
        pass
    else:
        synchronise.local_(mountpoint.get(), "../data/raw")