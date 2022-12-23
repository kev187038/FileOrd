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
import time
import sys
import PyQt5
import PyQt5.uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileSystemModel, QApplication, QWidget, QPushButton, QLabel, QGridLayout, QMessageBox, QLineEdit 
        

def background_task(dir1, dir2):
    dir_queue = [dir1, dir2]
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
        msg.setText("Both paths or one of them don't exist. Please retry.")
        msg.exec_()
    else:
        thread = threading.Thread(target=background_task, daemon=True, args=(dir1, dir2))
        thread.start()


def close_action(win):
    win.hide()

def search_action(text):
    dir_path = os.getcwd()
    dir_name = QtWidgets.QFileDialog.getExistingDirectory(None,"Open dir", dir_path)
    text.setText(dir_name)


def main():        

    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500, 200, 1000, 700)
    win.setWindowTitle("FileOrd")

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

    hide_button = QPushButton(win)
    hide_button.setText("Close window")
    hide_button.clicked.connect(lambda: close_action(win))
    hide_button.adjustSize()
    hide_button.move(100,500)

    search_button_1 = QPushButton(win)
    search_button_1.setText("Search on local")
    search_button_1.clicked.connect(lambda: search_action(Src_field))
    search_button_1.adjustSize()
    search_button_1.move(50,200)

    search_button_2 = QPushButton(win)
    search_button_2.setText("Search on local")
    search_button_2.clicked.connect(lambda: search_action(Des_field))
    search_button_2.adjustSize()
    search_button_2.move(800,200)

    win.show()
    sys.exit(app.exec())


    



main()