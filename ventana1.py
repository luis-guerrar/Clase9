import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout
from PyQt5 import QtGui

class Ventana1(QMainWindow):

    # Hacer el método de construcción de la ventana
    def __init__(self, parent=None):
        super().__init__(parent)

        # Poner el título
        self.setWindowTitle("Formulario de registro")

        # Poner el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/icono.png'))

        # Establecer las propiedades de ancho y alto
        self.ancho = 900
        self.alto = 600

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
        self.horizontal = QHBoxLayout()
        # Le ponemos las márgenes
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # ---------- LAYOUT IZQUIERDO -----------

        # Creamos el layout del lado izquierdo
        self.ladoIzquierdo = QFormLayout()

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Les escribimos el texto
        self.letrero1.setText("Información del cliente")

        # Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Andele Mono", 20))

        # --------- OJO IMPORTANTE PONER AL FINAL --------------

        # Indicamos que el Layout principal del fondo es horizontal
        self.fondo.setLayout(self.horizontal)

if __name__ == '__main__':

    app= QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())

