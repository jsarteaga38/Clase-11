import math
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QPushButton, QLineEdit, \
    QFormLayout, QDialog, QDialogButtonBox, QVBoxLayout, QScrollArea, QWidget, QGridLayout, QButtonGroup

from cliente import Cliente
from ventana3 import Ventana3


class Ventana2(QMainWindow):
    def __init__(self, anterior):
        super(Ventana2, self).__init__(anterior)

        self.ventanaAnterior = anterior

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

        self.letrero1 = QLabel()
        self.letrero1.setText("Usuarios registrados.")
        self.letrero1.setFont(QFont("Arial", 20))
        self.letrero1.setStyleSheet("color: black;")

        self.vertical.addWidget(self.letrero1)

        self.vertical.addStretch()

        self.scrollArea = QScrollArea()

        self.scrollArea.setStyleSheet("background-color : transparent;")

        self.scrollArea.setWidgetResizable(True)

        self.contenedora = QWidget()

        self.cuadricula = QGridLayout(self.contenedora)

        self.scrollArea.setWidget(self.contenedora)

        self.vertical.addWidget(self.scrollArea)

        self.file = open('datos/cliente.txt', 'rb')

        self.usuarios = []

        while self.file:

            linea = self.file.readline().decode('UTF-8')

            lista = linea.split(";")

            if linea == '':
                break

            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10]
            )

            self.usuarios.append(u)

        self.file.close()

        self.numeroUsuarios = len(self.usuarios)

        self.contador = 0

        self.elementosPorColumna = 3

        self.numeroFilas = math.ceil(self.numeroUsuarios/ self.elementosPorColumna) + 1

        self.botones = QButtonGroup()

        self.botones.setExclusive(False)

        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna+1):

                if self.contador < self.numeroUsuarios:

                    self.ventanaAuxiliar = QWidget()

                    self.ventanaAuxiliar.setFixedHeight(100)
                    self.ventanaAuxiliar.setFixedWidth(200)


                    self.verticalCuadricula = QVBoxLayout()

                    self.botonAccion = QPushButton(self.usuarios[self.contador].documento)

                    self.botonAccion.setFixedWidth(150)

                    self.botonAccion.setStyleSheet("background-color: blue;"
                                          "color: white;"
                                          "padding: 10px;"
                                          "margin-top: 10px;")

                    self.verticalCuadricula.addWidget(self.botonAccion)

                    self.botones.addButton(self.botonAccion, int(self.usuarios[self.contador].documento))

                    self.verticalCuadricula.addStretch()

                    self.ventanaAuxiliar.setLayout(self.verticalCuadricula)

                    self.cuadricula.addWidget(self.ventanaAuxiliar, fila, columna)

                    self.contador += 1



        self.botones.idClicked.connect(self.metodo_accionBotones)



        self.botonFormaTabular = QPushButton("Forma tabular")
        self.botonFormaTabular.setFixedWidth(100)
        self.botonFormaTabular.setStyleSheet("background-color: blue;"
                                          "color: white;"
                                          "padding: 10px;"
                                          "margin-top: 10px;")
        self.botonFormaTabular.clicked.connect(self.metodo_botonFormaTabular)

        self.vertical.addWidget(self.botonFormaTabular)
        
        self.botonVolver = QPushButton("Volver")

        self.botonVolver.setFixedWidth(90)

        self.botonVolver.setStyleSheet("background-color: blue;"
                                          "color: white;"
                                          "padding: 10px;"
                                          "margin-top: 10px;")

        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        self.vertical.addWidget(self.botonVolver)

        self.fondo.setLayout(self.vertical)


    def metodo_accionBotones(self, cedulaUsuario):

        print(cedulaUsuario)


    def metodo_botonVolver(self):

        self.hide()

        self.ventanaAnterior.show()


    def metodo_botonFormaTabular(self):

        self.hide()
        self.ventana3 = Ventana3(self)
        self.ventana3.show()








if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana2 = Ventana2()

    ventana2.show()

    sys.exit(app.exec_())
