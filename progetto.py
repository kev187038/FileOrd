import pathlib
import string
import posixpath
import os
import shutil
from pathlib import Path
from pathlib import PurePath
from pathlib import PurePosixPath
import threading
import logging
import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

def background_task(dir_queue):

    while True:
        #2 argomenti: uno è source e il secondo è destination
        #il processo prende come argomenti la cartella in cui vengono sempre messe le foto(tipo download) e lo controlla
        #in background di continuo, appena trova una foto la sposta con costo O(n) nella cartella a scelta dell'utente
        lista_file = os.listdir(dir_queue[0])

        for i in lista_file:
            if(PurePosixPath(i).suffix == '.jpeg'):
                os.system("mv "+ "'"+ dir_queue[0] + "/" + i + "'  '" + dir_queue[1] +"'")

        time.sleep(5) # faccio dormire il process per alleggerirlo


def main():

    dir1 = "/home/student/Desktop/dir1"
    dir2 = "/home/student/Desktop/dir2"
    
    lista_file = os.listdir(dir1)        

    print(lista_file)

    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500, 200, 500, 300)
    win.setWindowTitle("Progetto")

    Label = QtWidgets.QLabel(win)
    Label.setText("Testo")
    Label.move(50,50)


    #os.system("mv "+dir1+" "+dir2)
    #os.system("mv /home/student/Desktop/dir1/index.jpeg /home/student/Desktop/dir2")

    win.show()
    sys.exit(app.exec())


    



main()