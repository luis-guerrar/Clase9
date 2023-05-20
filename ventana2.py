import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QApplication


class Ventana2(QMainWindow):

    def __init__(self, anterior):
        super(Ventana2, self).__init__(anterior)
        self.ventanaAnterior = anterior
        # Poner el título
        self.setWindowTitle("Formulario de registro")

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


        # --------- OJO IMPORTANTE PONER AL FINAL --------------

        # Indicamos que el Layout principal del fondo es vertical
        self.fondo.setLayout(self.vertical)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana2 = Ventana2()

    ventana2.show()

    sys.exit(app.exec_())
