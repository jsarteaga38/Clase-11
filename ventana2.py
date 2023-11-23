import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QPushButton, QLineEdit, \
    QFormLayout, QDialog, QDialogButtonBox, QVBoxLayout




class Ventana2(QMainWindow):
    def __init__(self, parent=None):
        super(Ventana2, self).__init__(parent)

        self.setWindowTitle("Usuarios registrados")

        self.setWindowIcon(QtGui.QIcon("Imagenes/img.png"))

        self.ancho = 900
        self.alto = 600

        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap('Imagenes/img3.png')
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())
        self.setCentralWidget(self.fondo)

        self.vertical = QVBoxLayout()

        self.fondo.setLayout(self.vertical)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana2 = Ventana2()

    ventana2.show()

    sys.exit(app.exec_())
