#!/usr/bin/env python3
import wiiu_cdndownload
import sys
import threading
import keygen
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout,
                             QPushButton, QLabel, QLineEdit, QMessageBox,
                             QWidget)

valid_tid_lows = ['00050000', '0005000E', '0005000C', '00050010', '0005001B', '00050030']

class Gui:
    def __init__(self):
        app = QApplication(sys.argv)
        app.setStyle('Fusion')

        self.win = QMainWindow()
        self.win.setWindowTitle('uShop')
        self.widget = QtWidgets.QWidget(self.win)
        self.win.setCentralWidget(self.widget)

        vbox = self.vbox_layout()
        self.set_common_key()

        self.win.setWindowFlags(self.win.windowFlags() & Qt.CustomizeWindowHint)
        self.win.setWindowFlags(self.win.windowFlags() & ~Qt.WindowMinMaxButtonsHint)
        self.win.setFixedSize(250, 0)
        self.widget.setLayout(vbox)
        self.win.show()
        sys.exit(app.exec_())
    
    def vbox_layout(self):
        vbox = QVBoxLayout()
        # Common Key
        ckey_text = QLabel('Common Key')
        self.ckey_input = QLineEdit()

        # Title ID
        tid_text = QLabel('Title ID')
        self.tid_input = QLineEdit()

        # Version
        version_text = QLabel('Version')
        self.version_input = QLineEdit()
        
        # Download Button
        dl_button = QPushButton('Download')
        dl_button.clicked.connect(self.download)

        # Download Progress
        self.dl_label = QLabel()
        self.dl_label.hide()

        # Append widgets
        vbox.addWidget(ckey_text)
        vbox.addWidget(self.ckey_input)
        vbox.addWidget(tid_text)
        vbox.addWidget(self.tid_input)
        vbox.addWidget(version_text)
        vbox.addWidget(self.version_input)
        vbox.addWidget(dl_button)
        vbox.addWidget(self.dl_label)
        return vbox
    
    def message_box(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle('uShop - Error')
        msg.setText(text)
        msg.exec_()

    def set_common_key(self):
        if keygen.verify_ckey():
            self.ckey_input.setText(keygen.get_ckey())
            self.ckey_input.setEnabled(False)

    def download(self):
        with open('ckey.txt', 'w') as f:
            f.write(self.ckey_input.text())
        self.set_common_key()

        if keygen.verify_ckey():
            if self.tid_input.text()[0:8] in valid_tid_lows and len(self.tid_input.text()) == 16:
                download = threading.Thread(target = wiiu_cdndownload.runDownload, args = (self.tid_input.text(), self.dl_label, self.version_input.text()))
                download.daemon = True
                self.dl_label.setText(f'Downloading: {self.tid_input.text()}...')
                self.dl_label.show()
                download.start()
            else:
                self.message_box('Invalid Title ID.')
        else:
            self.message_box('Invalid Common Key.')

Gui()