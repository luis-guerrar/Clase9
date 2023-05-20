import math
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QApplication, QScrollArea, QWidget, \
    QGridLayout, QPushButton, QButtonGroup

from cliente import Cliente
from ventana3 import Ventana3

class Ventana2(QMainWindow):

    def __init__(self, anterior):
        super(Ventana2, self).__init__(anterior)
        self.ventanaAnterior = anterior
        # Poner el título
        self.setWindowTitle("Usuarios registrados")

        # Poner el ícono
        self.setWindowIcon(QtGui.QIcon('imagenes/icono.png'))

        # Establecer las propiedades de ancho y alto
        self.ancho = 1000
        self.alto = 700

        # Establecer el tamaño de la ventana
        self.resize(self.ancho, self.alto)

        # Hacer que la ventana se vea en el centro
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Fijar el ancho y el alto de la ventana
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Establecemos el fondo principal
        self.fondo = QLabel(self)

        # Definimos la imagen de fondo
        self.imagenFondo = QPixmap('imagenes/fondo.png')

        # Definimos la imagen de fondo
        self.fondo.setPixmap(self.imagenFondo)
        # Establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)
        # Hacemos que se adapte el tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como la ventana central
        self.setCentralWidget(self.fondo)
        # Establecemos la distribución de los elementos con Layout horizontal
        self.vertical = QVBoxLayout()

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Les escribimos el texto
        self.letrero1.setText("Usuarios registrados")

        # Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Andale Mono", 20))

        # Le ponemos el color de texto
        self.letrero1.setStyleSheet("color: #000000;")

        # Agregamos el letrero de la primera fila
        self.vertical.addWidget(self.letrero1)
        self.vertical.addStretch()

        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet("background-color:transparent;")
        self.scrollArea.setWidgetResizable(True)

        self.contenedora = QWidget()
        self.cuadricula = QGridLayout(self.contenedora)
        self.scrollArea.setWidget(self.contenedora)
        self.vertical.addWidget(self.scrollArea)

        self.file = open('datos/clientes.txt', 'rb')
        self.usuarios = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')
            lista = linea.split(";")

            # paramos el bucle si ya no encuentra más registros en el archivo
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
                lista[10])
            # Agregar los datos a la lista
            self.usuarios.append(u)

        # cerramos ael archivo txt
        self.file.close()

        '''En este punto tenemos la lista de todos los usuarios, se procede
         a obtener el número de usuarios y consultamos el tamaño de la lista'''
        self.numeroUsuarios = len(self.usuarios)
        self.contador = 0

        self.elementosPorColumna = 3
        self.numerosFilas = math.ceil(self.numeroUsuarios / self.elementosPorColumna) + 1

        self.botones = QButtonGroup()
        # Se define que la botones se encargue de todos los botone no de uno exclusivamente
        self.botones.setExclusive(False)

        for fila in range(self.numerosFilas):
            for columna in range(self.elementosPorColumna):
                if self.contador < self.numeroUsuarios:
                    self.ventanaAuxiliar = QWidget()
                    self.ventanaAuxiliar.setFixedWidth(200)
                    self.ventanaAuxiliar.setFixedHeight(50)
                    self.verticalCuadricula = QVBoxLayout()

                    # Creamos un botón por cada usuario
                    self.btnAccion = QPushButton(self.usuarios[self.contador].nombreCompleto)
                    self.btnAccion.setFixedWidth(186)
                    self.btnAccion.setStyleSheet('background-color: #008B45;'
                                                   'color:#FFFFFF;'
                                                   'padding:5px;')
                    self.verticalCuadricula.addWidget(self.btnAccion)
                    self.botones.addButton(self.btnAccion, int(self.usuarios[self.contador].documento))
                    self.verticalCuadricula.addStretch()
                    self.ventanaAuxiliar.setLayout(self.verticalCuadricula)
                    self.cuadricula.addWidget(self.ventanaAuxiliar, fila, columna)
                    self.contador += 1

        self.botones.idClicked.connect(self.accionBotones)


        # ----------------- BOTÓN VOLVER -----------------------
        self.btnVolver = QPushButton("Volver")
        self.btnVolver.setFixedWidth(186)
        self.btnVolver.setStyleSheet("background-color: #008B45;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;")

        self.btnVolver.clicked.connect(self.accionBotonVolver)

        # -------------- BOTÓN FORMA TABULAR -------------------
        self.btnTabularForm = QPushButton("Forma Tabular")
        self.btnTabularForm.setFixedWidth(186)
        self.btnTabularForm.setStyleSheet("background-color: #008B45;"
                                     "color: #FFFFFF;"
                                     "padding: 10px;")

        self.btnTabularForm.clicked.connect(self.accionBotonTabularForm)
        self.vertical.addWidget(self.btnTabularForm)
        self.vertical.addWidget(self.btnVolver)

        # --------- OJO IMPORTANTE PONER AL FINAL --------------

        # Indicamos que el Layout principal del fondo es vertical
        self.fondo.setLayout(self.vertical)

    def accionBotones(self, cc):
        print(cc)

    def accionBotonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def accionBotonTabularForm(self):
        self.hide()
        self.ventana3 = Ventana3(self)
        self.ventana3.show()
