from dirsync import sync
from os import system 


class synchronise():
    def local_(garmin, back_folder_name): #Include Garmin watch mount point, back-up folder location
        sync(garmin, back_folder_name, 'sync', purge = True, create=True)

    def cloud_(self):
        print("This is the cloud sync function")
    
    def rasp_(self):
        print("This is the raspberyy sync function")



