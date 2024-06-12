#---IMPORTS----

import os
from engine.features import *
from engine.command import *

import eel

#---connext path to html---
html_file_path = os.path.join("www", "index.html")

def start():
    #---START HTML---
    eel.init("www")
    #---PLAY SOUND---
    SS() 

    #---START APP---
    os.system('start msedge.exe --app="http:localhost:8000/index.html')
    eel.start('index.html',mode=None,host='localhost',block=True)
if __name__ == "__main__":
    start()
    