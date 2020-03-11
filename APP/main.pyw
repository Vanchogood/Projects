import sys, os, subprocess, threading
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
loader = QUiLoader()
def br1():
    i = 1
    if i == 1:
        def sshbr1():
            subprocess.run("putty cisco@192.168.254.3 22")
        tssh = threading.Thread(target=sshbr1, name='BR1')
        tssh.start()
        i += 1
    else:
        tssh.join()

def hq1():
    i = 1
    if i == 1:
        def sshhq1():
            subprocess.run("putty cisco@192.168.254.1 22")
        tssh = threading.Thread(target=sshhq1, name='HQ1')
        tssh.start()
        i += 1
    else:
        tssh.join()


def fw1():
    i = 1
    if i == 1:
        def sshfw1():
            subprocess.run("putty cisco@192.168.254.2 22")
        tssh = threading.Thread(target=sshfw1, name='FW1')
        tssh.start()
        i += 1
    else:
        tssh.join()

def sw1():
    i = 1
    if i == 1:
        def sshsw1():
            subprocess.run("putty cisco@192.168.254.10 22")
        tssh = threading.Thread(target=sshsw1, name='SW1')
        tssh.start()
        i += 1
    else:
        tssh.join()


def sw2():
    i = 1
    if i == 1:
        def sshsw2():
            subprocess.run("putty cisco@192.168.254.20 22")
        tssh = threading.Thread(target=sshsw2, name='SW2')
        tssh.start()
        i += 1
    else:
        tssh.join()


def sw3():
    i = 1
    if i == 1:
        def sshsw3():
            subprocess.run("putty cisco@192.168.254.30 22")
        tssh = threading.Thread(target=sshsw3, name='SW3')
        tssh.start()
        i += 1
    else:
        tssh.join()

def srv1():
    i = 1
    if i == 1:
        def sshsrv1():
            subprocess.run("putty cisco@192.168.254.10 22")
        tssh = threading.Thread(target=sshsrv1, name='SRV1')
        tssh.start()
        i += 1
    else:
        tssh.join()



def appstart():
    app = QtWidgets.QApplication(sys.argv)
    window = loader.load("test.ui", None)
    window.pushButton_BR1.clicked.connect (br1)
    window.pushButton_HQ1.clicked.connect (hq1)
    window.pushButton_FW1.clicked.connect (fw1)
    window.pushButton_SW1.clicked.connect (sw1)
    window.pushButton_SW2.clicked.connect (sw2)
    window.pushButton_SW3.clicked.connect (sw3)
    window.pushButton_SRV1.clicked.connect (srv1)
    window.show()
    app.exec_()

appstart()
