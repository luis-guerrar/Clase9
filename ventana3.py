import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDesktopWidget, QVBoxLayout, QScrollArea, QTableWidget, \
    QTableWidgetItem, QPushButton, QToolBar, QAction
from cliente import Cliente

class Ventana3(QMainWindow):
    def __init__(self, anterior):
        super(Ventana3, self).__init__(anterior)
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
        # Establecemos la distribución de los elementos con Layout vertical
        self.vertical = QVBoxLayout()

        # CONSTRUIR EL MENÚ TOOL BAR
        self.toolbar = QToolBar('Main toolbar')
        self.toolbar.setIconSize(QSize(32, 32))
        self.addToolBar(self.toolbar)

        # Eliminar
        self.delete = QAction(QIcon('imagenes/delete.png'), '&Delete', self)
        self.delete.triggered.connect(self.accionDelete)
        self.toolbar.addAction(self.delete)

        # Agregar
        self.add = QAction(QIcon('imagenes/add.png'), '&Add', self)
        self.add.triggered.connect(self.accionAdd)
        self.toolbar.addAction(self.add)

        # Editar
        self.edit = QAction(QIcon('imagenes/edit.png'), '&Edit', self)
        self.edit.triggered.connect(self.accionEdit)
        self.toolbar.addAction(self.edit)
        # FIN TOOLBAR


        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Les escribimos el texto
        self.letrero1.setText("Usuarios Registrados")

        # Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Andale Mono", 20))

        # Le ponemos el color de texto
        self.letrero1.setStyleSheet("color: #000000;")

        # Agregamos el letrero de la primera fila
        self.vertical.addWidget(self.letrero1)
        self.vertical.addStretch()

        self.scrollArea = QScrollArea()
        #self.scrollArea.setStyleSheet("background-color:#00B0F0;")
        self.scrollArea.setWidgetResizable(True)
        #self.scrollArea.setFixedHeight(500)

        # Creamos la tabla
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(11)

        # Definimos el ancho de las columnas
        self.tabla.setColumnWidth(0, 150)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setColumnWidth(3, 150)
        self.tabla.setColumnWidth(4, 150)
        self.tabla.setColumnWidth(5, 150)
        self.tabla.setColumnWidth(6, 150)
        self.tabla.setColumnWidth(7, 150)
        self.tabla.setColumnWidth(8, 150)
        self.tabla.setColumnWidth(9, 150)
        self.tabla.setColumnWidth(10, 150)

        # Definimos los encabezados de la tabla
        self.tabla.setHorizontalHeaderLabels(["Nombre",
                                              "Usuario",
                                              "Contraseña",
                                              "Documento",
                                              "Correo",
                                              "Pregunta 1",
                                              "Pregunta 2",
                                              "Pregunta 3",
                                              "Respuesta 1",
                                              "Respuesta 2",
                                              "Respuesta 3"])

        self.tabla.setRowCount(self.numeroUsuarios)

        for u in self.usuarios:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(u.nombreCompleto))
            # Hacemos que no se pueda editar
            self.tabla.item(self.contador, 0).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.clave))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
            self.tabla.item(self.contador, 3).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.correo))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.pregunta1))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.pregunta2))
            self.tabla.setItem(self.contador, 7, QTableWidgetItem(u.pregunta3))
            self.tabla.setItem(self.contador, 8, QTableWidgetItem(u.respuesta1))
            self.tabla.setItem(self.contador, 9, QTableWidgetItem(u.respuesta2))
            self.tabla.setItem(self.contador, 10, QTableWidgetItem(u.respuesta3))
            # Aumentamos el contador
            self.contador += 1

        # --------- OJO IMPORTANTE PONER AL FINAL --------------
        # Indicamos que el Layout principal del fondo es vertical
        self.fondo.setLayout(self.vertical)

        self.scrollArea.setWidget(self.tabla)
        self.vertical.addWidget(self.scrollArea)
        self.vertical.addStretch()

        # ----------------- BOTÓN VOLVER -----------------------
        self.btnVolver = QPushButton("Volver")
        self.btnVolver.setFixedWidth(186)
        self.btnVolver.setStyleSheet("background-color: #008B45;"
                                     "color: #FFFFFF;"
                                     "padding: 10px;")

        self.btnVolver.clicked.connect(self.accionBotonVolver)
        self.vertical.addWidget(self.btnVolver)

        self.fondo.setLayout(self.vertical)

    def accionBotonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def accionDelete(self):
        pass
    def accionAdd(self):
        pass
    def accionEdit(self):
        pass

if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana3 = Ventana3()

    ventana3.show()

    sys.exit(app.exec_())

