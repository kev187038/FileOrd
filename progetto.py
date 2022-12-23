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
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLabel, QGridLayout, QMessageBox, QLineEdit

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

def confirmation_action(field_src, field_des):
    dir1 = field_src.text()
    dir2 = field_des.text()

    if (not os.path.isdir(dir1)) or (not os.path.isdir(dir2)):
        msg = QMessageBox()
        msg.setText("Paths don't exist. Please retry.")
        msg.exec_()
    else:
        two_dirs = [dir1, dir2]
        background_task(two_dirs)

def main():

    dir1 = "/home/student/Desktop/dir1"
    dir2 = "/home/student/Desktop/dir2"
    
    lista_file = os.listdir(dir1)        

    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500, 200, 1000, 700)
    win.setWindowTitle("Progetto")

    Label = QtWidgets.QLabel(win)
    Label.setText("Source Folder")
    Label.adjustSize()
    Label.move(50,100)

    Src_field = QLineEdit(win)
    Src_field.setPlaceholderText("Enter source folder path")
    Src_field.adjustSize()
    Src_field.move(50,150)


    Label2 = QtWidgets.QLabel(win)
    Label2.setText("Destination Folder")
    Label2.adjustSize()
    Label2.move(800,100)

    Des_field =  QLineEdit(win)
    Des_field.setPlaceholderText("Enter destination folder path")
    Des_field.adjustSize()
    Des_field.move(800,150)

    confirmation_button = QPushButton(win)
    confirmation_button.setText("Confirm")
    confirmation_button.clicked.connect(lambda:confirmation_action(Src_field, Des_field))
    confirmation_button.move(800,500)


    win.show()
    sys.exit(app.exec())


    



main()